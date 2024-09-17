#!/bin/bash

#echo "$0 - is the 0 arguement"
#echo "$1 - is the 1 arguemnet"
#echo "$2 - is the 2 arguement"

clear 

echo " ----------------------------"
echo "working .."
echo " ----------------------------"

echo "let me add up $1 and $2 for you"

SUM=$(( $1 + $2 ))

sleep 2

echo "The sum is $SUM" 
