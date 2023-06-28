import ford_script_helpers as helpers
import pandas as pd

# Function for creating sample data frames
def data_frame_creator(data, correct_data):
    sample_df = pd.DataFrame(data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    correct_df = pd.DataFrame(correct_data, columns=['pn', 'ss', 'price', 'cuntry_tag'])
    return sample_df, correct_df



# TEST FOR PN 

def test_strange_characters_replace():
    data = (['0д00001', '', 0.18, 'A'],
            ['000э004', '', 0.10, 'A'],
            ['00000g5', '', 0.09, 'A'],
            ['Ж000006', '', 0.07, 'A'],
            ['0000007', '', 0.35, 'A'])
    correct_data = (['0D00001', '', 0.18, 'A'],
                    ['000E004', '', 0.10, 'A'],
                    ['00000G5', '', 0.09, 'A'],
                    ['Z000006', '', 0.07, 'A'],
                    ['0000007', '', 0.35, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    pd.testing.assert_frame_equal(helpers.strange_characters_replace(sample_df), correct_df)

def test_drop_pn_null_values():
    data = ([None, '', 0.18, 'A'],
            ['5320004', '', 0.10, 'A'],
            [None, '', 8.24, 'A'],
            ['6230005', '', 0.09, 'A'],
            [None, '', 1.24, 'A'],
            ['7650006', '', 0.07, 'A'])
    correct_data = (['5320004', '', 0.10, 'A'],
                    ['6230005', '', 0.09, 'A'],
                    ['7650006', '', 0.07, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.drop_pn_null_values(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)

def test_delete_zero_price_rows():
    data = (['0003152', '0000314', None, 'A'],
            ['0000314', '', 0.10, 'A'],
            ['0007123', '', 0.09, 'A'],
            ['0000153', '', 0.00, 'A'],
            ['0050813', '', 0.00, 'A'],
            ['0000222', '0004352', None, 'A'],
            ['0004352', '', 51.53, 'A'],
            ['0000356', '', 0.00, 'A'],
            ['5310240', '', 0.00, 'A'])
    correct_data = (['0003152', '0000314', None, 'A'],
                    ['0000314', '', 0.10, 'A'],
                    ['0007123', '', 0.09, 'A'],
                    ['0000222', '0004352', None, 'A'],
                    ['0004352', '', 51.53, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.delete_zero_price_rows(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)

def test_remove_chain_without_price():

    data = (['0053243', '', 5.18, 'A'],
        ['0353004', '', 25.10, 'A'],
        ['0005234', '0032583', None, 'A'],
        ['0032583', '', 4.25, 'A'],
        ['0053432', '', 51.53, 'A'],
        ['0002222', '0589402', None, 'A'],
        ['0051561', '', 41.51, 'A'],
        ['0589402', '', 3.51, 'A'],
        ['0532432', '0768435', None, 'A'],
        ['0768435', '0712345', None, 'A'],
        ['0712345', '5477644', None, 'A'])
    

    correct_data = (['0053243', '', 5.18, 'A'],
            ['0353004', '', 25.10, 'A'],
            ['0005234', '0032583', None, 'A'],
            ['0032583', '', 4.25, 'A'],
            ['0053432', '', 51.53, 'A'],
            ['0002222', '0589402', None, 'A'],
            ['0051561', '', 41.51, 'A'],
            ['0589402', '', 3.51, 'A'])

    sample_df, correct_df = data_frame_creator(data, correct_data)
    print(sample_df)
    sample_df = helpers.remove_chain_without_price(sample_df)
    print(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)

def test_blank_ss_while_same_as_pn():
    data = (['0532144', '0532144', 15.18, 'A'],
            ['0352314', '', 5.10, 'A'],
            ['0421251', '0421251', 26.09, 'A'],
            ['5242612', '', 62.07, 'A'])
    correct_data = (['0532144', '', 15.18, 'A'],
                    ['0352314', '', 5.10, 'A'],
                    ['0421251', '', 26.09, 'A'],
                    ['5242612', '', 62.07, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.blank_ss_while_same_as_pn(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)

def test_delete_empty_price_rows():
    data = (['5234123', '', None, 'A'],
            ['7643245', '', 256.11, 'A'],
            ['5421324', '8567189', None, 'A'],
            ['8567189', '', 512.00, 'A'])

    correct_data = (['7643245', '', 256.11, 'A'],
                    ['5421324', '8567189', None, 'A'],
                    ['8567189', '', 512.00, 'A'])

    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.delete_empty_price_rows(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)

def test_delete_string_price_rows():
    data = (['5217123', '', 'no price', 'A'],
            ['6213421', '', 51.66, 'A'],
            ['6431245', '', 78.51, 'A'],
            ['1234653', '', 145.07, 'A'],
            ['7532467', '', 'no price', 'A'])
    correct_data = (['6213421', '', 51.66, 'A'],
                    ['6431245', '', 78.51, 'A'],
                    ['1234653', '', 145.07, 'A'])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.delete_string_price_rows(sample_df, 'no price')
    pd.testing.assert_frame_equal(sample_df, correct_df, check_dtype=False)

