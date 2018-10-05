#!/bin/sh
read name
echo "\c"
echo "$name this is a test"
echo `date`
echo `pwd` > result
#read a b c
#echo "a is $a\\$b\\$c"
read -p "passwd:" -n 6 -t 10 -s password
echo -e "pwd is $password"
