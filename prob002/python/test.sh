#!/usr/bin/env bash

#input string echo passed into the test program.
python prob002.py yolo trol > prob0001.out
echo 'here is the diff with the solution (blank means correct): '
diff prob0001.out answer
