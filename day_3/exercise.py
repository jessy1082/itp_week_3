import requests
import json


#using the requests package, we can make API calls to retrieve JSON

response = requests.get("https://rickandmortyapi.com/api/character")

#print(response)
#print(response.text)

clean_data = json.loads(response.text)

print(clean_data)

# go through the results,
#for each row in an spreadsheet

for x in clean_data:
    print(x)
    if x == "results":
        for i in clean_data["results"]:
            print(i['name'])
            print(i['gender'])
            print(i['location'])

#print(i['name'] + ' : ' + i['species'])
            
import openpyxl

from openpyxl.workbook import Workbook
wb = Workbook()

ws1 = wb.create_sheet("Sheet_A")
ws1.title = "Title_A"
wb.save(filename = 'sample_book.xlsx')

