import requests
from bs4 import BeautifulSoup

bot_token ='7819157836:AAG1nd9uCOVBuYArLDde5T7aivhn2DWJjrQ'
chat_id='6645558353'
def send_telegram(message):
    url=f'https://api.telegram.org/bot{'7819157836:AAG1nd9uCOVBuYArLDde5T7aivhn2DWJjrQ'}/sendMessage'
    payload={
    'chat_id': chat_id,
    'text':message
    }
    response= requests.post(url, data=payload)

    if response.status_code==200:
       print('message sent successfully')
    else:
       print('failed to send message:',response.text)
#webbb scraping

URL = "https://ipowatch.in/ipo-grey-market-premium-latest-ipo-gmp/"
headers={
    "User-Agent": "Mozilla/5.0"
}

response=requests.get(URL, headers=headers)

soup=BeautifulSoup(response.text,'lxml')
tables=soup.find_all("table")
ipo_data=[]
for table in tables:
    rows=table.find_all("tr")

    for row in rows[1:]:
        cols=row.find_all("td")

        if len(cols)>=7:
            ipo={
                "name":cols[0].get_text(strip=True),
                "gmp": cols[1].get_text(strip=True),
                "price":cols[2].get_text(strip=True),
                "gain":cols[3].get_text(strip=True),
                "date":cols[4].get_text(strip=True),
                "subject_to":cols[5].get_text(strip=True),
                "type":cols[6].get_text(strip=True)
            }
            
            ipo_data.append(ipo)
            # Clean gain and type
            gain_str = ipo["gain"].replace('%', '').replace('+', '').strip()
            try:
                gain_value = float(gain_str)
            except ValueError:
                print(f"⚠️ Skipping: {ipo['name']} - invalid gain: {ipo['gain']}")
                continue

            ipo_type = ipo["type"].strip().lower()

            # Debug print
            print(f"→ Checking: {ipo['name']}, Gain: {gain_value}%, Type: {ipo_type}")

            # Condition to trigger notification
            if gain_value >= 15 and ipo_type == "mainboard":
                message = (
                    f"🚨 IPO Alert!\n\n"
                    f"📌 {ipo['name']}\n"
                    f"💰 GMP: {ipo['gmp']}\n"
                    f"📈 Gain: {ipo['gain']}\n"
                    f"📆 Date: {ipo['date']}\n"
                    f"📦 Type: {ipo['type']}"
                )
                send_telegram(message)

