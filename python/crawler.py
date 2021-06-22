import json
import requests
import os
import sys
from bs4 import BeautifulSoup
static_dir_URL = './static'
if not os.path.isdir(static_dir_URL):
    os.mkdir(static_dir_URL)
URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
r = requests.get(URL).text
i = 1
cards = json.loads(r)['data']
for card in cards:
    card['image_url'] = card['card_images'][0]['image_url']
    del card['race']
    del card['card_prices']
    del card['card_images']
    if 'archetype' in card.keys():
        del card['archetype']
    if 'card_sets' in card.keys():
        del card['card_sets']
    # make card_id dir
    if not os.path.isdir(f"{static_dir_URL}/{card['id']}"):
        os.mkdir(f"{static_dir_URL}/{card['id']}")
    # save card info in json to static/{card_id}
    with open(f"{static_dir_URL}/{card['id']}/{card['id']}.json", 'w', encoding="utf-8") as fp:
        json.dump(card, fp, ensure_ascii=False, indent=2)
    # save card image in jpg to static/{card_id}
    image = requests.get(card['image_url']).content
    with open(f"{static_dir_URL}/{card['id']}/{card['id']}.jpg", 'wb') as fp:
        fp.write(image)
    print(f"{i}/{len(cards)}")
    i += 1