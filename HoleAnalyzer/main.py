#!/usr/bin/env python3

from os import path
from src.HoleFinder import HoleAnalyzer
from typing import List, Dict

if __name__ == '__main__':
    data_path = path.join(path.dirname(__file__), 'data')
    h = HoleAnalyzer(data_path, 30)
    
    output_path = path.join(path.dirname(__file__), 'output')
    h.output_csv(path.join(output_path, 'output.csv'))
    h.output_json(path.join(output_path, 'output.json'))
    h.print_table()

