from setuptools import setup, find_packages

setup(
    name="csv2json",
    version="0.1.0",
    description="A CLI tool to convert CSV files to JSON",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "csv2json=csv2json.cli:main",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
