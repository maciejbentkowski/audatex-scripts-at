import pandas as pd
import numpy as np
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

def strange_characters_replace(pricefile):
    strange_characters_dictionary = {
        ')': '',
        '(': '',
        'a': 'A',
        'А': 'A',
        'б': 'B',
        'b': 'B',
        'в': 'B',
        'с': 'C',
        'C': 'C',
        'д': 'D',
        'Д': 'D',
        'd': 'D',
        'E': 'E',
        'э': 'E',
        'е': 'E',
        'f': 'F',
        'ф': 'F',
        'H': 'H',
        'н': 'H',
        'к': 'K',
        'k': 'K',
        'К': 'K',
        'р': 'P',
        'Р': 'P',
        'п': 'P',
        'П': 'P',
        'т': 'T',
        'Т': 'T',
        't': 'T',
        '0': '0',
        'g': 'G',
        'и': 'I',
        'j': 'J',
        'l': 'L',
        'м': 'M',
        'М': 'M',
        'n': 'N',
        'о': 'O',
        'О': 'O',
        'q': 'Q',
        'л': 'L',
        'y': 'Y',
        'У': 'Y',
        'u': 'U',
        'Г': 'G',
        'Ч': 'C',
        'Ш': 'Z',
        'З': 'Z',
        'Ж': 'Z',
        'Ą': 'A',
        'Ć': 'C',
        'Ź': 'Z',
        'Ę': 'E',
        'Ń': 'N',
        ';': '.',
        "'": '.',
        '+': '-',
        '-': '',
        '&' : '',
    }
    if isinstance(pricefile, pd.DataFrame):
        pricefile['pn'] = pricefile['pn'].str.translate(str.maketrans(strange_characters_dictionary))
    return pricefile


def drop_duplicates(pricefile):
    if isinstance(pricefile, pd.DataFrame):
        pricefile = pricefile.sort_values('price', ascending=False)
        pricefile.drop_duplicates(subset=['pn'], keep='first', inplace=True)
    return pricefile


def generate_txt_file(pricefile, filename):
    pricefile['price'] = pricefile['price'].str.replace(',', '.').astype(float)
    with open(filename, 'w') as file:
        write_todays_date(file)
#        file.write('pn;price\n')
        for _, row in pricefile.iterrows():

            pn = str(row['pn'])
            price = str(row['price'])
            blank = 50 - (len(pn))
            price = "{:.2f}".format(row['price']).replace('.', ',')
#            file.write(f"{pn};{price}\n")
            file.write(f"{pn}{price:>{blank}}\n")



                
def write_todays_date(file):
    today = date.today()
    today = today.strftime("%d.%m.%Y")
    file.write(f'PriceL{today}'+ (" "*30) +"9,99\n")