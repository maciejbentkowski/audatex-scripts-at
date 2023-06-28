from modules.script_helpers import *


pricefile = 'ford_at.txt'

cols = ['pn', 'ss', 'price', 'cuntry_tag']
df = pd.read_fwf(pricefile, colspecs=([1,8], [46,53], [53,65], [30,31]),names=cols, skiprows=1)
df = df.drop(df[df['cuntry_tag'] != 'A'].index)

df = clear_ss_while_there_is_no_equivalent_pn(df)
df = strange_characters_replace(df)
df = drop_pn_null_values(df)
df = delete_string_price_rows(df, 'KEIN PREIS')
df = blank_ss_while_same_as_pn(df)
df = delete_zero_price_rows(df)
df = delete_empty_price_rows(df)

df = remove_chain_without_price(df)
generate_txt_file(df, 'output.txt')