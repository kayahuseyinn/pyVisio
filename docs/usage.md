
# pyVisio Kullanım Kılavuzu

## Kurulum

pyVisio'i pip ile kurabilirsiniz:

```bash
pip install pyVisio
```

Geliştirme sürümünü yüklemek için, projeyi klonlayıp `pip install -e .` komutunu çalıştırabilirsiniz:

```bash
git clone https://github.com/yourusername/pyVisio.git
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

### Temalar ve Modlar

pyVisio, grafiklerinize modern ve çekici temalar eklemenize olanak tanır. Temaları kullanmak için `set_theme` fonksiyonunu kullanabilirsiniz.

#### Dark Mode

```python
pv.set_theme('dark')
```

#### Light Mode

```python
pv.set_theme('light')
```

### Canlı Veri Güncellemeleri

Canlı veri güncellemeleri yapabilmek için `LiveChart` sınıfını kullanabilirsiniz.

```python
import numpy as np
import time

def get_live_data():
    x = list(range(10))
    y = np.random.randint(0, 10, size=10)
    return x, y

live_chart = pv.LiveChart(title="Canlı Çizgi Grafiği")
live_chart.start_live_update(get_live_data, interval=2)
```

### Veri Analizi

#### Betimsel İstatistikler ve Korelasyon Matrisi

```python
data_analysis = {
    'column1': [1, 2, 3, 4, 5],
    'column2': [5, 4, 3, 2, 1]
}

description, correlation = pv.analyze_data(data_analysis)
print("Betimsel İstatistikler:")
print(description)
print("
Korelasyon Matrisi:")
print(correlation)
```

#### Doğrusal Regresyon

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 3, 2, 5])

summary, predictions = pv.linear_regression(x, y)
print(summary)
```

#### Zaman Serisi Analizi

```python
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    data_ts = np.random.randn(1000)
    summary, forecast = pv.time_series_analysis(data_ts)
    print(summary)
    print("Forecast:", forecast)
```
