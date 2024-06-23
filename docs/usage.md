
# pyVisio Kullanım Kılavuzu

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
pv.line_chart(data, title="Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='mavi', interactive=False)
```
Bir çizgi grafiği oluşturur.

- **data**: Sayısal değerlerden oluşan liste
- **title**: Grafiğin başlığı (str)
- **xlabel**: X ekseni etiketi (str)
- **ylabel**: Y ekseni etiketi (str)
- **color**: Çizginin rengi (str)
- **interactive**: Grafiğin etkileşimli olup olmadığını belirtir (bool)

### bar_chart
```python
pv.bar_chart(data, title="Bar Grafiği", xlabel="Kategori", ylabel="Değer", color='mavi', interactive=False)
```
Bir bar grafiği oluşturur.

- **data**: Kategoriler anahtarlar ve sayısal değerler içeren sözlük
- **title**: Grafiğin başlığı (str)
- **xlabel**: X ekseni etiketi (str)
- **ylabel**: Y ekseni etiketi (str)
- **color**: Barların rengi (str)
- **interactive**: Grafiğin etkileşimli olup olmadığını belirtir (bool)

### scatter_plot
```python
pv.scatter_plot(x_data, y_data, title="Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='mavi', interactive=False)
```
Bir dağılım grafiği oluşturur.

- **x_data**: X ekseni için sayısal değerlerden oluşan liste
- **y_data**: Y ekseni için sayısal değerlerden oluşan liste
- **title**: Grafiğin başlığı (str)
- **xlabel**: X ekseni etiketi (str)
- **ylabel**: Y ekseni etiketi (str)
- **color**: Noktaların rengi (str)
- **interactive**: Grafiğin etkileşimli olup olmadığını belirtir (bool)

### pie_chart
```python
pv.pie_chart(data, title="Pasta Grafiği", interactive=False)
```
Bir pasta grafiği oluşturur.

- **data**: Kategoriler anahtarlar ve sayısal değerler içeren sözlük
- **title**: Grafiğin başlığı (str)
- **interactive**: Grafiğin etkileşimli olup olmadığını belirtir (bool)

### time_series_analysis
```python
pv.time_series_analysis(data, lags=1, detect_anomalies=False, anomaly_threshold=3)
```
Zaman serisi analizi yapar.

- **data**: Sayısal değerlerden oluşan liste veya numpy array
- **lags**: ARIMA modelinde kullanılacak lag sayısı (int)
- **detect_anomalies**: Anomalileri tespit edip etmeyeceğini belirtir (bool)
- **anomaly_threshold**: Anomalileri tespit etmek için eşik değeri (int)

### detect_anomalies_in_series
```python
pv.detect_anomalies_in_series(data, threshold=3)
```
Bir zaman serisinde anomalileri tespit eder.

- **data**: Sayısal değerlerden oluşan liste veya numpy array
- **threshold**: Anomalileri tespit etmek için eşik değeri (int)

### clean_data
```python
pv.clean_data(data, method='fillna', fill_value=0)
```
Veriyi temizler.

- **data**: Sözlük veya pandas DataFrame
- **method**: Veriyi temizlemek için kullanılacak yöntem ('fillna', 'dropna') (str)
- **fill_value**: 'fillna' yöntemi kullanılıyorsa NaN değerlerini doldurmak için kullanılacak değer

### set_theme
```python
pv.set_theme(theme)
```
Grafikler için temayı ayarlar.

- **theme**: 'background_color', 'grid_color', 'line_color', 'font_family' anahtarlarına sahip sözlük

### live_line_chart
```python
pv.live_line_chart(data, title="Canlı Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='mavi')
```
Bir canlı çizgi grafiği oluşturur.

- **data**: Sayısal değerlerden oluşan liste
- **title**: Grafiğin başlığı (str)
- **xlabel**: X ekseni etiketi (str)
- **ylabel**: Y ekseni etiketi (str)
- **color**: Çizginin rengi (str)

### live_bar_chart
```python
pv.live_bar_chart(data, title="Canlı Bar Grafiği", xlabel="Kategori", ylabel="Değer", color='mavi')
```
Bir canlı bar grafiği oluşturur.

- **data**: Kategoriler anahtarlar ve sayısal değerler içeren sözlük
- **title**: Grafiğin başlığı (str)
- **xlabel**: X ekseni etiketi (str)
- **ylabel**: Y ekseni etiketi (str)
- **color**: Barların rengi (str)

### generate_report
```python
pv.generate_report(report_data, format='pdf', output_path='rapor.pdf')
```
Bir rapor oluşturur.

- **report_data**: Rapor detaylarını içeren sözlük
- **format**: Raporun formatı ('pdf', 'html') (str)
- **output_path**: Raporun kaydedileceği yol (str)

### basic_analysis
```python
pv.basic_analysis(data):
```
Veri üzerinde temel analiz yapar.

- **data**: Sayısal değerlerden oluşan liste

### advanced_analysis
```python
pv.advanced_analysis(data):
```
Veri üzerinde ileri düzey analiz yapar.

- **data**: Sayısal değerlerden oluşan liste
