#!/usr/bin/python3

for j in range(100):
    print("{:02d}".format(j) if j < 10 else "{:d}".format(j),
          end=", " if j < 99 else "\n")
