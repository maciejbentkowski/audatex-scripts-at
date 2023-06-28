from modules.suzuki_script_helpers import *
pricefile = 'suzuki_at.txt'

cols = ['pn', 'price']
df = pd.read_fwf(pricefile, colspecs=([1,16], [47,57]),names=cols, encoding= 'utf-8')

df = strange_characters_replace(df)
print(df.shape[0])
df = drop_duplicates(df)
print(df.shape[0])

df = generate_txt_file(df, 'output.txt')