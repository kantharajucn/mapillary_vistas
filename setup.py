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
        'numpy >= 1.16',
        'tqdm',
        'scikit-learn',
        'pillow ',
        'matplotlib',
        'scipy'
      ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['vistasEvaluate=mapillary_vistas.tools.evaluation:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT",
        "Operating System :: Linux",
    ],
)