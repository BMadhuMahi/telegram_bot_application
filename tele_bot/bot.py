import os
import sys
import django
import requests
import time

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tele_bot_app.settings")
django.setup()

from api_app.models import TelegramProfile
from django.conf import settings

TOKEN = settings.TELEGRAM_BOT_TOKEN
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def handle_start_command(username):
    if not TelegramProfile.objects.filter(telegram_username=username).exists():
        TelegramProfile.objects.create(telegram_username=username)

def process_update(update):
    message = update.get("message", {})
    if message.get("text") == "/start":
        user = message.get("from", {})
        username = user.get("username")
        if username:
            handle_start_command(username)
            chat_id = message["chat"]["id"]
            text = f"Hi {username}, you're now registered!"
            send_message(chat_id, text)

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

def run():
    print("Polling Telegram bot...")
    offset = None
    while True:
        try:
            updates = get_updates(offset)
            for update in updates:
                process_update(update)
                offset = update["update_id"] + 1
            time.sleep(1)
        except Exception as e:
            print("Error:", e)
            time.sleep(5)

if __name__ == "__main__":
    run()
