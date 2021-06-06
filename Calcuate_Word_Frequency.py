#!usr/bin/python3


import argparse
from collections import defaultdict
import collections


parser = argparse.ArgumentParser(usage="python3 Calculate_Frequency.py [-h] input_file.\n This program calculate the frequency of the words in the file", description="")
parser.add_argument('input_file',type =str, help='Enter the filename')
args = parser.parse_args()
input_file = args.input_file

Words_Dictionary={}
with open(input_file,'r') as fh:
    content = fh.readlines()
for every_line in content:
    list_words=every_line.split(" ")
    for every_word in list_words:
        if every_word in Words_Dictionary:
            Words_Dictionary[every_word]+=1
        else:
            Words_Dictionary[every_word]=1


#sorted_dict = collections.OrderedDict(Words_Dictionary)

with open("frequency_file","w") as fh:
    {print(k,v,file=fh) for k, v in sorted(Words_Dictionary.items(), key=lambda item: item[1], reverse=True)}
