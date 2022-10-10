import requests

echo_get = 'https://postman-echo.com/get'
echo_post = 'https://postman-echo.com/post'

var1 = 'bar3'

my_header = dict(
    account = 'acc_xyz',
    merchant = 'merch_abc'
)

my_query_string = dict(
    foo1='bar1',
    foo2=var1
)

response = requests.get(url=echo_get, params=my_query_string, headers=my_header)

response_status = f'Response Status: {response.status_code}'

data = response.json()

print(data)
print(response_status)