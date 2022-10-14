import requests
import json
import csv
import time

url = 'http://mockbin.org/bin/42e30578-743d-46c0-880b-12b67cfc1faa'

with open("body.json", "r") as read_file:
    my_body = json.load(read_file)

# header params
my_header = dict(
    account = 'acc_xyz',
    merchant = 'merch_abc'
)

with open('response.csv', mode='w', newline='', encoding='utf-8') as response_file:
    response_writer = csv.writer(response_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    response_writer.writerow(['limit_date', 'service_order_number', 'logistic_operator', 'provider', 'response_http_status'])

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1

            # manipulate json body
            my_body["terminal"]["id"] = row["id_meio_captura"]

            print(f'Sending request {line_count}:')

            post_response = requests.post(url=url, headers=my_header, json=my_body)
            response_status = post_response.status_code
            response = post_response.json()

            response_writer.writerow([response["limit_date"], response["service_order_number"], response["logistic_operator"], response["provider"], response_status])

            print(f'Response {line_count}: {response}')
            print(f'Status code: {response_status}')

            line_count += 1
            time.sleep(1)

    print(f'Processed {line_count} lines.')


