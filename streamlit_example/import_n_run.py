# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 19:10:36 2023

@author: Bruger
"""

import subprocess

# List of packages to install
packages = ['streamlit', 'pandas', 'plotly']

# Install packages using pip
for package in packages:
    subprocess.check_call(['pip', 'install', package])

# Construct the subprocess command
subprocess_cmd = ['streamlit', 'run', "streamlit_example.py"]

# Call the subprocess
subprocess.check_call(subprocess_cmd)