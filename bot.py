import json
import requests
import time
import urllib
from base import app, db
from base.models import faq
from similarity import similarity

TOKEN = "924202097:AAEm9tGw4SIjNKHN_AC_nnhfCCX0Nd9ssgs"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)



def echo_all(updates):
    found = 0
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            prev_score = 0
            instances = faq.query.all()
            print(instances)
            for instance in instances:
                score, match = similarity(text,instance.question)
                if match and prev_score < score:
                    Atext = instance.answer
                    chat = update["message"]["chat"]["id"]
                    found = 1
                    prev_score = score

            if found != 1:
                Atext = "Sorry I didn't quite get you"
                chat = update["message"]["chat"]["id"]
                send_message(Atext, chat)
            else:
                send_message(Atext, chat)
        except Exception as e:
            print(e)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
