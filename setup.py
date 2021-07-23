import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='parsingHLA',
    version='1.0.0',
    author="heeseung",
    author_email="1714855@sookmyung.ac.kr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/heeseungYoo/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)