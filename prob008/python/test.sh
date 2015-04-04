#!/usr/bin/env bash

#input string passed into the test program.
echo '' > prob008.out
python prob008.py angel >> prob008.out
python prob008.py abmHAUSDad >> prob008.out
python prob008.py AaBbxXyYzZ >> prob008.out
python prob008.py CoMpuTer >> prob008.out
python prob008.py BaBiLonIa >> prob008.out
python prob008.py Zebra >> prob008.out
python prob008.py Coke >> prob008.out
python prob008.py Soda >> prob008.out

echo 'output of program:'
while read p; do
  echo $p
done <prob008.out





#echo 'output of program:'
#cat prob008.out
echo 'here is the diff with the solution (blank means correct): '
diff prob008.out answer>prob008.diff
cat prob008.diff
