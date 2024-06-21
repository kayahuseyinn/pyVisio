import pyVisio as pv
import pytest

def test_pie_chart():
    data_pie = {'Elma': 50, 'Armut': 30, 'Kiraz': 20}
    try:
        pv.pie_chart(data_pie, title="Pasta Grafiği")
        assert True
    except Exception as e:
        assert False, f"test_pie_chart failed: {e}"

def test_interactive_pie_chart():
    data_pie = {'Elma': 50, 'Armut': 30, 'Kiraz': 20}
    try:
        pv.pie_chart(data_pie, title="Etkileşimli Pasta Grafiği", interactive=True)
        assert True
    except Exception as e:
        assert False, f"test_interactive_pie_chart failed: {e}"

if __name__ == "__main__":
    pytest.main()
