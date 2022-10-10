import requests
import json

echo_get = 'https://postman-echo.com/get'
echo_post = 'https://postman-echo.com/post'

with open("body.json", "r") as read_file:
    my_body = json.load(read_file)

print(my_body["address"]["line1"])
my_body["param_2"] = 'new_var_2'
my_body["address"]["line1"] = 'New Street'

my_header = dict(
    account = 'acc_xyz',
    merchant = 'merch_abc'
) 

my_query_string = dict(
    foo1='bar1'
)

# get_response = requests.get(url=echo_get, params=my_query_string, headers=my_header)

post_response = requests.post(url=echo_post, params=my_query_string, headers=my_header, json=my_body)

response_status = f'Response Status: {post_response.status_code}'
response = post_response.json()

print(response)
print(response_status)