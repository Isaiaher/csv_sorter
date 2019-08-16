import csv
import operator

outputFile = open('final_output.csv', 'r')

output = csv.reader(outputFile, delimiter=',')

file = open('durmas_output.csv', 'w')

for eachline in output:
    print >>file, ', '.join(eachline)[:-3]

file.close()
