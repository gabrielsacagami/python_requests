import requests
import json
import csv
import time
import requestsResources as rsource

URL = 'http://mockbin.org/bin/42e30578-743d-46c0-880b-12b67cfc1faa'

with open("tokens.json", "r") as read_token:
    my_tokens = json.load(read_token)
    logistic_token = my_tokens["logistic_token"]

my_header = dict(
    token = logistic_token
)

with open("body.json", "r") as read_file:
    my_body = json.load(read_file)

with open('response.csv', mode='w', newline='', encoding='utf-8') as response_file:
    response_writer = csv.writer(response_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            rsource.change_body(my_body, row)
            rsource.print_line_to_process(row)
            rsource.print_send_request(line_count)

            post_response = requests.post(url=URL, headers=my_header, json=my_body)
            response_status, responsej = rsource.process_responses(post_response)

            if line_count == 0:
                header = list(responsej.keys())
                response_writer.writerow([*header, 'response_http_status', 'request_number','id_meio_captura'])
                line_count += 1

            response_headers = responsej.keys()
            responsel = list(responsej.values())

            response_writer.writerow([*responsel, response_status, f'Request {line_count}', my_body["terminal"]["id"]])
            rsource.print_result(line_count, response_status, responsej)

            line_count += 1
            time.sleep(1)
        rsource.process_result(line_count - 1)
