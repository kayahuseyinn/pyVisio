from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "docs" / "pypi.md").read_text()

setup(
    name='pyVisio',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'plotly',
        'pandas',
        'numpy',
        'statsmodels',
        'jinja2',
        'reportlab',
        'fpdf2'
    ],
    author='Hüseyin Kaya',
    author_email='kaya87826@gmail.com',
    description='Interactive and dynamic data visualization library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kayahuseyinn/pyVisio',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
