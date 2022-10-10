import requests
import json

url = 'https://postman-echo.com/post'

with open("body.json", "r") as read_file:
    my_body = json.load(read_file)

# header params
my_header = dict(
    account = 'acc_xyz',
    merchant = 'merch_abc'
) 

# manipulate json body
my_body["param_2"] = 'new_var_2'
my_body["address"]["line1"] = 'New Street'

post_response = requests.post(url=url, headers=my_header, json=my_body)
response_status = f'Response Status: {post_response.status_code}'
response = post_response.json()

print(response)
print(response_status)