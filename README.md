# Covid-19 Vaccine Tracker (Telegram Bot)
A telegram bot which notifies the user of an available vaccine slot booking using Co-Win API.

We will be using the Co-win public API’s provided by the government to track vaccines without the need to login into the Co-Win website portal or the Aarogya Setu App every time to check for a vaccine slot booking.

# Contents:

**Telegram Bot:**

Creating a telegram bot using BotFather which is a bot used to create a bot in telegram.

Upon creating a bot the developer will be provided with a unique HTTP API token which can be used to control the bot.

Then we add it to a telegram group with the user so it can notify the user if a vaccine booking slot is available.


**Python Code:**

We write a python code which will ping the Co-Win API and retrieve the data for the vaccine slot booking.

We then extract the data and feed it to our bot who then sends it in the form of a message in the telegram group.


This way the user can have access to the vaccine slot booking from their computer or their mobiles phone using the telegram app and get vaccinated as soon as possible .



**API used : Aarogya Setu API to display vaccination centres (ONLY FOR INDIA)**

**API : https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}**

# Steps to run:
**To run the bot on a local machine**

Go to the path in the terminal where the file is saved and run it by :

```
python3 main.py
```

# Telegram Bot
To add the bot to your Telegram app search for:

`https://t.me/covid19_VaccineTracker_INDIA_bot` in your Web Browser

or 

 `covid19_VaccineTracker_INDIA_bot` in the search bar for username field in the Telegram App

**Curently my bot is hosted on Heroku, if it doesn't respond to your command give it some minutes as the bot might be dormant.**

