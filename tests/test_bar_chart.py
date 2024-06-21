import pyVisio as pv
import pytest

def test_bar_chart():
    data = {'A': 10, 'B': 20, 'C': 30}
    try:
        pv.bar_chart(data, title="Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", color='blue')
        assert True
    except Exception as e:
        assert False, f"test_bar_chart failed: {e}"

def test_interactive_bar_chart():
    data = {'A': 10, 'B': 20, 'C': 30}
    try:
        pv.bar_chart(data, title="Etkileşimli Çubuk Grafiği", xlabel="Kategori", ylabel="Değer", interactive=True, color='purple')
        assert True
    except Exception as e:
        assert False, f"test_interactive_bar_chart failed: {e}"

if __name__ == "__main__":
    pytest.main()
