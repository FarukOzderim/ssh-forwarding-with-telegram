import sys
import os
import subprocess as sp
from pyngrok import ngrok
import requests
import time

telegram_token = str(os.environ.get("TELEGRAM_TOKEN"))
port = int(os.environ.get("PORT"))
chat_id = str(os.environ.get("CHATID"))
ngrok_token = str(os.environ.get("NGROK_TOKEN"))
result = sp.run(["whoami"], capture_output=True)
username = result.stdout.decode('UTF-8')[:-1]
ngrok.set_auth_token(ngrok_token)
ssh_tunnel = ngrok.connect(port, "tcp")
print(ssh_tunnel)
ssh_url_all = ssh_tunnel.public_url
ssh_temp = ssh_url_all.split("tcp://",1)[1]
ssh_url , ssh_port = ssh_temp.split(":",1)
print(ssh_url, ssh_port)
TELEGRAM_SEND_MESSAGE_URL = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
payload = {
            'chat_id': chat_id,
            'text': f"ssh -p {ssh_port} {username}@{ssh_url}"
        }

response = requests.post(TELEGRAM_SEND_MESSAGE_URL, json=payload)
print(response.json())
time.sleep(365*24*60*60)