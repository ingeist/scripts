#!/bin/bash


# let input be a string written in binary with spaces 
input=$1

if [[ $input = "-h" ]];
then
	printf "usage: ./binary.sh \"01101100 01100101 01110110 01100101 01101100 00100000 00110000 00100000\"\n";
	exit	
fi
IFS=' ' # delimate with spaces 
read -ra Arr <<< "$input" # read and save to Arr 

for i in ${Arr[@]}; do 
	printf "\x$(printf %x $(( 2#$i )))";
done
printf "\n"

