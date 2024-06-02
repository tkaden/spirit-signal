import unittest
import pandas as pd
from data import read_csv
from io import StringIO

class TestData(unittest.TestCase):

    def test_read_csv(self):
        test_csv = StringIO(
            "spirit,email,zipcode\n"
            "fortaleza,test@example.com,90210\n"
            "g4,example@test.com,10001"
        )
        expected_df = pd.DataFrame({
            "spirit": ["fortaleza", "g4"],
            "email": ["test@example.com", "example@test.com"],
            "zipcode": ["90210", "10001"]
        })

        result_df = read_csv(test_csv)
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == "__main__":
    unittest.main()
