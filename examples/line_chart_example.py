import pyVisio as pv

# Veri seti
data = [1, 2, 3, 4, 5]

# Temel Çizgi Grafiği
pv.line_chart(data, title="Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='red')

# Etkileşimli Çizgi Grafiği
pv.line_chart(data, title="Etkileşimli Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", interactive=True, color='green')
