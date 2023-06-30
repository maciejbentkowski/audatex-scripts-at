import pandas as pd
import numpy as np
from datetime import date
from decimal import Decimal, ROUND_HALF_UP



def delete_zero_price_rows(pricefile):
    pricefile['price'] = pricefile['price'].astype(float)
    pricefile = pricefile[~(pricefile['price'] == 0.00)].reset_index(drop=True)
    pricefile['price'] = pricefile['price'].astype(float)
    return pricefile



def generate_txt_file(pricefile, filename):
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