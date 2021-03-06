from setuptools import setup

with open('README.md', 'r') as file:
     long_description = file.read()

setup(
    name='randomquotes',
    version='1.0',
    description='A package that generates quotes of life and smile ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['randomquotes'],
    package_dir={'': 'src'},
    classifiers=[

         "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=["random"],
    url="https://github.com/kaviyasobanbabu/randomquotes.git",
    author='kaviya P S, venkateswar.S',
    author_email='kaviyasobanbabu@gmail.com'
)
