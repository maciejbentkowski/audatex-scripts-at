import suzuki_script_helpers as helpers
import pandas as pd

# Function for creating sample data frames
def data_frame_creator(data, correct_data):
    sample_df = pd.DataFrame(data, columns=['pn','price'])
    correct_df = pd.DataFrame(correct_data, columns=['pn','price'])
    return sample_df, correct_df


def test_strange_characters_replace():
    data = (['9AIRCON-MAILER', 0.01],
            ['9BER00-17431-900', 0.10],
            ['0BPZ8H-N-10', 10.09],
            ['0B&Z623R43', 754.09])
    correct_data = (['9AIRCONMAILER', 0.01],
                    ['9BER0017431900', 0.10],
                    ['0BPZ8HN10', 10.09],
                    ['0BZ623R43', 754.09])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.strange_characters_replace(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)


def test_drop_duplicates():
    data = (['0BPMR7A', 45.01],
            ['952423NMD34', 23.10],
            ['0BPMR7A', 0.01],
            ['9BPSZ045T0', 10.09])
    correct_data = (['0BPMR7A', 45.01],
                    ['952423NMD34', 23.10],
                    ['9BPSZ045T0', 10.09])
    sample_df, correct_df = data_frame_creator(data, correct_data)
    sample_df = helpers.drop_duplicates(sample_df)
    print(sample_df)
    pd.testing.assert_frame_equal(sample_df, correct_df)
