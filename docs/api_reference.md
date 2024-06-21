
# pyVisio API Referansı

## Charts

### `line_chart`

Çizgi grafiği oluşturur.

**Parametreler**:
- `data` (list): Grafik için veri.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `xlabel` (str, optional): X ekseni etiketi. Varsayılan `None`.
- `ylabel` (str, optional): Y ekseni etiketi. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.
- `color` (str, optional): Çizgi rengi. Varsayılan `'blue'`.
- `linestyle` (str, optional): Çizgi stili. Varsayılan `'-'`.
- `marker` (str, optional): Veri noktası işaretçisi. Varsayılan `'o'`.

**Örnek**:

```python
import pyVisio as tp

data = [1, 2, 3, 4, 5]
tp.line_chart(data, title="Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='red')
```

### `bar_chart`

Çubuk grafiği oluşturur.

**Parametreler**:
- `data` (dict): Grafik için veri.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `xlabel` (str, optional): X ekseni etiketi. Varsayılan `None`.
- `ylabel` (str, optional): Y ekseni etiketi. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.
- `color` (str, optional): Çubuk rengi. Varsayılan `'blue'`.

**Örnek**:

```python
import pyVisio as tp

data_bar = {'A': 10, 'B': 20, 'C': 30}
tp.bar_chart(data_bar, title="Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", color='blue')
```

### `scatter_plot`

Dağılım grafiği oluşturur.

**Parametreler**:
- `x_data` (list): X ekseni verisi.
- `y_data` (list): Y ekseni verisi.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `xlabel` (str, optional): X ekseni etiketi. Varsayılan `None`.
- `ylabel` (str, optional): Y ekseni etiketi. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.
- `color` (str, optional): Nokta rengi. Varsayılan `'blue'`.

**Örnek**:

```python
import pyVisio as tp

x_data = [1, 2, 3, 4, 5]
y_data = [10, 14, 12, 15, 10]
tp.scatter_plot(x_data, y_data, title="Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='blue')
```

### `pie_chart`

Pasta grafiği oluşturur.

**Parametreler**:
- `data` (dict): Grafik için veri.
- `title` (str, optional): Grafik başlığı. Varsayılan `None`.
- `interactive` (bool, optional): Etkileşimli grafik oluşturur. Varsayılan `False`.

**Örnek**:

```python
import pyVisio as tp

data_pie = {'Elma': 50, 'Armut': 30, 'Kiraz': 20}
tp.pie_chart(data_pie, title="Pasta Grafiği")
```

## Themes

### `set_theme`

Grafik temalarını ayarlar.

**Parametreler**:
- `theme` (str): Tema adı. `'dark'` veya `'light'` olabilir.

**Örnek**:

```python
import pyVisio as tp

tp.set_theme('dark')
```

## Live Charts

### `LiveChart`

Canlı veri güncellemeleri için sınıf.

**Metodlar**:
- `__init__(self, title="Canlı Grafik")`: Yeni bir canlı grafik oluşturur.
- `update_line_chart(self, x_data, y_data)`: Çizgi grafiğini günceller.
- `start_live_update(self, update_function, interval=1)`: Belirli aralıklarla grafiği günceller.

**Örnek**:

```python
import numpy as np
import time
import pyVisio as tp

def get_live_data():
    x = list(range(10))
    y = np.random.randint(0, 10, size=10)
    return x, y

live_chart = tp.LiveChart(title="Canlı Çizgi Grafiği")
live_chart.start_live_update(get_live_data, interval=2)
```

## Data Analysis

### `analyze_data`

Veriyi analiz eder.

**Parametreler**:
- `data` (dict): Analiz edilecek veri.

**Döndürür**:
- `description` (DataFrame): Betimsel istatistikler.
- `correlation` (DataFrame): Korelasyon matrisi.

**Örnek**:

```python
import pyVisio as tp

data_analysis = {
    'column1': [1, 2, 3, 4, 5],
    'column2': [5, 4, 3, 2, 1]
}

description, correlation = tp.analyze_data(data_analysis)
print("Betimsel İstatistikler:")
print(description)
print("
Korelasyon Matrisi:")
print(correlation)
```

### `linear_regression`

Doğrusal regresyon analizi yapar.

**Parametreler**:
- `x` (array-like): Bağımsız değişkenler.
- `y` (array-like): Bağımlı değişkenler.

**Döndürür**:
- `summary` (str): Model özeti.
- `predictions` (array): Tahminler.

**Örnek**:

```python
import pyVisio as tp
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 3, 2, 5])

summary, predictions = tp.linear_regression(x, y)
print(summary)
```

### `time_series_analysis`

Zaman serisi analizi yapar.

**Parametreler**:
- `data` (array-like): Zaman serisi verisi.
- `lags` (int, optional): Lag sayısı. Varsayılan `1`.

**Döndürür**:
- `summary` (str): Model özeti.
- `forecast` (array): Tahminler.

**Örnek**:

```python
import warnings
import pyVisio as tp
import numpy as np

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    data_ts = np.random.randn(1000)
    summary, forecast = tp.time_series_analysis(data_ts)
    print(summary)
    print("Forecast:", forecast)
```
