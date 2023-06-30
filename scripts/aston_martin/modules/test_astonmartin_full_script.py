import astonmartin_script_helpers as helpers
import pandas as pd

def data_frame_creator(data, correct_data):
    sample_df = pd.DataFrame(data, columns=['pn', 'price'])
    correct_sample_df = pd.DataFrame(correct_data, columns=['pn','price'])
    return sample_df, correct_sample_df


def test_full_ford_at_script():
    data = (['00-27712', 0.05],
            ['002941', 0.00],
            ['01-75424-KIT', 56.09],
            ['78-123759-AA', 0.10],
            ['78-17327', 0.00],
            ['HY53-045K06-ACW', 0.00])
    
    correct_data = (['00-27712', 0.05],
                    ['01-75424-KIT', 56.09],
                    ['78-123759-AA', 0.10])
    

    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.delete_zero_price_rows(sample_df)


    print(sample_df)
    print(correct_df)
    
    pd.testing.assert_frame_equal(sample_df, correct_df)

