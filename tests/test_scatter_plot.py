import pyVisio as pv
import pytest

def test_scatter_plot():
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 14, 12, 15, 10]
    try:
        pv.scatter_plot(x_data, y_data, title="Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", color='blue')
        assert True
    except Exception as e:
        assert False, f"test_scatter_plot failed: {e}"

def test_interactive_scatter_plot():
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 14, 12, 15, 10]
    try:
        pv.scatter_plot(x_data, y_data, title="Etkileşimli Dağılım Grafiği", xlabel="X Ekseni", ylabel="Y Ekseni", interactive=True, color='orange')
        assert True
    except Exception as e:
        assert False, f"test_interactive_scatter_plot failed: {e}"

if __name__ == "__main__":
    pytest.main()
