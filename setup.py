from ast import literal_eval
import os
from setuptools import setup, find_packages

requirements = [
    'cookiecutter>=1.0.0',
]
constants = os.path.join('coverpage', 'constants.py')
with open(constants) as f:
    for line in f.readlines():
        if line.startswith('TEMPLATE_ROOT'):
            TEMPLATE_ROOT = literal_eval(line.split('=')[1])
            TEMPLATE_ROOT = os.path.expanduser(TEMPLATE_ROOT)
        if line.startswith('TEMPLATE_DIR'):
            TEMPLATE_DIR = eval(line.split('=')[1])
data_files = []
template_name = os.path.basename(TEMPLATE_DIR)
for root, _, filenames in os.walk(template_name):
    data_files.append( (
            os.path.join(TEMPLATE_ROOT, root),
            [os.path.join(root, f) for f in filenames]
    ) )
setup(
    name='coverpage',
    version='0.1.0',
    author='Selim Belhaouane',
    entry_points={
        'console_scripts': [
            'coverpage = coverpage.__main__:main'
        ]
    },
    install_requires=requirements,
    data_files=data_files,
    packages=find_packages(),
)
