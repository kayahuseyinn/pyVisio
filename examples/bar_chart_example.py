import pyVisio as pv

# Veri seti
data_bar = {'A': 10, 'B': 20, 'C': 30}

# Temel Çubuk Grafiği
pv.bar_chart(data_bar, title="Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", color='blue')

# Etkileşimli Çubuk Grafiği
pv.bar_chart(data_bar, title="Etkileşimli Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", interactive=True, color='purple')
