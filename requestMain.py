import requests
import json
import csv
import time

url = 'https://postman-echo.com/post'

with open("body.json", "r") as read_file:
    my_body = json.load(read_file)

# header params
my_header = dict(
    account = 'acc_xyz',
    merchant = 'merch_abc'
)

with open('response.csv', mode='w') as response_file:
    response_writer = csv.writer(response_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    response_writer.writerow(['cep', 'id_meio_captura', 'status'])

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            # manipulate json body
            my_body["cep"] = row["cep"]
            my_body["id_meio_captura"] = row["id_meio_captura"]

            post_response = requests.post(url=url, headers=my_header, json=my_body)
            response_status = f'Response Status: {post_response.status_code}'
            response = post_response.json()

            response_writer.writerow([row["cep"], row["id_meio_captura"], response_status])

            print(response)
            print(response_status)

            line_count += 1
            time.sleep(1)

    print(f'Processed {line_count} lines.')


