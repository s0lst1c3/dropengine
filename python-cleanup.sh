#!/bin/bash

find . -type f -name '*.pyc' -exec rm -f {} +
find . -type f -name '*.swp' -exec rm -f {} +
find . -type f -name '*.swo' -exec rm -f {} +
find . -type d -name '__pycache__' -exec rm -rf {} +
