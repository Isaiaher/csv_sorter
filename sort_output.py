import csv
import operator

outputFile = open('Outputs3/all_outputs.csv', 'r')

output = csv.reader(outputFile, delimiter=',')

sort = sorted(output, key = operator.itemgetter(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

file = open('sorted_ouput.csv', 'w')

for eachline in sort:
    print >>file, ', '.join(eachline)

file.close()