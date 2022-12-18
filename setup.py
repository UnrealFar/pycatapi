from setuptools import setup
import re

requirements = ["requests"]

version = ''
with open('pycatapi/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()


packages = [
    "pycatapi"
]

setup(name='PyCatApi',
    author='UnrealFar',
    url='https://github.com/UnrealFar/pycatapi/',
    version=version,
    packages=packages,
    license='MIT',
    description='A Python wrapper for TheCatApi',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8.0',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
      ]
)
