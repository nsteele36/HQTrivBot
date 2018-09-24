#!/usr/bin/env python3
import fileinput

with fileinput.FileInput('logs.txt', inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('[soandso@MLSP3 HACKUTD]$ time python hqtrivsolver.py', '***TEST***'), end='')
