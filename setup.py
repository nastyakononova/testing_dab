from setuptools import setup, find_packages


setup(
    name="books_databricks",  # Replace with your package name
    version="0.1.0",
    author="nastyakononovaa76@gmail.com",
    url='https://databricks.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
     entry_points={
    'group_1': 'run=books_databricks.main:main'
    },
    install_requires=[
        'setuptools'
    ],
    python_requires=">=3.6",
)