import unittest
from langdt import get_timeframe


class TestLangDT(unittest.TestCase):
    def test_langdt(self):
        # Testing the function with the provided examples
        test_cases = [
            "all", "recent", "yesterday", "since last month", "this week",
            "last 20 minutes", "last year", "last 2 years", "last month", "last 5 weeks", "last hour",
            "from 2022-10-10 to 2025-10-10T00:30:11",
            "from 2022 to 2025",
            "from Nov 2nd 2023 to Nov 5th 2025",
            "365D", "1W", "1M", "1Y", "1H",
        ]

        for test_case in test_cases:
            print(test_case)
            print(get_timeframe(test_case))
        pass