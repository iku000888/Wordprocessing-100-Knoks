#!/usr/bin/env bash

#input string echo passed into the test program.
python prob002.py yolo trol > prob002.out
echo 'output of program:'
cat prob002.out
echo 'here is the diff with the solution (blank means correct): '
diff prob002.out answer>prob002.diff
cat prob002.diff
