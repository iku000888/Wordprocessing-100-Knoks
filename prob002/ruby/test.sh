#!/usr/bin/env bash

#input string echo passed into the test program.
ruby prob002.rb yolo trol > prob002.out
echo 'run:ruby prob002.rb yolo trol'
echo 'test output'
cat prob002.out
echo 'here is the diff with the solution (blank means correct): '
diff prob002.out answer > prob002_answer.diff
cat prob002_answer.diff
 
