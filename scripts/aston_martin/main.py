from modules.astonmartin_script_helpers import *


pricefile = 'astonmartin_at.csv'


df = pd.read_csv(pricefile,header = 0,names=['pn', 'price'], encoding='utf-8', usecols=[0,2])

df = delete_zero_price_rows(df)

print(df)

df = generate_txt_file(df, 'output.txt')