import setuptools

setuptools.setup(
    name="onadata",
    version="0.1",
    url="https://github.com/keithmcnulty/onadata-python",
    author="Keith McNulty",
    author_email="keith.mcnulty@gmail.com",
    description="Allows data access from the book - Handbook of Graphs and Networks in People Analytics.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
)
