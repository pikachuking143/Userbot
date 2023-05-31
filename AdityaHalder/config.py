import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "25926586"))
API_HASH = getenv("API_HASH", "642d4eceda4a20fe656e05de9764378c")
BOT_TOKEN = getenv("BOT_TOKEN", "6238568856:AAEVwEADIEq6yKQW58UGQxpDVStBRA6UWuk")
STRING_SESSION = getenv("STRING_SESSION", "BQAh5fsKwC4D5zzdrGsW5z9Vo8cvhBIbSTuip2IlZYtVoe1dVCuojm_ne0tUNrpRK9HgGc_2gQPOqhSq3cVRPk_tqEbVKEgR2yJpY7l40hx-PhxFADCF6BnPv8MYVAgzoMdG9iTC0I4hB6ha8jMH5B5E2Dg7Z5y5f2iWaT9fTcKtGq5e7u45OTl_1QypqFTco_ZiZ2ewRBy0BeMLf5jVg8F3-9DIr0EyhsHq5sVZYGWtK8oe7T5XlEj0zYuYY2W5nZQsbW-FuhE1hO1CH8TQTAYCF5onKyqNbB2PIFIzbSTl0jii5uV5zQy1-4e8g96avAVfCME-oNlUFs-8-2w01kAAAAAW66KoUA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://doboh53061:adhya789@cluster0.pcv0ubh.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6152661637").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001828684256"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6152661637").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/XdityaHalder/Genius-Userbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
