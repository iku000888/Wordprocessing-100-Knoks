#!/usr/bin/env bash

#input string passed into the test program.
python prob009.py input.txt > prob009.out
echo 'output of program:'
cat prob009.out
#echo 'here is the diff with the solution (blank means correct): '
#diff prob007.out answer>prob007.diff
#cat prob007.diff
