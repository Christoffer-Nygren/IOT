# Tutorial on how to build a temperature and humidity sensor with push notifications.
***Christoffer Nygren - cn222tm***

This project will be focused on creating a system that measures the temperature and humidity of my apartment as well as having a function where the button is pressed a notification is sent to my phone with the current temperature and humidity.

The complexity of this project is not very high but has some difficulties such as getting the notifications to work but it should be able to be done within 20 hours of work. When following this tutorial it should not take longer than a few hours since all the hard work is already done.

## Objective
The reason to why I have chosen this project is because in the recent weeks we have hade very high temperatures in my city and even higher in my apartment to a point where I can barely stand being inside of the apartment. 

This got me thinking of starting to measure the temperature of my apartment to get a better understanding of the situation and with the measurements from the sensor I can start doing some smaller experiments to see how best i can battle this heat, such as with a dehumidifier, better fan, air cooler etc...

## Material
Listed below are all the materials needed for following this project.

| Material  | Price    | Description |
| ---------| ---------| ---------|
| DHT11    | [49kr](https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/)    | This sensor is used to measure both the humidity and temperature of the area which it is located in. Also included in the bundle with button.|
|Push Button| [299kr](https://www.electrokit.com/en/product/sensor-kit-26-modules/)| This sensor is self-explanatory it is used as a button and when pressed it sends a 0 otherwise a 1.|
|Pycom LoPy 4|[949kr](https://www.electrokit.com/en/product/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/)|This is a device programmed by MicroPython which has multiple bands of connectivity, it has many digital and analog inputs/outputs which makes it perfect for this project.|
|Pycom expansion board|Included above package|It is with help of this expansion board we can make use of all the features the LoPy 4 has to offer, this board. [Docs for board](https://docs.pycom.io/datasheets/expansionboards/expansion3/)|
|Wires| Included in packages|Wires that connect the different sensors together with help of the breadboard.|
|Breadboard| Included above package|An extension to the boards that help connect wires together with the sensors and helps with organizing and connecting multiple sensors to the same electrical outlet/ground.|

Shown below are a picture of all the materials


| Picture | Description |
| -------- | -------- |
| ![](https://i.imgur.com/JnMLLRf.jpg)     | Part 1, Breadboard, this is what is used for connecting all the sensors through wires ot the lopy.   |
| ![](https://i.imgur.com/mZCMk3D.jpg)     | Part 2, Push button, this sensor sends a analog signal 1 or 0 if it is being sent or not and is used for notifications.   |
| ![](https://i.imgur.com/JTE9Q7f.jpg)     | Part 3, DHT11, this sensor is being used for measuring both the humidity and temperature of the area it is being located within.     |
| ![](https://i.imgur.com/0QSwahy.jpg)     | Part 4, LoPy + Extension board, this is the computer itself processing all the information from the sensors and sending it to pybytes.    |


## Computer Setup

For this project I have chosen to use the Atom IDE created by github. To get started with Atom you will need to head over to [Atom website](https://atom.io) and press download. After that just follow the instructions to install it on your computer. 

Once that is done you will be promped with a welcome page which is where we will first need to press on "Install a Package". Then search for "pymakr" which will be the package used for connecting to the LoPy 4. Next step is to create our project folder to prepare the code.

We then need to update the firmware on the LoPy before we start coding and this can be done with help of pybytes a website for managing pycom devices. So head over to [pybytes website](https:pybytes.pycom.io//) and sign in/  sign up. Then when signed in press the `Add Device` button then `Add via USB` select the LoPy 4 and then `manage wifi` and type in your wifi credentials, the name + the password for your wifi(This will be important later when connecting the LoPy to the web). Decide a name for your project and press save! Now we will need to upload the firmware update to the device, download it and follow it until it says you have to type in a token, go back to the website and then to the `Offline Firmware Updater` copy the token and continue.

For future needs of this project we will also be needing Node.js installed on the computer which is a package manager for installing different javascript packages which will be needed later for the notifications to work properly. Head over to the [Node.js website](https://nodejs.org/en/) and follow the download instructions then to confirm it is installed open up a terminal and write `node --version` if it responds with a version you have properly installed node.js.

For the javascript part, these packages are also required `Emmet` and `Emmet-jsx-props` which are essential tools for web developing and the second is specifically for javascript. The express server can be found on this link [IOTWebserver](https://github.com/Christoffer-Nygren/IOTWebserver). When getting the express server later all that has to be done within the folder is open console and in folder write `npm i` which will install all neccessary libraries.

There is also a requirement to sign up an account on [Twilio](https://twilio.com) and follow the sign up instruction there to setup a phone service for the future of this project, otherwise phone notifications will not be possible to send.

To upload code onto the LoPy we need to first connect it to the computer via USB to microUSB and once its connected the lamp on top of it should start glowing, then to upload written code onto it simply press the upload button on the bottom of Atom and then wait. If errors occur it might be because code is already running on the LoPy and if that is the case just press `Ctrl + C` to stop it then try again.

## Putting everything Together
Seen below we have how the DHT11 sensor is connected and the pushbutton can be connected in the exact same way which will be shown in Figure 1. Because of how I got these sensors there was no worries about resistors and the input is done with voltage and current where DHT11 has a current input and the push button has a voltage input of either 1 or 0 where 0 is on and 1 is off for some reason. The way this is constructed supposedly it could be put in production since it is not a very complicated set up.

Both the sensors need 3v3 outlet from the lopy and can be connected to the same ground the only difference in wires is that they have to be connected to 2 different pins and the ones I have chosen are 16(Button) and 23(DHT11). The red wire is the electricity out as 3v, the white is the ground outlet for the sensors and the blue is the input/output signals.

![](https://i.imgur.com/a9A4wD7.jpg)

>Figure 1, circuit diagram.

## Platform

For this project pybytes is to be used as a platform of communication between the device and the internet, which also is a free platform but it has limits such as data gets removed when they get 1 month old. So if you want data to stay under longer periods of time it can be wise to setup a database of some sort connected to a webserver hosting the statistical data either locally or on the cloud, which in my case is not needed since I am not that interested in long term data. 

With help of pybtes it is easily possible to see different signals data in diagrams to be displayed and viewed upon. With help of pybytes it is also easy to setup a webhook which is a "tool" used to update data on other places like the small webserver that is needed in this project to send the notifications, so everytime an update is sent to pybytes; pybytes then sends that update to my webserver which can send the information to an api sending the information to a sms on my phone.

The other platform in use is [Twilio](https://twilio.com) which is a paid service for phone notifications of sorts, but for this project I only signed up for a trial account which lets me have around 250 notifications sent total from a cheap number chosen.
## The Code
### LoPy
#### Boot.py
The most important file is the `boot.py` as seen in "Code 1", with help of the name this will be automatically run first when uploading the code to the LoPy and in here what we do is that we connect the LoPy to the chosen WiFi(Same as the one we chose on the pybytes website). The code checks through all available wifis and if it finds the one we have told it to look for it connects to it and messages that 
it was succesful then moves on to `main.py`.

```python=
from network import WLAN
import machine
import main
from lib import key
wlan = WLAN(mode=WLAN.STA)

#Connects the lopy to the wifi
nets = wlan.scan()
for net in nets:
    if net.ssid == key.ssid:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, key.ssid_pass), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        print(wlan.ifconfig())
        break

machine.main(main)
```
>Code 1, boot.py

#### Main.py
The first thing we will look on in `main.py` is the pins we have connected for the sensors, so p_in is the push button and th is the DHT11 sensor for humidity and temperature. For the DHT11 to work we need to set the mode to OPEN_DRAIN which means it can be used for both input and outputs while Pin.IN only allows for input values.

```python=

p_in = Pin('P16', mode=Pin.IN)
th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)

#Checks the sensors and returns data
```
>Code 2, main.py Pins

Next to look at in `main.py` is the main function of the file that makes everything run. here we start with an endless loop that sets the value the pushbutton as well as checks the current seconds alive. The first if statement checks if 10 minutes has passed and if it has it will then get the sensor information (Explained later) and sends them to pybytes using 2 different signals then prints it has been done succesfully. The last part is that it puts itself to sleep for 1 second otherwise these signals would be sent multiple times within the second that it has been 10 minutes, this ensures it is being sent only 1 time.
```python=
def run():
   while(1):
      value = p_in.value()
      t = time.time()
      if t % 600 == 0:  # Checks if 10 minutes has passed for updates
          sensors = getSensorInfo()
          pybytes.send_signal(2, sensors[0])
          pybytes.send_signal(3, sensors[1])
          print('Sent auto temp successfully!')
          time.sleep(1)
      if value == 0:  # Checks if button has been pressed
         sensors = getSensorInfo()
         result_string = "Temperature: {}°C and Humidity: {}%".format(
             sensors[0], sensors[1])
         pybytes.send_signal(1, result_string)
         print('Sending {}'.format(result_string))
         pycom.rgbled(0x220000)
         time.sleep(1)
      else:
         pycom.rgbled(0x000022)
         time.sleep(1)


run()

```
>Code 3, main.py run()

This little function reads the data of the DHT11 sensor and divides it into an array with both the temperature and humidity to then be returned to `run()`. For this to work we need to add [this library](https://) to the lib folder and import it in main.py, this is the library that holds all the code for the sensor to work.
```python=
def getSensorInfo():
   result = th.read()
   while not result.is_valid():
      time.sleep(.5)
      result = th.read()
   sensors = [result.temperature, result.humidity]
   return sensors

```
>Code 4, main.py getSensorInfo()

The last file of `main.py` is a class that I made to make http post calls to the twilio api for phone notifications and for this to work a library named `urequests.py` is needed which in my case was not working properly, `GET` calls work but `POST` calls do not seem to work properly which is why I had to come up with a different solution explained below. What happened for me is that the post call could not properly format the payload and kept sending it all as a string within "" instead of a json object as {}. 
```python=
from urllib import urequests
import ujson

# Class for sending notifications
class PhoneNotification:
    def sendNotification(temp, humidity):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        string_to_send = 'Temperature: {}C and Humidity: {}'.format(temp, humidity)
        account_sid = 'Sid'

        url = 'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
        fromNum = 'fromNumTwilio'
        toNum = 'toNumTwilio'

        payload = {
        'From': fromNum,
        'Body': string_to_send,
        'To': toNum
        }
       
        readyLoad = ujson.dumps(payload)
        headers = {
        'Authorization': 'Basic urlencodedAuth',
        'Content-Type':'application/json',
        'Host':'api.twilio.com'
        }


        response = urequests.post(url, headers=headers, json=payload)


        print(response.text)

```
>Code 5, phone.py (Optional)

### Express.js
To fix the problem I had with http calls not working on the LoPy I decided to set up my own Express.js server to take webhook calls from pybytes and forward them to twilio to be able to have it sent as a notification to my phone. 

Below is the main part of the express server which succesfully makes a http POST call to the twilio api which is a api that can send phone notifications. When a webhook update is sent from pybytes it gets forwarded with the message to this function if it is the right signal, then it is pushed into the body of the message that is going to be sent to the api. It then sends the POST and if it catches any errors it is printed in the console.

```javascript=
async function sendNotification(stringToSend)  {
  let data = await new FormData();
  data.append('To', process.env.TWILIO_TO);
  data.append('From', process.env.TWILIO_FROM);
  data.append('Body', stringToSend);

  let config = {
    method: 'post',
    url: process.env.TWILIO_URL,
    headers: {
      'Authorization': 'Basic ' + process.env.TWILIO_AUTH_TOKEN,
      ...data.getHeaders()
    },
    data : data
  };

  await axios(config)
  .then(function (response) {
    console.log(JSON.stringify(response.data));
    return response
  })
  .catch(function (error) {
    console.log(error);
  });

}

```
>Code 6, notification function of the express server.

Last part of the code is what catches the webhook from pybytes and makes sure that the webhook has the right signal to be sent further away, would not want the 10 minute auto updates to be sent to my phone.

```javascript=
app.post('/test', async (req, res) => {
  console.log(req.body);
  let signal = req.body.signal
  signal == 1 ? await sendNotification(req.body.payload) : console.log('Wrong notification');//Checks if signal is right

  res.send('Notification sent')
})
```
>Code 7, catches the webhook.
## Transmitting the data / connectivity
With help of WiFi protocol data is being sent every 10 minutes with 2 different signals, 1 signal for the temperature and the second signal for the humidity to the pybytes website to be displayed. When pressing the button a third signal is also sent containing both the temperature and humidity to then with help of the webhook gets transferred to a express js server that sends a http post call to the twilio api to be sent as a sms to the phone with all the information from the sensors. 

To make sure i dont send sms every 10 minutes there is a check in place checking if it is the right signal number otherwise it does nothing.

Since the device will be put in my apartment I did not feel the need to have any battery attached to it and only put wifi since it will be sitting right next to the router which means range will neither be a problem for this project.
## Presenting the data
In the figure below we can see how I have chosen to present the data on the dashboard, the 2 most important signals are displayed on the dashboard and have chosen to have a pull size of 288 which is 2 full days of 10 minute updates to provide a nice curvature of the data and the possibility to easily see the increase/decrease of temperature/humidity during the days.

With everything being saved on pybytes and no use of other cloud service or database, the data here is preserved for 1 month before being deleted which is more than enough time to check the inside climate change over time.

The automation being made are from the webhook on pybytes sending information to the webserver.
![](https://i.imgur.com/uo8VEhg.png)
>Figure 4, Dashboard of pybytes

## Finalizing the design
This is the final project, I did not get time to fix it any casing but will probably put it in a food box for longer data collection as it has been connected through my computer now instead. I think this course has been extremely fun and useful for me since I for a longer time wanted to learn more about IoT but feel a bit sad that I did not come up with a better project idea since I am sure I could have done way better. 

There are several improvements that could have been done, the reason the cables are all different is that multiple sensors were being used first resulting in not having enough colors and the http post call should have worked directly from the lopy with urequests but after multiple hours of trying to find a solution and also with multiple other people looking into it we could not find a solution.

This lead me to creating a webserver instead so I could make the http calls with javascript instead on a webserver open on a public port (NOT THE SAFEST) and since I had no credentials it was not a problem.
This worked out really well since pybytes has great webhook integration and I could connect it directly to the webserver without any problems.

Then there is the problem of error checking more, I should have implemented maybe a bit more catches of potential errors so that the whole program does not just stop working and instead sends a error message to the console, same goes for the webserver where I also could implement a check for token to make sure no one else can make calls.
![](https://i.imgur.com/Sq1vF9h.jpg)
>Picture 1, Final result

Below is shown how the data is presented on the phone after the button is being pressed.
![](https://i.imgur.com/lNFlStU.jpg)
>Picture 2, The notification





