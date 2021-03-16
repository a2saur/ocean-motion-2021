#!/bin/bash

cd /Users/brownscholar/Desktop/A2_Internship/InternshipGit/ocean-motion-2021/2-25

python3 writing-exec-file.py 940518

gfortran -O3 -o vectorq.exe vectorq.f
gfortran -O3 -o omegainv.exe omegainv.f

./vectorq.exec
./omegainv.exec