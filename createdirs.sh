echo 'creating python and ruby sub directories for:'$1
mkdir -p $1
mkdir -p $1/python
mkdir -p $1/ruby
echo 'problem statement for '$1> $1/probstatement$1.txt
echo $2>> $1/probstatement$1.txt
