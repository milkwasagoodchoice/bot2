git
remote
add
origin
https: // github.com / milkwasagoodchoice / bot2.git
git
branch - M
main
git
push - u
origin
main
import requests
import schedule
import datetime
import json
import asyncio
from telegram import Bot
import argparse
import requests
import schedule
import time
from datetime import datetime as dt

TELEGRAM_TOKEN = '7713171054:AAF4sL1XxoU6yyMCZftuj870n5iQPGj-nxo'
CHAT_ID = '109194797'

 #stone island
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'  # You can change this to 'Markdown' if needed
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        print("Message sent to Telegram.")
    except requests.RequestException as e:
        print(f"Error sending message to Telegram: {e}")


# Function to get and send selected content from the API for a specific query
def get_selected_content(query, store_id=5):
    # URL for the API request based on the query
    url = f"https://www.extraloppan.is/boerneloppen-theme/searches/search.json?page=1&query={query}&boerneloppen_theme_store_id={store_id}&boerneloppen_theme_status_id=&sort=name&direction=ASC&only_own_products=false&show_marked_inactive=false"

    # Headers from the provided cURL command
    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'cookieSafe=%7B%22date%22%3A%222024-10-26%22%7D; _ga=GA1.2.1492334422.1729951084; _gid=GA1.2.591370508.1729951084; vmcms=471427930748ac3950065627e60cecb4; _ga_QGEHQDPWYD=GS1.2.1729983899.3.1.1729984222.0.0.0',
        'priority': 'u=1, i',
        'referer': 'https://www.extraloppan.is/leitaou-ao-voeru?boerneloppen_theme_store_id=5&query=',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response

        # Check if the response contains products
        if 'data' in data and isinstance(data['data'], list):
            products = data['data']
            formatted_message = f"Products Found for '{query}':\n"

            # Loop through products and extract name, price, and stand
            for product in products:
                name = product.get('name', 'No Name')  # Default if name not found
                price = product.get('price', 'No Price')  # Default if price not found
                stand = product.get('stand', 'No Stand')  # Default if stand not found
                formatted_message += f"- Name: {name}, Price: {price}, Stand: {stand}\n"

            # Send the formatted content to the Telegram bot
            send_to_telegram(formatted_message)
        else:
            send_to_telegram(f"No products found for '{query}'.")

    except requests.RequestException as e:
        print(f"Error fetching data for '{query}': {e}")


if __name__ == "__main__":
    # List of queries to search
    queries = ["stone island"]
    for query in queries:
        get_selected_content(query)

#ganni
url = "https://www.extraloppan.is/boerneloppen-theme/searches/search.json?page=1&query=ganni&boerneloppen_theme_store_id=5&boerneloppen_theme_status_id=&sort=name&direction=ASC&only_own_products=false&show_marked_inactive=false"

# Headers from the provided cURL command
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'cookieSafe=%7B%22date%22%3A%222024-10-26%22%7D; _ga=GA1.2.1492334422.1729951084; _gid=GA1.2.591370508.1729951084; vmcms=471427930748ac3950065627e60cecb4; _gat_UA-143241006-1=1; _ga_QGEHQDPWYD=GS1.2.1729983899.3.1.1729984222.0.0.0',
    'priority': 'u=1, i',
    'referer': 'https://www.extraloppan.is/leitaou-ao-voeru?boerneloppen_theme_store_id=5&query=',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


# Function to send a message to the Telegram bot
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'  # You can change this to 'Markdown' if needed
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        print("Message sent to Telegram.")
    except requests.RequestException as e:
        print(f"Error sending message to Telegram: {e}")


# Function to get and send selected content from the API
def get_selected_content():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response

        # Check if the response contains products
        if 'data' in data and isinstance(data['data'], list):
            products = data['data']
            formatted_message = "Products Found:\n"

            # Loop through products and extract name, price, and stand
            for product in products:
                name = product.get('name', 'No Name')  # Default if name not found
                price = product.get('price', 'No Price')  # Default if price not found
                stand = product.get('stand', 'No Stand')  # Default if stand not found
                formatted_message += f"- Name: {name}, Price: {price}, Stand: {stand}\n"

            # Send the formatted content to the Telegram bot
            send_to_telegram(formatted_message)
        else:
            send_to_telegram("No products found in the response.")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    get_selected_content()

#cp company

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'  # You can change this to 'Markdown' if needed
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        print("Message sent to Telegram.")
    except requests.RequestException as e:
        print(f"Error sending message to Telegram: {e}")


# Function to get and send selected content from the API for a specific query
def get_selected_content(query, store_id=5):
    # URL for the API request based on the query
    url = f"https://www.extraloppan.is/boerneloppen-theme/searches/search.json?page=1&query={query}&boerneloppen_theme_store_id={store_id}&boerneloppen_theme_status_id=&sort=name&direction=ASC&only_own_products=false&show_marked_inactive=false"

    # Headers from the provided cURL command
    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'cookieSafe=%7B%22date%22%3A%222024-10-26%22%7D; _ga=GA1.2.1492334422.1729951084; _gid=GA1.2.591370508.1729951084; vmcms=471427930748ac3950065627e60cecb4; _ga_QGEHQDPWYD=GS1.2.1729983899.3.1.1729984222.0.0.0',
        'priority': 'u=1, i',
        'referer': 'https://www.extraloppan.is/leitaou-ao-voeru?boerneloppen_theme_store_id=5&query=',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response

        # Check if the response contains products
        if 'data' in data and isinstance(data['data'], list):
            products = data['data']
            formatted_message = f"Products Found for '{query}':\n"

            # Loop through products and extract name, price, and stand
            for product in products:
                name = product.get('name', 'No Name')  # Default if name not found
                price = product.get('price', 'No Price')  # Default if price not found
                stand = product.get('stand', 'No Stand')  # Default if stand not found
                formatted_message += f"- Name: {name}, Price: {price}, Stand: {stand}\n"

            # Send the formatted content to the Telegram bot
            send_to_telegram(formatted_message)
        else:
            send_to_telegram(f"No products found for '{query}'.")

    except requests.RequestException as e:
        print(f"Error fetching data for '{query}': {e}")


