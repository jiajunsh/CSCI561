#!/usr/bin/env python
# coding=utf-8

import os

os.system('mkdir -p results')

for i in xrange(85):
    os.system('cp ./cases/input{0}.txt ./input.txt'.format(i))
    os.system('./test_target > /dev/null')
    print("-->On test case #{0}<--".format(i))
    os.system('diff ./output.txt ./cases/output{0}.txt'.format(i))
    os.system('cp ./output.txt ./results/output{0}.txt'.format(i))

os.system('rm input.txt output.txt')
