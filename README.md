# ssher-telegram

You can run the ssh forwarding like this, you need to have a telegram bot and get your chatid from your chat or group. You can also set this program as a 
systemd service which will run in boot, see [here](https://www.howtogeek.com/687970/how-to-run-a-linux-program-at-startup-with-systemd/). 

## Requirements
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install httpx pyngrok
```

## Run
```
#!/bin/bash
cd [path]
export PORT=22
export TELEGRAM_TOKEN=[YOUR_TOKEN]
export CHATID=[TELEGRAM_CHAT_ID]
export NGROK_TOKEN=[YOUR_TOKEN]

python3 ssher.py
```

Feel free to open an issue if you have any questions.
