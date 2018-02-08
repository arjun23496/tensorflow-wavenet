import sys

string = sys.argv[1]

string = string.split('/')[-1].split('_')

index = string[0][1:]
count = string[1].split('.')[0]

print index," ",count
