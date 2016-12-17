import requests
import json
from mtranslate import translate

sehir=raw_input("Sehir :")
url="http://api.apixu.com/v1/current.json?key=aba6dbd30810434ca8e210850161612&q="+sehir.capitalize()

response=requests.get(url)

response=json.loads(response.content)

havaDurumu=translate(str(response["current"]["condition"]["text"]),"tr").encode("utf-8")
derece=str(response["current"]["temp_c"])
hissedilen=str(response["current"]["feelslike_c"])
saat=str(response["location"]["localtime"])
saat = saat.replace("-",".")
saat = saat.replace(" "," ,  ")
from twilio.rest import TwilioRestClient

sonuc="""
Sehir : {Sehir}
Hava : {Hava_durum}
Derece : {Derece}
Hissedilen Derece : {His_derece}
Gun,Saat : {GunSaat}
"""

ACCOUNT_SID = "//"
AUTH_TOKEN = "//"
sonuc = sonuc.format(Sehir=sehir.capitalize(),Hava_durum=havaDurumu,Derece=derece,His_derece=hissedilen,GunSaat=saat)

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(to="Number",
                                   from_="Number",
                                   body=sonuc)