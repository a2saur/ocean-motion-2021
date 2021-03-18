#!/bin/bash

message="Hello! Starting Printing..."
echo $message


filename='/Users/brownscholar/Desktop/A2_Internship/InternshipGit/ocean-motion-2021/3-16/date_list.txt'
while read date; do 
    echo $date
done < $filename