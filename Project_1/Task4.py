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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
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

def UniqueTeleCaller(list_of_list):
    '''
    Function takes in a list of lists and outputs 
    number of distinct Telephone Numbers in the Data Set
    '''
    distinct_set =set()
    for record in list_of_list:
        distinct_set.add(record[0])
    return distinct_set


if __name__ == "__main__":
    outgoingCalls = set()
    incomingCalls = set()
    outgoingTexts = set()
    incomingTexts = set()

    for call in calls:
        outgoingCalls.add(call[0])
        incomingCalls.add(call[1])
    for text in texts:
        outgoingTexts.add(text[0])
        outgoingTexts.add(text[1])

    TeleMarketers = outgoingCalls.difference(incomingCalls)
    TeleMarketers = TeleMarketers.difference(outgoingTexts)
    TeleMarketers = TeleMarketers.difference(incomingTexts)
    TeleMarketers = sorted(list(TeleMarketers))
    print("These numbers could be telemarketers: ")
    for record in TeleMarketers:
        print(record)
