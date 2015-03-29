#!/usr/bin/env bash

#input string echo passed into the test program.
ruby prob003.rb prob003.input > prob003.out
echo 'output of program:'
cat prob003.out
echo 'here is the diff with the solution (blank means correct): '
diff prob003.out answer>prob003.diff
cat prob003.diff
