import weasyprint
from jinja2 import Template

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
    template = Template("""
    <html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ title }}</h1>
        <p>Author: {{ author }}</p>
        <p>Date: {{ date }}</p>
        {% for item in content %}
            <h2>{{ item.title }}</h2>
            <p>Type: {{ item.type }}</p>
            <p>Data: {{ item.data }}</p>
        {% endfor %}
    </body>
    </html>
    """)

    html_content = template.render(
        title=report_data['title'],
        author=report_data['author'],
        date=report_data['date'],
        content=report_data['content']
    )

    if format == 'pdf':
        weasyprint.HTML(string=html_content).write_pdf(output_path)

    # Add more formats if needed

