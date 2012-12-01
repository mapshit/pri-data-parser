#!/bin/bash

parse.py "$1" csv | tr '\r' '\n' | sed -e 1d -e '$d'
