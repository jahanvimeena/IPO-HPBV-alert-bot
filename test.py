import requests

bot_token = '7819157836:AAG1nd9uCOVBuYArLDde5T7aivhn2DWJjrQ'
chat_id = '6645558353'

message = '🔔 Test alert from IPO bot!'
url = f'https://api.telegram.org/bot{'7819157836:AAG1nd9uCOVBuYArLDde5T7aivhn2DWJjrQ'}/sendMessage'
payload = {
    'chat_id': chat_id,
    'text': message
}
response = requests.post(url, data=payload)

print(response.status_code)
print(response.text)
