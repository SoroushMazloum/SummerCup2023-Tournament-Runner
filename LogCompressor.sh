#!/bin/bash

for file in ./*.rcg; do
    if [ -f "$file" ]; then
	tar czvfp "${file}.tar.gz" "$file"
	rm "$file"
    fi
done

for file in ./*.rcl; do
    if [ -f "$file" ]; then
        tar czvfp "${file}.tar.gz" "$file"
	rm "$file"
    fi
done
