import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# admins = [
#     os.getenv("ADMIN_ID"),
# ]
admins = [
    1079453114,
]
channels = ['@get_me1']

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
