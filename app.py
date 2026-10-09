"""Entry point for fps.ms deployment
fps.ms automatically runs app.py when the server starts
"""

import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from config import Config
from pyrogram import Client, idle, __version__
from pyrogram.raw.all import layer

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Create download directory if it doesn't exist
if not os.path.isdir(Config.DOWNLOAD_LOCATION):
    os.makedirs(Config.DOWNLOAD_LOCATION)
    logger.info(f"Created download directory: {Config.DOWNLOAD_LOCATION}")

# Validate required configuration
if not Config.BOT_TOKEN:
    logger.error("❌ BOT_TOKEN not set. Add it to .env file")
    exit(1)

if not Config.API_ID:
    logger.error("❌ API_ID not set. Add it to .env file")
    exit(1)

if not Config.API_HASH:
    logger.error("❌ API_HASH not set. Add it to .env file")
    exit(1)

logger.info("✅ Configuration loaded successfully")

# Initialize and start the bot
if __name__ == "__main__":
    bot = Client(
        "All-Url-Uploader",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        workers=50,
        plugins=dict(root="plugins"),
    )

    try:
        bot.start()
        logger.info("🤖 Bot has started successfully")
        logger.info(f"📦 Pyrogram Version: {__version__}")
        logger.info(f"🔧 Layer: {layer}")
        logger.info("💻 Hosting: fps.ms")
        logger.info("👤 Developer: github.com/kalanakt")
        logger.info("\n✨ Bot is running 24/7 on fps.ms")
        
        idle()
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}", exc_info=True)
        exit(1)
    finally:
        bot.stop()
        logger.info("🛑 Bot stopped")
