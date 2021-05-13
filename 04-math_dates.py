import unittest
import datetime
from datetime import timedelta, date


class DateMath:
    """Use timedelta function to do simple math with days from a date"""
    def add_days(given_date):
        """Add 20 days to the date 2021-12-01"""
        return given_date + datetime.timedelta(days=20)

    def minus_days(given_date):
        """Minus 20 days from the date 2021-12-01"""
        return given_date - datetime.timedelta(days=20)


class TestDateMath(unittest.TestCase):
    """Test timedelta function to confirm expected resulting dates"""
    def test_add_days(self):
        """Confirm that the result of adding 20 days returned 2021-12-21"""
        self.assertEqual(
            DateMath.add_days(date(2021, 12, 1)),
            datetime.date(2021, 12, 21))

    def test_minus_days(self):
        """Confirm that the result of taking away 20 days returned 2021-11-11"""
        self.assertEqual(
            DateMath.minus_days(date(2021, 12, 1)),
            datetime.date(2021, 11, 11))

if __name__ == '__main__':
    # Print result of adding days to a date
    print('Adding 20 days to 2021-12-01 should result in',
          DateMath.add_days(date(2021, 12, 1)))

    # Print result of subtracting days from a date
    print('Subtracting 20 days from 2021-12-01 should result in',
          DateMath.minus_days(date(2021, 12, 1)))

    # Display unittest results
    print('\nUnittest Results:')
    unittest.main(verbosity=2)
