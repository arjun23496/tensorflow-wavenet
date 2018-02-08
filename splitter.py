import sys

string = sys.argv[1]

string = string.split('/')[-1].split('_')

index = string[1][1:]
count = string.split('.')[0]

print index," ",count