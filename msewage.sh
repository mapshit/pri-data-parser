#!/bin/sh

parse.py "$1" msewage > "$1".json
echo msewage-importer -Topen_defecation_site "$1".json
