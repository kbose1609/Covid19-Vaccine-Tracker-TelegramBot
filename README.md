# Cowin-bot
A telegram bot which notifies the user of an available vaccine slot booking using Co-Win API.

We will be using the Co-win public API’s provided by the government to track vaccines without the need to login into the Co-Win website portal or the Aarogya Setu App every time to check for a vaccine slot booking.

Contents:

A Telegram Bot:

Creating a telegram bot using BotFather which is a bot used to create a bot in telegram.

Upon creating a bot the developer will be provided with a unique HTTP API token which can be used to control the bot.

Then we add it to a telegram group with the user so it can notify the user if a vaccine booking slot is available.


Python code:

We write a python code which will ping the Co-Win API and retrieve the data for the vaccine slot booking.

We then extract the data and feed it to our bot who then sends it in the form of a message in the telegram group.


This way the user can have access to the vaccine slot booking from their computer or their mobiles phone using the telegram app and get vaccinated as soon as possible .


api used : aarogya setu api to display vaccination centres 
