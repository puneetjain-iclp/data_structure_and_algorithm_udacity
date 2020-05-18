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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def GetAllAreaCodes(calls):
  '''
  Returns all the Area Codes in the form of list of Strings
  Returns the total number of calls from land line to land line
  Returns the total numner of calls from from landline
  '''
  tele = set()
  num = 0
  tot = 0
  for records in calls:
    if records[0].startswith('(080)'):
      if records[1].startswith('('):
        tele.add((records[1][1:].split(")")[0]))
      elif records[1][0] in ['9','8','7']:
        tele.add((records[1].split(" ")[0][:4]))
      if  records[1].startswith('(080)'):
        num += 1
      tot +=1
  tele.add('140')
  return tele,num,tot

if __name__ == "__main__":
  tele , TotalLandlineCalls , TotalLineCalls = GetAllAreaCodes(calls)
  print("The numbers called by people in Bangalore have codes:")
  print(*sorted(set(tele)),sep='\n')

  tot =0
  num=0
  for records in calls:
    if records[0].startswith('(080)'):
      if  records[1].startswith('(080)'):
        num += 1
      tot +=1

  print('{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(TotalLandlineCalls/TotalLineCalls*100))
