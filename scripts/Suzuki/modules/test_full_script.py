import script_helpers as helpers
import pandas as pd

def data_frame_creator(data, correct_data):
    sample_df = pd.DataFrame(data, columns=['pn', 'price'])
    correct_sample_df = pd.DataFrame(correct_data, columns=['pn','price'])
    return sample_df, correct_sample_df


def test_full_ford_at_script():
    data = (['9AIRCON-MAILER', 0.01],
            ['9BER00-17431-900', 0.10],
            ['0BPZ8H-N-10', 10.09])
    
    correct_data = (['9AIRCONMAILER', 0.01],
                    ['9BER0017431900', 0.10],
                    ['0BPZ8HN10', 10.09])
    

    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.strange_characters_replace(sample_df)
    
    pd.testing.assert_frame_equal(sample_df, correct_df)

