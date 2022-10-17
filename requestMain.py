import requests
import json
import csv
import time

URL = 'http://mockbin.org/bin/42e30578-743d-46c0-880b-12b67cfc1faa'

my_header = dict(
    account = 'acc_xyz',
    merchant = 'merch_abc'
)

def change_body(my_body, row):
    my_body["terminal"]["id"] = row["id_meio_captura"]

def print_line_to_process(row):
    print(f'Line to process: {row}')

def print_result(line_count, response_status, response):
    print(f'Response {line_count}: {response}')
    print(f'Status code: {response_status}')

def request_p_status(line_count):
    print(f'Sending request {line_count}:')

def process_result(line_count):
    if line_count == 1:
        print(f'Processed {line_count} line of data.')
    else:
        print(f'Processed {line_count} lines of data.')

def responses_p(post_response):
    response_status = post_response.status_code
    responsej = post_response.json()
    return response_status,responsej

with open("body.json", "r") as read_file:
    my_body = json.load(read_file)


with open('response.csv', mode='w', newline='', encoding='utf-8') as response_file:
    response_writer = csv.writer(response_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    response_writer.writerow(['limit_date', 'service_order_number', 'logistic_operator', 'provider', 'response_http_status'])

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            print_line_to_process(row)
            change_body(my_body, row)
            request_p_status(line_count)

            post_response = requests.post(url=URL, headers=my_header, json=my_body)
            response_status, responsej = responses_p(post_response)

            response_writer.writerow([responsej["limit_date"], responsej["service_order_number"], responsej["logistic_operator"], responsej["provider"], response_status])
            print_result(line_count, response_status, responsej)

            line_count += 1
            time.sleep(1)
        process_result(line_count - 1)


