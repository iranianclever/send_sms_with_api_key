import requests

# api key
api_key = ''
# url from web service
api_url = f'https://api.kavenegar.com/v1/{api_key}/sms/send.json'

message = 'Hello ali'

payload = {
    'receptor': '09911122714',
    'message': message
}
# send message
response = requests.post(api_url, data=payload)
# check message correctly
if response.status_code == 200:
    print(f'ارسال شد | کد وضعیت : {response.status_code}')
else:
    print(f'ارسال نشده | کد وضعیت : {response.status_code}')
