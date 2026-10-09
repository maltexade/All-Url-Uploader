# Deploy All-Url-Uploader to fps.ms

## What You Need

1. **fps.ms Account** → Sign up at [fps.ms](https://fps.ms) (free)
2. **Telegram Bot Token** → Get from [@BotFather](https://t.me/BotFather)
3. **API_ID & API_HASH** → Get from [my.telegram.org](https://my.telegram.org)
4. **OWNER_ID** → Your Telegram user ID

## Step 1: Create fps.ms Server

1. Log in to [fps.ms Dashboard](https://fps.ms)
2. Click **Deploy Container**
3. Select **Python** runtime
4. Name your server (e.g., `url-uploader-bot`)
5. Click **Create**

## Step 2: Download Files from GitHub

1. Go to https://github.com/maltexade/All-Url-Uploader
2. Click **Code** → **Download ZIP**
3. Extract the ZIP file
4. Copy **ALL** files and folders

## Step 3: Upload to fps.ms

Use **SFTP** (recommended for fast uploads):

1. In fps.ms panel, go to **Settings** → **SFTP Details**
2. Note your SFTP credentials
3. Use FileZilla or any SFTP client to connect
4. Upload all extracted files to the server

**OR use Panel File Manager** (slower but simpler):

1. Go to **Files** tab in fps.ms panel
2. Create folders: `plugins/`, `plugins/functions/`
3. Upload all files one by one

## Step 4: Create .env File on fps.ms

**Important: Do NOT use the .env.fps file from GitHub**

1. In fps.ms panel, go to **Files** tab
2. Create a new file named `.env`
3. Paste this content:

```env
BOT_TOKEN=your-actual-bot-token
API_ID=your-actual-api-id
API_HASH=your-actual-api-hash
OWNER_ID=your-telegram-user-id
AUTH_USERS=your-user-id
```

4. Replace the placeholders with your actual values
5. Save the file

## Step 5: Start the Bot

1. Go to **Console** tab in fps.ms panel
2. Click **Start**
3. Wait for output like:
   ```
   ✅ Configuration loaded successfully
   🤖 Bot has started successfully
   ✨ Bot is running 24/7 on fps.ms
   ```

## Step 6: Test Your Bot

1. Open Telegram
2. Find your bot
3. Send `/start`
4. Bot should respond with welcome message

## File Structure Expected on fps.ms

```
/
├── app.py                    ← fps.ms entry point
├── bot.py                    ← original bot code
├── config.py                 ← configuration
├── requirements.txt          ← dependencies
├���─ .env                      ← your secrets (CREATE THIS)
├── Dockerfile                ← (optional)
├── Procfile                  ← (optional)
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
└── ... (other files from repo)
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'pyrogram'"
- Check that `requirements.txt` was uploaded
- Click **Restart** in Console
- Wait 30 seconds for dependencies to install

### "BOT_TOKEN not set"
- Verify `.env` file exists in root directory
- Check token is correct from @BotFather
- Click **Restart**

### "Bot starts but doesn't respond"
- Check Console logs for errors
- Verify bot token is correct
- Make sure you're messaging the bot in private chat
- Check `/start` command is registered in @BotFather

### "Disk space full" error
- Your bot downloads large files
- Check **Resources** tab for disk usage
- Consider fps.ms paid plan if you exceed limits
- Or modify `config.py` to delete files after upload

## Monitoring

**Check Bot Status:**
- Console tab shows real-time logs
- Resources tab shows CPU/RAM/Disk usage

**Edit Code:**
- Go to Files tab and edit directly, OR
- Use SFTP to edit in your text editor, OR
- Use VS Code with SFTP extension for auto-sync

**Restart After Changes:**
- Always click **Restart** in Console after editing code

## Tips

1. **Save disk space**: Modify `config.py` to use `/tmp` for downloads
   ```python
   DOWNLOAD_LOCATION = "/tmp"
   ```

2. **Auto-cleanup**: Add to your upload handlers to delete files after sending
   ```python
   os.remove(file_path)
   ```

3. **Monitor logs**: Check Console regularly for errors or warnings

## Support

- **fps.ms Docs**: https://docs.fps.ms
- **fps.ms Discord**: Join their Discord community
- **Pyrogram Docs**: https://docs.pyrogram.org
- **GitHub Issues**: https://github.com/maltexade/All-Url-Uploader/issues

---

**Your bot is now live 24/7 on fps.ms!** 🚀
