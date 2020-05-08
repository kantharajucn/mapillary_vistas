import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vistas_eval",
    version="0.1.0",
    author="",
    author_email="",
    description="Mapillary Vistas Evaluation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kantharajucn/mapillary_vistas",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy == 1.18.1',
        'tqdm == 4.43.0',
        'scikit-learn == 0.22.2',
        'pillow == 7.0.0',
        'matplotlib == 3.2.0',
        'scipy == 1.4.1'
      ],
      include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT",
        "Operating System :: Linux",
    ],
)