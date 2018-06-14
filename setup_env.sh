#!/bin/sh
mkdir dependencies/ext_script
mv dependencies/make_cli_script_file.py dependencies/ext_script/.
touch dependencies/ext_script/__init__.py
git clone git@github.com:knan02/scripts.git
#touch __init__.py

