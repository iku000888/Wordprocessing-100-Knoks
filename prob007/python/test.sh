#!/usr/bin/env bash

#input string passed into the test program.
python prob007.py 12 気温 22.4 > prob007.out
echo 'output of program:'
cat prob007.out
echo 'here is the diff with the solution (blank means correct): '
diff prob007.out answer>prob007.diff
cat prob007.diff
