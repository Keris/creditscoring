#!/bin/bash
echo "Cleaning build and dist..."
rm -rf build dist
echo "Packaging..."
python setup.py sdist bdist_wheel
echo "Uploading to pypi using twine..."
twine upload --repository pypi dist/*
