#!/bin/bash
clear

message1="START"
echo $message1

cd /Users/brownscholar/Desktop/A2_Internship/InternshipGit/ocean-motion-2021/2-25

gfortran -O3 -o vectorq.exe vectorq.f
gfortran -O3 -o omegainv.exe omegainv.f

filename='/Users/brownscholar/Desktop/A2_Internship/InternshipGit/ocean-motion-2021/3-16/date_list.txt'
while read date; do 
	echo $date

	python3 writing-exec-file.py $date
	./vectorq.exec
	./omegainv.exec
done < $filename

message2="END"
echo $message2