#!/usr/bin/env bash

#input string echo passed into the test program.
python prob005.py prob005.input > prob005.out
echo 'output of program:'
cat prob005.out
echo 'here is the diff with the solution (blank means correct): '
diff prob005.out answer>prob005.diff
cat prob005.diff
