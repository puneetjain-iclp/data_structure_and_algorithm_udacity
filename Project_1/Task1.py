"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def FindUniqueNumberofRecords(list_of_list):
    '''
    Function takes in a list of lists and outputs 
    number of distinct Telephone Numbers in the Data Set
    '''
    distinct_set =set()
    for record in list_of_list:
        distinct_set.add(record[0])
        distinct_set.add(record[1])
    return distinct_set

if __name__ == "__main__":
    #The Function FindUniqueNumberofRecords has O(N) Time complexity
    UniqueTextNumbers = FindUniqueNumberofRecords(texts)
    UniqueCallNumbers = FindUniqueNumberofRecords(calls)
    #The update attribute for set also has O(N) Time Complexity
    UniqueTextNumbers.update(UniqueCallNumbers)
    #The update Function also has O(1) Time Complexity
    DistinctCalls = len(UniqueTextNumbers)
    print("There are {} different telephone numbers in the records.".format(DistinctCalls))