#!/usr/bin/env bash

#input string echo passed into the test program.
python prob006.py paraparaparadise paragraph se > prob006.out
echo 'output of program:'
cat prob006.out
echo 'here is the diff with the solution (blank means correct): '
diff prob006.out answer>prob006.diff
cat prob006.diff
