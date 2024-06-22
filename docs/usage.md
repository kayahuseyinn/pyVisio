
# pyVisio Kullanım Kılavuzu

## Kurulum

pyVisio'yu pip ile kurabilirsiniz:

```bash
pip install pyVisio
```

Geliştirme sürümünü yüklemek için, projeyi klonlayıp `pip install -e .` komutunu çalıştırabilirsiniz:

```bash
git clone https://github.com/kayahuseyinn/pyVisio.git
cd pyVisio
pip install -e .
```

## Temel Kullanım

### Çizgi Grafiği

Çizgi grafiği oluşturmak için `line_chart` fonksiyonunu kullanabilirsiniz.

```python
import pyVisio as pv

data = [1, 2, 3, 4, 5]
pv.line_chart(data, title="Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='red')
```

### Etkileşimli Çizgi Grafiği

Etkileşimli çizgi grafiği oluşturmak için `line_chart` fonksiyonunun `interactive` parametresini `True` olarak ayarlayabilirsiniz.

```python
pv.line_chart(data, title="Etkileşimli Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", interactive=True, color='green')
```

### Çubuk Grafiği

Çubuk grafiği oluşturmak için `bar_chart` fonksiyonunu kullanabilirsiniz.

```python
data_bar = {'A': 10, 'B': 20, 'C': 30}
pv.bar_chart(data_bar, title="Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", color='blue')
```

### Etkileşimli Çubuk Grafiği

Etkileşimli çubuk grafiği oluşturmak için `bar_chart` fonksiyonunun `interactive` parametresini `True` olarak ayarlayabilirsiniz.

```python
pv.bar_chart(data_bar, title="Etkileşimli Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", interactive=True, color='purple')
```

### Dağılım Grafiği

Dağılım grafiği oluşturmak için `scatter_plot` fonksiyonunu kullanabilirsiniz.

```python
x_data = [1, 2, 3, 4, 5]
y_data = [10, 14, 12, 15, 10]
pv.scatter_plot(x_data, y_data, title="Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='blue')
```

### Etkileşimli Dağılım Grafiği

Etkileşimli dağılım grafiği oluşturmak için `scatter_plot` fonksiyonunun `interactive` parametresini `True` olarak ayarlayabilirsiniz.

```python
pv.scatter_plot(x_data, y_data, title="Etkileşimli Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", interactive=True, color='orange')
```

### Pasta Grafiği

Pasta grafiği oluşturmak için `pie_chart` fonksiyonunu kullanabilirsiniz.

```python
data_pie = {'Elma': 50, 'Armut': 30, 'Kiraz': 20}
pv.pie_chart(data_pie, title="Pasta Grafiği")
```

### Etkileşimli Pasta Grafiği

Etkileşimli pasta grafiği oluşturmak için `pie_chart` fonksiyonunun `interactive` parametresini `True` olarak ayarlayabilirsiniz.

```python
pv.pie_chart(data_pie, title="Etkileşimli Pasta Grafiği", interactive=True)
```

### Zaman Serisi Analizi

Zaman serisi analizi yapmak için `time_series_analysis` fonksiyonunu kullanabilirsiniz.

```python
import pyVisio as pv
import numpy as np

data_ts = np.random.randn(100)
summary, forecast, anomalies = pv.time_series_analysis(data_ts, detect_anomalies=True)
print(summary)
print("Forecast:", forecast)
print("Anomalies:", anomalies)
```

### Anomali Tespiti

Zaman serisi verisinde anomali tespiti yapmak için `detect_anomalies_in_series` fonksiyonunu kullanabilirsiniz.

```python
import pyVisio as pv
import numpy as np

data_ts = np.random.randn(100)
anomalies = pv.detect_anomalies_in_series(data_ts)
print("Anomalies:", anomalies)
```

### Rapor Oluşturma

Otomatik rapor oluşturmak için `generate_report` fonksiyonunu kullanabilirsiniz.

```python
import pyVisio as pv

report_data = {
    'title': 'Veri Analiz Raporu',
    'author': 'Hüseyin Kaya',
    'date': '2024-06-22',
    'content': [
        {'type': 'line_chart', 'data': [1, 2, 3, 4, 5], 'title': 'Çizgi Grafiği'},
        {'type': 'bar_chart', 'data': {'A': 10, 'B': 20, 'C': 30}, 'title': 'Çubuk Grafiği'}
    ]
}
pv.generate_report(report_data, format='pdf', output_path='report.pdf')
```

### Veri Temizleme

Veri temizleme işlemi yapmak için `clean_data` fonksiyonunu kullanabilirsiniz.

```python
import pyVisio as pv

raw_data = {'column1': [1, 2, None, 4, 5], 'column2': [5, None, 3, 2, 1]}
cleaned_data = pv.clean_data(raw_data, method='fillna', fill_value=0)
pv.line_chart(cleaned_data['column1'], title="Temizlenmiş Veri ile Çizgi Grafiği")
```

### Tema Ayarlama

Grafiklerin temasını ayarlamak için `set_theme` fonksiyonunu kullanabilirsiniz.

```python
import pyVisio as pv

custom_theme = {
    'background_color': 'black',
    'grid_color': 'gray',
    'line_color': 'cyan',
    'font_family': 'Arial'
}
pv.set_theme(custom_theme)
pv.line_chart([1, 2, 3, 4, 5], title="Özelleştirilmiş Tema ile Çizgi Grafiği")
```
