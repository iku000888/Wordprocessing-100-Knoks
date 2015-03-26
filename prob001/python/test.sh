#!/usr/bin/env bash

#input string echo passed into the test program.
echo 'stressed'|python prob001.py > prob0001.out
echo 'here is the diff with the solution (blank means correct): '
diff prob0001.out answer
