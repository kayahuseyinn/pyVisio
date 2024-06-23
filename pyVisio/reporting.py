from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from jinja2 import Template
import matplotlib.pyplot as plt
import io

def generate_report(report_data, format='pdf', output_path='report.pdf'):
    """
    Generates a report with the given data.

    Parameters:
        report_data (dict): The data for the report.
        format (str, optional): The format of the report. Default is 'pdf'.
        output_path (str, optional): The output path for the report. Default is 'report.pdf'.

    Returns:
        None
    """
    if format != 'pdf':
        raise ValueError("Currently only 'pdf' format is supported")

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    title = report_data.get('title', 'Data Analysis Report')
    author = report_data.get('author', 'Unknown')
    date = report_data.get('date', 'Unknown')

    elements.append(Paragraph(title, styles['Title']))
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph(f"Author: {author}", styles['Normal']))
    elements.append(Paragraph(f"Date: {date}", styles['Normal']))
    elements.append(Spacer(1, 0.5*inch))

    for item in report_data['content']:
        elements.append(Paragraph(item['title'], styles['Heading2']))
        elements.append(Spacer(1, 0.2*inch))
        
        if item['type'] == 'line_chart':
            fig, ax = plt.subplots()
            ax.plot(item['data'])
            ax.set_title(item['title'])
            ax.set_xlabel('X Axis')
            ax.set_ylabel('Y Axis')
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            elements.append(Spacer(1, 0.2*inch))
            elements.append(Image(buf, width=5*inch, height=3*inch))
            plt.close(fig)
        
        elif item['type'] == 'bar_chart':
            fig, ax = plt.subplots()
            ax.bar(item['data'].keys(), item['data'].values())
            ax.set_title(item['title'])
            ax.set_xlabel('Category')
            ax.set_ylabel('Value')
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            elements.append(Spacer(1, 0.2*inch))
            elements.append(Image(buf, width=5*inch, height=3*inch))
            plt.close(fig)
        
        elif item['type'] == 'table':
            table_data = [list(item['data'].keys())] + list(zip(*item['data'].values()))
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            elements.append(table)
            elements.append(Spacer(1, 0.2*inch))

    doc.build(elements)
