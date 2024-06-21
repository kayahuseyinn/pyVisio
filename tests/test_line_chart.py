import pyVisio as pv
import pytest

def test_line_chart():
    data = [1, 2, 3, 4, 5]
    try:
        pv.line_chart(data, title="Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='red')
        assert True
    except Exception as e:
        assert False, f"test_line_chart failed: {e}"

def test_interactive_line_chart():
    data = [1, 2, 3, 4, 5]
    try:
        pv.line_chart(data, title="Etkileşimli Çizgi Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", interactive=True, color='green')
        assert True
    except Exception as e:
        assert False, f"test_interactive_line_chart failed: {e}"

if __name__ == "__main__":
    pytest.main()
