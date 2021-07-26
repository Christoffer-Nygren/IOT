from urllib import urequests
import ujson
import smtplib

# Class for sending notifications
class PhoneNotification:
    def sendNotification(temp, humidity):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        string_to_send = 'Temperature: {}C and Humidity: {}'.format(temp, humidity)
        account_sid = 'Twilio_SID'

        url = 'https://api.twilio.com/2010-04-01/Accounts/Twilio_SID/Messages.json'
        fromNum = 'from'
        toNum = 'to'

        payload = {
        'From': fromNum,
        'Body': string_to_send,
        'To': toNum
        }
        headers = {
        'Authorization': 'Basic urlEncodedKey',
        'Content-Type':'application/json',
        'Host':'api.twilio.com'
        }


        response = urequests.post(url, headers=headers, json=payload)


        print(response.text)
