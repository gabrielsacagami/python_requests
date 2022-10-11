import requests
import json
import csv

url = 'https://postman-echo.com/post'

with open("body.json", "r") as read_file:
    my_body = json.load(read_file)

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[4])
            print(row[1])
            print(row[8])
            line_count += 1
    print(f'Processed {line_count} lines.')

# header params
my_header = dict(
    account = 'acc_xyz',
    merchant = 'merch_abc'
) 

# manipulate json body
my_body["criadaPor"] = 'python_runner'
my_body["terminal"]["id"] = 'NOVO_ID'

post_response = requests.post(url=url, headers=my_header, json=my_body)
response_status = f'Response Status: {post_response.status_code}'
response = post_response.json()

print(response)
print(response_status)