#!usr/bin/env bash
echo ' '
echo 'List of IP addresses within your network: '
echo ' '
#in sequence of 1 thru 254 we use 'do' to perform ping
for ip in `seq 1 254`; do

#$1 asks for user input which should be an IP address
ping -c 1 $1.$ip | grep '64 bytes' | cut -d " " -f 4 | tr -d ':' &
done

