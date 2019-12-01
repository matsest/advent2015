#!/usr/bin/env Python

import ast

memory_count = 0
raw_count = 0

with open("input.txt",'r') as f:
    for line in f:
        raw = line.strip() # strips leading and trailing " and whitespace
        parsed = ast.literal_eval(raw) # parses as ascii
        print parsed

        raw_count += len(raw)
        memory_count += len(parsed)

print(raw_count - memory_count)

#must run in terminal - sublime does not like ascii
#note that you changed output encoding to ascii in iTerm for this to print correctly