if __name__ == "__main__":
    # List of queries to search
    queries = ["cp company"]
    for query in queries:
        get_selected_content(query)

#palace

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'  # You can change this to 'Markdown' if needed
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        print("Message sent to Telegram.")
    except requests.RequestException as e:
        print(f"Error sending message to Telegram: {e}")


# Function to get and send selected content from the API for a specific query
def get_selected_content(query, store_id=5):
    # URL for the API request based on the query
    url = f"https://www.extraloppan.is/boerneloppen-theme/searches/search.json?page=1&query={query}&boerneloppen_theme_store_id={store_id}&boerneloppen_theme_status_id=&sort=name&direction=ASC&only_own_products=false&show_marked_inactive=false"

    # Headers from the provided cURL command
    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'cookieSafe=%7B%22date%22%3A%222024-10-26%22%7D; _ga=GA1.2.1492334422.1729951084; _gid=GA1.2.591370508.1729951084; vmcms=471427930748ac3950065627e60cecb4; _ga_QGEHQDPWYD=GS1.2.1729983899.3.1.1729984222.0.0.0',
        'priority': 'u=1, i',
        'referer': 'https://www.extraloppan.is/leitaou-ao-voeru?boerneloppen_theme_store_id=5&query=',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response

        # Check if the response contains products
        if 'data' in data and isinstance(data['data'], list):
            products = data['data']
            formatted_message = f"Products Found for '{query}':\n"

            # Loop through products and extract name, price, and stand
            for product in products:
                name = product.get('name', 'No Name')  # Default if name not found
                price = product.get('price', 'No Price')  # Default if price not found
                stand = product.get('stand', 'No Stand')  # Default if stand not found
                formatted_message += f"- Name: {name}, Price: {price}, Stand: {stand}\n"

            # Send the formatted content to the Telegram bot
            send_to_telegram(formatted_message)
        else:
            send_to_telegram(f"No products found for '{query}'.")

    except requests.RequestException as e:
        print(f"Error fetching data for '{query}': {e}")

import requests


# Function to send a message to the Telegram bot
def send_telegram_message(chat_id, message, bot_token):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'  # Optional: use HTML formatting
    }
    response = requests.post(url, data=payload)
    return response.status_code == 200

if __name__ == "__main__":
    # List of queries to search
    queries = ["palace"]
    for query in queries:
        get_selected_content(query)


# Define the Telegram bot token and chat ID
BOT_TOKEN = '7713171054:AAF4sL1XxoU6yyMCZftuj870n5iQPGj-nxo'  # Replace with your bot's token
CHAT_ID = '109194797'  # Replace with your chat ID

# Define the URL and headers
url = 'https://svc-121-usf.hotyon.com/search'
headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://riteil.is',
    'priority': 'u=1, i',
    'referer': 'https://riteil.is/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

# Define the query parameters
params = {
    'q': 'stone island',
    'apiKey': 'cde900dd-9968-4655-9573-813d8c444b9a',  # Corrected API key string
    'country': 'IS',
    'locale': 'is',
    'skip': '0',
    'take': '40',
    'sort': '-date'
}

# Make the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON data

    # Attempt to access items in nested structure
    items = data.get("data", {}).get("items", [])  # Adjust keys if necessary

    # Prepare message content
    messages = []

    # Print each item with specific fields if items are found
    if items:
        for item in items:
            title = item.get('title', 'N/A')  # Get title or 'N/A' if not found
            tags = item.get('tags', [])  # Get tags or empty list if not found

            # Prepare message for each item
            message = f"Title: {title}\n"

            # Process and print only the BÁS from tags
            if tags:
                message += "BÁS in Tags:\n"
                for tag in tags:
                    message += f"  - BÁS: {tag}\n"  # Print each tag directly
            else:
                message += "No tags available.\n"

            # Process and print only the price in variants
            variants = item.get('variants', [])
            if variants:
                message += "Price:\n"
                for variant in variants:
                    price = variant.get('price', 'N/A')  # Get price or 'N/A' if not found
                    message += f"  - Price: {price}\n"
            else:
                message += "No variants available.\n"

            messages.append(message)
            messages.append("-" * 20)  # Separator for readability

    # Send each message to Telegram
    for msg in messages:
        send_telegram_message(CHAT_ID, msg, BOT_TOKEN)

else:
    print("Failed to retrieve data:", response.status_code)




# Function to send a message to the Telegram bot
def send_telegram_message(chat_id, message, bot_token):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'  # Optional: use HTML formatting
    }
    response = requests.post(url, data=payload)
    return response.status_code == 200




def job():
    for query in queries:
        get_selected_content(query)

# Schedule the job every two hours between 11:00 and 18:00
schedule.every(2).hours.at(":00").do(job)  # At 00 minutes
schedule.every(2).hours.at(":30").do(job)  # At 30 minutes

# Run the scheduler
while True:
    current_time = dt.now()  # Use the alias for datetime
    if 11 <= current_time.hour < 18:  # Check if current time is between 11 AM and 6 PM
        schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking again
