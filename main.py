import Constants as keys
from telegram.ext import *
import responses as R
import requests, json
from datetime import date

today=date.today()
d1 = today.strftime("%d-%m-%yY")

print('Bot is starting')

def start_command(update, context):
	update.message.reply_text('Hi, welcome to the Covid Vaccine tracker Bot.')
	update.message.reply_text(' To custom search for a vaccination slot type (pincode:dd-mm-yyyy) for eg 400055:25-10-2021')

def vaccine_command(update, context):
	pin = '400053'
	date = d1
	url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}'
	browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
	print(url)
	response = requests.get(url, headers=browser_header)
	print(response)
	json_data = response.json()
	final_text = ''
	if len(json_data['sessions'])==0:
		print("\nSlots Not Available\n")
	else:
		for slots in json_data['sessions']:
			final_text = final_text + "\nName: " + str(slots['name']) + '\n' + "Available Capacity: " + str(slots['available_capacity']) + '\n' + "Min Age Limit: " + str(slots['min_age_limit']) + '\n' + "Vaccine: " + str(slots['vaccine']) + '\n' + "Fee Type: " + str(slots['fee_type']) + '\n'"Fee: " + str(slots['fee']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)

def handle_message(update, context):
	text = str(update.message.text).lower()
	user = update.effective_user
	print(f'{user["username"]}: {text}')
	response = R.sample_responses(text)
	print(f'Bot: {response}')
	update.message.reply_text(response)

def error(update, context):
	print(f"Update {update} caused error {context.error}")

def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("vaccine", vaccine_command))
	dp.add_handler(MessageHandler(Filters.text, handle_message))
	dp.add_error_handler(error)


	updater.start_polling()
	updater.idle()

main()