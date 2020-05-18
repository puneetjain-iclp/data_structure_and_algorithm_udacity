"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def FindUniqueNumberofRecords(list_of_list):
    '''
    Function takes in a list of lists and outputs 
    number of distinct Telephone Numbers in the Data Set
    '''
    unique_dict = dict()
    for record in calls:
        if record[0] in unique_dict:
            unique_dict[record[0]] += int(record[3])
        else:
            unique_dict[record[0]] = int(record[3])
        if record[1] in unique_dict:
            unique_dict[record[1]] += int(record[3])
        else:
            unique_dict[record[1]] = int(record[3])
    return unique_dict

if __name__ == "__main__":
    DistinctTele = FindUniqueNumberofRecords(calls)
    maximum = max(DistinctTele, key=DistinctTele.get)
  
    print(" {0} spent the longest time, {1} seconds, on the phone during September 2016.".format(maximum,DistinctTele[maximum]))