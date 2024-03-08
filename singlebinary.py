# coding: utf-8
from setuptools import setup
import os
import toml

pyproject = {}
if os.path.exists('pyproject.toml'):
    pyproject = toml.load('pyproject.toml')

def get_entry_points():
    entry_points = []
    for script_name, script_spec in pyproject.get('tool', {}).get('poetry', {}).get('scripts', {}).items():
        entry_points.append(f'{script_name}={script_spec}')
    return entry_points
def get_version():
    return pyproject.get('tool', {}).get('poetry', {}).get('version', '0.1.0')

setup(
    name="eve",
    version=get_version(),
    packages=['eve'],
    entry_points={
        'console_scripts': get_entry_points(),
    },
)