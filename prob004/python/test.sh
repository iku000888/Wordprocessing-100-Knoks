#!/usr/bin/env bash

#input string echo passed into the test program.
python prob004.py prob004.input > prob004.out
echo 'output of program:'
cat prob004.out
echo 'here is the diff with the solution (blank means correct): '
diff prob004.out answer>prob004.diff
cat prob004.diff
