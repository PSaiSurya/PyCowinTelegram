# PyCowinTelegram
Queries Cowin public API and notifies in your Telegram Channel or Group, if new slots open

Made with Python

Get started with your District ID from Cowin Portal and Chat ID of your Telegram Channel/Group

Tested Working on <b> Python 3.9+ (Windows 10) </b>


# Creating a Virtual Environment (Optional, Can be Skipped)

* Install [Anaconda](https://www.anaconda.com/products/individual)
* Use Anaconda to create a virtual environment and Activate it

<b>For Step by Step Instructions, </b> https://medium.com/swlh/setting-up-a-conda-environment-in-less-than-5-minutes-e64d8fc338e4#:~:text=Scenario%203%3A%20You,conda%20activate%20%3Cenvironment_name%3E.



# Installing Requirements  

```python
pip install requirements.txt
```



# Getting District ID from Cowin Portal
Use the following code to get your district ID

````python
import requests
import json
from fake-useragent import UserAgent

Agent = UserAgent()
header = {"User-Agent":Agent.random}
for states in range(1,40):
  print("State Code: ",states)
  response = requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{states}", headers=browser_header)
  json_data = json.loads(response.text)
    for state in json_data["districts"]:
        print(state["district_id"],'\t', state["district_name"])
    print("\n")

````


# Getting Chat ID from Telegram

## 1. Creating a Telegram Bot
(Source: https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq)

To set up a new bot, start the conversation with BotFather (@BotFather).
BotFather will help us in creating the new bot.
* Search for @botfather in Telegram.
* Start your conversation by pressing the Start button.
* Create the bot by running /newbot command
* Enter the Display Name and User Name for the bot.
* BotFather will send you a message with the token

<b>DISCLAIMER</b> — Keep access token of the bot securely. Anyone with your token can manipulate this bot.
 
## 2. Telegram Bot and Chat ID
* Create a new Telegram Channel or group (It can be Public/Private)
* Add your bot to the Channel/Group 
* Send a sample message to your Channel
* Forward the same to [@JsonDumpBot](https://t.me/JsonDumpBot)
* Get the ID

<b>DISCLAIMER</b> — Im not an affiliate and [@JsonDumpBot](https://t.me/JsonDumpBot) is not my bot.
![alt text](https://i.stack.imgur.com/whXiS.png)




<h3> Feel free to use this code in your application </h3>
<h3> Show your ❤️ by ⭐ this Repository </h3> 
