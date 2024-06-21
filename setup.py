from setuptools import setup, find_packages

setup(
    name="pyVisio",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "plotly",
        "pandas",
        "numpy",
        "statsmodels"
    ],
    description="An interactive and dynamic data visualization and analysis library",
    author="Hüseyin Kaya",
    author_email="kaya87826@gmail.com",
    url="https://github.com/kayahuseyinn/pyVisio",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
