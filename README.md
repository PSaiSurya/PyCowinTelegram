# PyCowinTelegram
Queries <b>Cowin public API</b>, then sends the details of new slots in your district to your <b>Telegram</b> Channel or Group.

Made with ❤️ using <b>Python</b> 🐍.

Get started with your <b>District ID</b> and <b>Chat ID</b> of your Telegram Channel/Group.

Requires <b> Python 3.9+ </b> 

Tested working on <b> Windows 10 </b>.

Works only in <b>India</b> (🇮🇳) due to <b>Geofencing</b> of the API.


# Getting Started

## Creating a Virtual Environment (Optional, Can be Skipped)

* Install [Anaconda](https://www.anaconda.com/products/individual)
* Use Anaconda to create a virtual environment and Activate it

   For detailed steps, see [here](https://medium.com/swlh/setting-up-a-conda-environment-in-less-than-5-minutes-e64d8fc338e4#:~:text=Scenario%203%3A%20You,conda%20activate%20%3Cenvironment_name%3E)



## Installing Requirements  

```python
pip install requirements.txt
```


## District ID from Cowin Portal
Use the following code to get your district ID

````python
import requests
import json
from fake_useragent import UserAgent

Agent = UserAgent()
browser_header = {"User-Agent":Agent.random}
for states in range(1,40):
  print("State Code: ",states)
  response = requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{states}", headers=browser_header)
  json_data = json.loads(response.text)
  for state in json_data["districts"]:
    print(state["district_id"],'\t', state["district_name"])
  print("\n")

````


## Chat ID from Telegram

### 1. Creating a Telegram Bot 

To set up a new bot, start the conversation with BotFather (@BotFather).
BotFather will help us in creating the new bot.
* Search for @botfather in Telegram.
* Start your conversation by pressing the Start button.
* Create the bot by running /newbot command
* Enter the Display Name and User Name for the bot.
* BotFather will send you a message with the token

<b>DISCLAIMER</b> — Keep access token of the bot securely. Anyone with your token can manipulate this bot.

 
### 2. Telegram Bot and Chat ID
* Create a new Telegram Channel or group (It can be Public/Private)
* Add your bot to the Channel/Group 
* Send a sample message to your Channel
* Forward the same to [@JsonDumpBot](https://t.me/JsonDumpBot)
* Get the ID

<b>DISCLAIMER</b> — I'm not an affiliate and [@JsonDumpBot](https://t.me/JsonDumpBot) is not my bot.
![alt text](https://i.stack.imgur.com/whXiS.png)



# FAQ
## 1. I do not want to use Telegram and view the details of new slots in the Output Screen(Terminal/CMD/Powershell) instead. What to do?

* Uncomment <b>Line 150</b> in main.py
* Comment <b>Lines 151,152 </b> in main.py

<br>
<br>
<h3> Feel free to use this code in your application 😃 </h3>
<h3> Show your ❤️ by ⭐ this Repository </h3> 


[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FPSaiSurya%2FPyCowinTelegram&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=Visits&edge_flat=false)](https://hits.seeyoufarm.com)
