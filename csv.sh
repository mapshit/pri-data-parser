#!/bin/sh

parse.py "$1" csv > "$1".csv | sed -e 's/\r/\r\n/' -e 1d
