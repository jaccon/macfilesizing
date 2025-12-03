from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="macFileSizing",
    version="1.0.0",
    author="Jaccon",
    description="A Python script to list files and directories sorted by size",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaccon/macfilesizing",
    py_modules=["macFileSizing"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "tqdm>=4.0.0",
    ],
    entry_points={
        "console_scripts": [
            "macfilesizing=macFileSizing:main",
        ],
    },
)
