import os

from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Bot
# ==========================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# نام کاربری ربات (بدون @)
BOT_USERNAME = "MarketDanRadarBot"

# ==========================================
# Required Channels
# ==========================================

REQUIRED_CHANNELS = [
    "@MarketDanRadar",
    "@MarketDanRadarBackup",
    "@MarketDanRadar_Group",
]

# لینک کانال‌ها
CHANNEL_LINKS = {
    "@MarketDanRadar": "https://t.me/MarketDanRadar",
    "@MarketDanRadarBackup": "https://t.me/MarketDanRadarBackup",
    "@MarketDanRadar_Group": "https://t.me/MarketDanRadar_Group",
}

# ==========================================
# Project
# ==========================================

PROJECT_NAME = "MARKET DAN RADAR"

VERSION = "3.0.0"

# ==========================================
# APIs
# ==========================================

NAVASAN_API_KEY = os.getenv("NAVASAN_API_KEY")

# ==========================
# Admin
# ==========================

ADMIN_CHAT_ID = 8920456282