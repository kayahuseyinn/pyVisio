import pyVisio as pv

# Veri seti
data_pie = {'Elma': 50, 'Armut': 30, 'Kiraz': 20}

# Temel Pasta Grafiği
pv.pie_chart(data_pie, title="Pasta Grafiği")

# Etkileşimli Pasta Grafiği
pv.pie_chart(data_pie, title="Etkileşimli Pasta Grafiği", interactive=True)
