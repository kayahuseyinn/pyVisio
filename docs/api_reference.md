
# API Referansı

## `line_chart`

Çizgi grafiği oluşturur.

**Parametreler**:
- `data` (list): Grafik için veri.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `xlabel` (str, optional): X ekseni etiketi. Varsayılan `None`.
- `ylabel` (str, optional): Y ekseni etiketi. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.
- `color` (str, optional): Çizgi rengi. Varsayılan `'blue'`.

**Örnek**:

```python
import pyVisio as pv

data = [1, 2, 3, 4, 5]
pv.line_chart(data, title="Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='red')
```

## `bar_chart`

Çubuk grafiği oluşturur.

**Parametreler**:
- `data` (dict): Kategoriler ve değerler.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `xlabel` (str, optional): X ekseni etiketi. Varsayılan `None`.
- `ylabel` (str, optional): Y ekseni etiketi. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.
- `color` (str, optional): Çubuk rengi. Varsayılan `'blue'`.

**Örnek**:

```python
data_bar = {'A': 10, 'B': 20, 'C': 30}
pv.bar_chart(data_bar, title="Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", color='blue')
```

## `scatter_plot`

Dağılım grafiği oluşturur.

**Parametreler**:
- `x_data` (list): X ekseni verisi.
- `y_data` (list): Y ekseni verisi.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `xlabel` (str, optional): X ekseni etiketi. Varsayılan `None`.
- `ylabel` (str, optional): Y ekseni etiketi. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.
- `color` (str, optional): Noktaların rengi. Varsayılan `'blue'`.

**Örnek**:

```python
import pyVisio as pv

x_data = [1, 2, 3, 4, 5]
y_data = [10, 14, 12, 15, 10]
pv.scatter_plot(x_data, y_data, title="Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='blue')
```

## `pie_chart`

Pasta grafiği oluşturur.

**Parametreler**:
- `data` (dict): Kategoriler ve değerler.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.

**Örnek**:

```python
data_pie = {'Elma': 50, 'Armut': 30, 'Kiraz': 20}
pv.pie_chart(data_pie, title="Pasta Grafiği")
```

## `time_series_analysis`

Zaman serisi analizi yapar.

**Parametreler**:
- `data` (list): Zaman serisi verisi.
- `lags` (int, optional): Gecikme sayısı. Varsayılan `1`.
- `detect_anomalies` (bool, optional): Anomali tespiti yapar. Varsayılan `False`.

**Örnek**:

```python
import pyVisio as pv
import numpy as np

data_ts = np.random.randn(100)
summary, forecast, anomalies = pv.time_series_analysis(data_ts, detect_anomalies=True)
print(summary)
print("Forecast:", forecast)
print("Anomalies:", anomalies)
```

## `detect_anomalies_in_series`

Zaman serisi verisinde anomali tespiti yapar.

**Parametreler**:
- `data` (list): Zaman serisi verisi.

**Örnek**:

```python
import pyVisio as pv
import numpy as np

data_ts = np.random.randn(100)
anomalies = pv.detect_anomalies_in_series(data_ts)
print("Anomalies:", anomalies)
```

## `generate_report`

Otomatik rapor oluşturur.

**Parametreler**:
- `report_data` (dict): Rapor verisi.
- `format` (str, optional): Rapor formatı. Varsayılan `'pdf'`.
- `output_path` (str, optional): Rapor çıktısı yolu. Varsayılan `'report.pdf'`.

**Örnek**:

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

## `clean_data`

Veri temizleme işlemi yapar.

**Parametreler**:
- `data` (dict): Temizlenecek veri.
- `method` (str, optional): Temizleme yöntemi. Varsayılan `'fillna'`.
- `fill_value` (any, optional): Eksik verilerin doldurulacağı değer. Varsayılan `0`.

**Örnek**:

```python
import pyVisio as pv

raw_data = {'column1': [1, 2, None, 4, 5], 'column2': [5, None, 3, 2, 1]}
cleaned_data = pv.clean_data(raw_data, method='fillna', fill_value=0)
pv.line_chart(cleaned_data['column1'], title="Temizlenmiş Veri ile Çizgi Grafiği")
```

## `set_theme`

Grafiklerin temasını ayarlar.

**Parametreler**:
- `theme` (dict): Tema ayarları.

**Örnek**:

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

