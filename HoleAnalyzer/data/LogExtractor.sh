#!/bin/bash

for file in ./*.tar.gz; do
    if [ -f "$file" ]; then
	tar xvf "$file"
	rm "$file"
    fi
done
