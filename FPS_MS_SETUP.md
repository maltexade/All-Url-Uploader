# Deploying All-Url-Uploader to fps.ms

This guide walks you through hosting your Telegram bot on **fps.ms** — a free platform with 24/7 uptime for Telegram bots.

## Prerequisites

1. **fps.ms Account** → Sign up at [fps.ms](https://fps.ms)
2. **Telegram Bot Token** → Get from [@BotFather](https://t.me/BotFather)
3. **API_ID & API_HASH** → Get from [my.telegram.org](https://my.telegram.org)
4. **OWNER_ID** → Your Telegram user ID (send `/start` to any bot to find it)

## Step 1: Create fps.ms Server

1. Go to [fps.ms Dashboard](https://fps.ms)
2. Click **Deploy Container**
3. Select **Python** as the runtime
4. Choose a server name (e.g., `url-uploader-bot`)
5. Click **Create**

## Step 2: Upload Your Bot Files

You have 3 options:

### Option A: Upload via Panel File Manager (Easiest)

1. In fps.ms panel, go to **Files** tab
2. Create the folder structure:
   ```
   /
   ├── app.py (rename from bot.py)
   ├── config.py
   ├── requirements.txt
   ├── .env
   ├── plugins/
   │   ├── __init__.py
   │   ├── commands.py
   │   ├── echo.py
   │   ├── callbacks.py
   │   ├── button.py
   │   ├── dl_button.py
   │   ├── youtube.py
   │   ├── script.py
   │   ├── thumbunali.py
   │   ├── utitles.py
   │   └── functions/
   ```

3. Upload files one by one

### Option B: Upload via SFTP (Recommended for Large Projects)

1. Go to **Settings** → **SFTP Details** in fps.ms panel
2. Note your SFTP credentials:
   - Host: `mango/papaya/pineapple/guava/other.fps.ms`
   - Port: `2022`
   - Username: (shown in panel)
   - Password: (set in panel)

3. Use FileZilla or any SFTP client:
   - Connect with above credentials
   - Upload your bot folder contents

### Option C: Deploy from GitHub

1. Go to **Startup** tab → **Git Repo Address**
2. Enter: `https://github.com/maltexade/All-Url-Uploader`
3. Set **Branch**: `main`
4. Click **Reinstall Server**

*(If your repo is private, add Git Access Token)*

## Step 3: Configure Environment Variables

1. In fps.ms panel, go to **Files** tab
2. Create a file named `.env` with:

```env
BOT_TOKEN=your-telegram-bot-token-here
API_ID=your-api-id
API_HASH=your-api-hash
OWNER_ID=your-telegram-user-id
AUTH_USERS=your-user-id other-user-ids
```

**Never commit `.env` to GitHub** — set it only on fps.ms.

## Step 4: Update requirements.txt

Make sure your `requirements.txt` includes:

```txt
aiohttp
hachoir
Pillow
pyrogram>=2.0.0
requests
tgcrypto
python-dotenv
loggers
yt-dlp
wget
youtube_dl
FFmpeg
```

## Step 5: Rename bot.py → app.py

fps.ms looks for `app.py` as the entry point. You have two options:

**Option 1: Rename the file**
- Rename `bot.py` → `app.py` in fps.ms Files tab

**Option 2: Create a new app.py that imports bot.py**

Create `app.py`:
```python
import os
from dotenv import load_dotenv
load_dotenv()

# Import and run bot
from config import Config
from pyrogram import Client, idle

if __name__ == "__main__":
    if not Config.BOT_TOKEN:
        print("ERROR: BOT_TOKEN not set in .env")
        exit(1)
    
    bot = Client(
        "All-Url-Uploader",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        workers=50,
        plugins=dict(root="plugins"),
    )
    
    bot.start()
    print("✅ Bot has started on fps.ms")
    idle()
```

## Step 6: Start Your Bot

1. Go to **Console** tab in fps.ms panel
2. Click **Start**
3. Wait for output like:
   ```
   Bot is running...
   ✅ Bot has started on fps.ms
   ```

4. Test in Telegram: Send `/start` to your bot

## Step 7: Monitor & Edit

**View Logs:**
- Console tab shows real-time logs

**Edit Code:**
- Panel: Edit files directly in Files tab
- SFTP: Upload changes via FileZilla
- VS Code: Use SFTP extension with auto-sync

**Restart Bot:**
- After editing code, click **Restart** in Console tab

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'pyrogram'`
- Add all dependencies to `requirements.txt`
- Click **Restart** in Console

### Error: `BOT_TOKEN not set`
- Check `.env` file exists and has correct token
- Verify variable names match `config.py`

### Bot starts but doesn't respond
- Check Console logs for errors
- Verify bot token is correct from @BotFather
- Make sure you're sending `/start` in private chat

### Large file downloads fail
- fps.ms has disk space limits for free tier
- Check Console for disk space errors
- Consider upgrading plan if needed

## Performance Tips

1. **Download Location** → Change in `config.py`:
   ```python
   DOWNLOAD_LOCATION = "/tmp"  # Use temp directory to save space
   ```

2. **Auto-cleanup** → Add to your download handler:
   ```python
   import os
   os.remove(downloaded_file)  # Delete after upload
   ```

3. **Monitor Usage**:
   - Go to **Resources** tab to see CPU/RAM/Disk usage
   - Adjust if bot is hitting limits

## Next Steps

✅ Bot is running 24/7 on fps.ms
✅ Send `/start` to your bot to test
✅ Customize commands in `plugins/commands.py`
✅ Add new features and restart

## Need Help?

- **fps.ms Docs**: https://docs.fps.ms
- **fps.ms Discord**: Join their community
- **Pyrogram Docs**: https://docs.pyrogram.org

---

**Your bot is now live on fps.ms!** 🚀
