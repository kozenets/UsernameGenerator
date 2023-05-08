import random
import os
import requests
from bs4 import BeautifulSoup

# Отбираем слова соответствующей длины
prefixes = []
nouns = []
profanity = []
aggressive = []
cute = []
profession = []
popular = []
colors = []
hobbies = []
simple = []
short = []
qualities = []

for file in os.listdir():
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            words = f.read().splitlines()
            if 'prefixes' in file:
                prefixes += words
            elif 'nouns' in file:
                nouns += words
            elif 'profanity' in file:
                profanity += words
            elif 'aggressive' in file:
                aggressive += words
            elif 'cute' in file:
                cute += words
            elif 'profession' in file:
                profession += words
            elif 'popular' in file:
                popular += words
            elif 'colors' in file:
                colors += words
            elif 'hobbies' in file:
                hobbies += words
            elif 'simple' in file:
                simple += words
            elif 'short' in file:
                short += words
            elif 'qualities' in file:
                qualities += words

modes = {
    'prefixes + nouns': [prefixes, nouns],
    'prefixes + profanity': [prefixes, profanity],
    'prefixes + aggressive': [prefixes, aggressive],
    'prefixes + cute': [prefixes, cute],
    'prefixes + profession': [prefixes, profession],
    'prefixes + popular': [prefixes, popular],
    'prefixes + qualities': [prefixes, qualities],
    'prefixes + short': [prefixes, short],
    'prefixes + hobbies': [prefixes, hobbies],
    'prefixes + simple': [prefixes, simple],
    'prefixes + colors': [prefixes, colors],
    'nouns + profanity': [nouns, profanity],
    'nouns + aggressive': [nouns, aggressive],
    'nouns + cute': [nouns, cute],
    'nouns + profession': [nouns, profession],
    'nouns + popular': [nouns, popular],
    'nouns + qualities': [nouns, qualities],
    'nouns + short': [nouns, short],
    'nouns + hobbies': [nouns, hobbies],
    'nouns + simple': [nouns, simple],
    'nouns + colors': [nouns, colors],
    'profession + popular': [profession, popular],
    'profession + qualities': [profession, qualities],
    'profession + short': [profession, short],
    'profession + hobbies': [profession, hobbies],
    'profession + simple': [profession, simple],
    'profession + colors': [profession, colors],
    'popular + prefixes': [popular, prefixes],
    'popular + qualities': [popular, qualities],
    'popular + short': [popular, short],
    'popular + hobbies': [popular, hobbies],
    'popular + simple': [popular, simple],
    'popular + colors': [popular, colors],
    'profanity + aggressive': [profanity, aggressive],
    'profanity + cute': [profanity, cute],
    'profanity + profession': [profanity, profession],
    'profanity + popular': [profanity, popular],
    'profanity + qualities': [profanity, qualities],
    'profanity + short': [profanity, short],
    'profanity + hobbies': [profanity, hobbies],
    'profanity + simple': [profanity, simple],
    'profanity + colors': [profanity, colors],
    'aggressive + cute': [aggressive, cute],
    'aggressive + profession': [aggressive, profession],
    'aggressive + popular': [aggressive, popular],
    'aggressive + qualities': [aggressive, qualities],
    'aggressive + short': [aggressive, short],
    'aggressive + hobbies': [aggressive, hobbies],
    'aggressive + simple': [aggressive, simple],
    'aggressive + colors': [aggressive, colors],
    'cute + profession': [cute, profession],
    'cute + popular': [cute, popular],
    'cute + qualities': [cute, qualities],
    'cute + short': [cute, short],
    'cute + hobbies': [cute, hobbies],
    'cute + simple': [cute, simple],
    'cute + colors': [cute, colors],
    'qualities + short': [qualities, short],
    'qualities + hobbies': [qualities, hobbies],
    'qualities + simple': [qualities, simple],
    'qualities + colors': [qualities, colors],
    'short + hobbies': [short, hobbies],
    'short + simple': [short, simple],
    'short + colors': [short, colors],
    'hobbies + simple': [hobbies, simple],
    'hobbies + colors': [hobbies, colors],
    'simple + colors': [simple, colors]
}

print('Выберите режим:')
for i, mode in enumerate(modes.keys()):
    print(f'{i+1}. {mode}')
choice = int(input()) - 1
mode = list(modes.values())[choice]

Usernames = []
for i in range(len(mode[1])):
    Username = '@' + random.choice(mode[0]) + random.choice(mode[1])
    Usernames.append(Username)


def get_price_and_availability(Username):
    price = None
    availability = None
    x = Username[1:]
    response = requests.get(f'https://fragment.com/?query={x}')
    soup = BeautifulSoup(response.content, 'html.parser')
    status_elem = soup.find('div', {'class': 'table-cell-value tm-value tm-status-unavail'}) or soup.find('div', {
        'class': 'table-cell-value tm-value tm-status-avail'}) or soup.find('div', {
        'class': 'table-cell-value tm-value tm-status-taken'})
    if status_elem:
        if 'tm-status-unavail' in status_elem.get('class'):
            if 'Unavailable' in status_elem.text.strip():
                availability = 'Свободный'
            elif 'Sold' in status_elem.text.strip():
                availability = 'Продан'
        elif 'tm-status-taken' in status_elem.get('class'):
            if 'Taken' in status_elem.text.strip():
                availability = 'Занят'
        elif 'tm-status-avail' in status_elem.get('class'):
            if 'Available' in status_elem.text.strip():
                availability = 'На аукционе'

    response = requests.get(f'https://fragment.com/?query={x}')
    soup = BeautifulSoup(response.content, 'html.parser')
    price_elem = soup.select('div.table-cell-value.tm-value')

    for z in price_elem:
        if z.text not in ['Unknown', 'Taken', 'Available', 'Sold', 'Unavailable']:
            price = z.text
            if price is not None and price.isdigit():
                price = int(price)
            elif price.startswith('@'):
                price = None

    return price, availability, price_elem

for Username in Usernames:
    a = get_price_and_availability(Username)
    price = a[0]
    availability = a[1]
    price_elem = a[2]
    if price_elem is not None:
        print(f'Username: {Username} {availability}\n{price} TON')
    else:
        print(f'Username: {Username} {availability}\n{price} TON')
