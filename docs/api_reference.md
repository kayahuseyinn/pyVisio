
# pyVisio API Referansı

## İçindekiler
- [Giriş](#giriş)
- [Fonksiyonlar](#fonksiyonlar)
  - [line_chart](#line_chart)
  - [bar_chart](#bar_chart)
  - [scatter_plot](#scatter_plot)
  - [pie_chart](#pie_chart)
  - [time_series_analysis](#time_series_analysis)
  - [detect_anomalies_in_series](#detect_anomalies_in_series)
  - [clean_data](#clean_data)
  - [set_theme](#set_theme)
  - [live_line_chart](#live_line_chart)
  - [live_bar_chart](#live_bar_chart)
  - [generate_report](#generate_report)
  - [basic_analysis](#basic_analysis)
  - [advanced_analysis](#advanced_analysis)

## Giriş
`pyVisio`, zengin ve etkileşimli görselleştirmeler için kapsamlı araçlar sağlayan dinamik ve etkileşimli bir veri görselleştirme kütüphanesidir. Bu kütüphane, çeşitli grafik türleri oluşturma, veri analizi yapma ve raporlar oluşturma yeteneklerini sunar.

## Fonksiyonlar

### line_chart
```python
def line_chart(data, title="Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='mavi', interactive=False):
```
Bir çizgi grafiği oluşturur.

#### Parametreler
- **data**: (list) Sayısal değerlerden oluşan liste.
- **title**: (str) Grafiğin başlığı.
- **xlabel**: (str) X ekseni etiketi.
- **ylabel**: (str) Y ekseni etiketi.
- **color**: (str) Çizginin rengi.
- **interactive**: (bool) Grafiğin etkileşimli olup olmadığını belirtir.

### bar_chart
```python
def bar_chart(data, title="Bar Grafiği", xlabel="Kategori", ylabel="Değer", color='mavi', interactive=False):
```
Bir bar grafiği oluşturur.

#### Parametreler
- **data**: (dict) Kategoriler anahtarlar ve sayısal değerler içeren sözlük.
- **title**: (str) Grafiğin başlığı.
- **xlabel**: (str) X ekseni etiketi.
- **ylabel**: (str) Y ekseni etiketi.
- **color**: (str) Barların rengi.
- **interactive**: (bool) Grafiğin etkileşimli olup olmadığını belirtir.

### scatter_plot
```python
def scatter_plot(x_data, y_data, title="Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='mavi', interactive=False):
```
Bir dağılım grafiği oluşturur.

#### Parametreler
- **x_data**: (list) X ekseni için sayısal değerlerden oluşan liste.
- **y_data**: (list) Y ekseni için sayısal değerlerden oluşan liste.
- **title**: (str) Grafiğin başlığı.
- **xlabel**: (str) X ekseni etiketi.
- **ylabel**: (str) Y ekseni etiketi.
- **color**: (str) Noktaların rengi.
- **interactive**: (bool) Grafiğin etkileşimli olup olmadığını belirtir.

### pie_chart
```python
def pie_chart(data, title="Pasta Grafiği", interactive=False):
```
Bir pasta grafiği oluşturur.

#### Parametreler
- **data**: (dict) Kategoriler anahtarlar ve sayısal değerler içeren sözlük.
- **title**: (str) Grafiğin başlığı.
- **interactive**: (bool) Grafiğin etkileşimli olup olmadığını belirtir.

### time_series_analysis
```python
def time_series_analysis(data, lags=1, detect_anomalies=False, anomaly_threshold=3):
```
Zaman serisi analizi yapar.

#### Parametreler
- **data**: (list veya numpy array) Sayısal değerlerden oluşan veri.
- **lags**: (int) ARIMA modelinde kullanılacak lag sayısı.
- **detect_anomalies**: (bool) Anomalileri tespit edip etmeyeceğini belirtir.
- **anomaly_threshold**: (int) Anomalileri tespit etmek için eşik değeri.

### detect_anomalies_in_series
```python
def detect_anomalies_in_series(data, threshold=3):
```
Bir zaman serisinde anomalileri tespit eder.

#### Parametreler
- **data**: (list veya numpy array) Sayısal değerlerden oluşan veri.
- **threshold**: (int) Anomalileri tespit etmek için eşik değeri.

### clean_data
```python
def clean_data(data, method='fillna', fill_value=0):
```
Veriyi temizler.

#### Parametreler
- **data**: (dict veya pandas DataFrame) Temizlenecek veri.
- **method**: (str) Veriyi temizlemek için kullanılacak yöntem ('fillna', 'dropna').
- **fill_value**: (herhangi bir değer) 'fillna' yöntemi kullanılıyorsa NaN değerlerini doldurmak için kullanılacak değer.

### set_theme
```python
def set_theme(theme):
```
Grafikler için temayı ayarlar.

#### Parametreler
- **theme**: (dict) 'background_color', 'grid_color', 'line_color', 'font_family' anahtarlarına sahip sözlük.

### live_line_chart
```python
def live_line_chart(data, title="Canlı Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='mavi'):
```
Bir canlı çizgi grafiği oluşturur.

#### Parametreler
- **data**: (list) Sayısal değerlerden oluşan liste.
- **title**: (str) Grafiğin başlığı.
- **xlabel**: (str) X ekseni etiketi.
- **ylabel**: (str) Y ekseni etiketi.
- **color**: (str) Çizginin rengi.

### live_bar_chart
```python
def live_bar_chart(data, title="Canlı Bar Grafiği", xlabel="Kategori", ylabel="Değer", color='mavi'):
```
Bir canlı bar grafiği oluşturur.

#### Parametreler
- **data**: (dict) Kategoriler anahtarlar ve sayısal değerler içeren sözlük.
- **title**: (str) Grafiğin başlığı.
- **xlabel**: (str) X ekseni etiketi.
- **ylabel**: (str) Y ekseni etiketi.
- **color**: (str) Barların rengi.

### generate_report
```python
def generate_report(report_data, format='pdf', output_path='rapor.pdf'):
```
Bir rapor oluşturur.

#### Parametreler
- **report_data**: (dict) Rapor detaylarını içeren sözlük.
- **format**: (str) Raporun formatı ('pdf', 'html').
- **output_path**: (str) Raporun kaydedileceği yol.

### basic_analysis
```python
def basic_analysis(data):
```
Veri üzerinde temel analiz yapar.

#### Parametreler
- **data**: (list) Sayısal değerlerden oluşan liste.

### advanced_analysis
```python
def advanced_analysis(data):
```
Veri üzerinde ileri düzey analiz yapar.

#### Parametreler
- **data**: (list) Sayısal değerlerden oluşan liste.
