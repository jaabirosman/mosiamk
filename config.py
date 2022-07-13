# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAkcO4N6bBz4buGS1A7xDRoS7L3-L9KuNzXBIB_Fr7lqb2LyFE1I2lBtMcO9aRQOJroutYTqhj5QdpyDzjp4sE-FkstbsPb-clB8_DYH3NVgVr3l7fMiWFJ6G0VhnnOnSYyUaVtEFZKqeCcdUv0abbx5GQupXzn0dVPckfdENJCdrZv2mIFnMCko_GyDSfQDGeecm3VVqMvXLO5YeptHQCsDops_vokxoi4wCikVeP9sfAIiMT5CpWSibY_sAEReFzJTdRehBDf4jKE6WwOmVZluOsNwHhLKi-Wn_shMgEwHd0UxfKzKDwPf_YTbdgjCBJi7PX6fJsrBwYJU0232tVvAAAAATTDl_YA")
BOT_TOKEN = getenv("BOT_TOKEN", "5462008662:AAG5mk5QF0JNi_ruvoiSmdREHMiUOMZlxNY")
BOT_NAME = getenv("BOT_NAME", "Osmani Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "teamosmani")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/09d6c7cc130bec60767f2.jpg")
admins = {}
API_ID = int(getenv("API_ID", "15499461"))
API_HASH = getenv("API_HASH", "ff93948d3b7c3091e8d573275a4ed80f")
BOT_USERNAME = getenv("BOT_USERNAME", "Ribaj_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ribajassistant2")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "osmanigroupbot")
PROJECT_NAME = getenv("PROJECT_NAME", "RibajXmusic v2")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/Ribaj")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "4500"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1008271006").split()))
