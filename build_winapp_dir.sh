#!/bin/sh

mkdir Procerfa
cp -r modules Procerfa/
find Procerfa/ | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
cp -r --parents data/pdf_models/ Procerfa/
cp run_app.py Procerfa/
