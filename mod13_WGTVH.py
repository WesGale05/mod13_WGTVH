import unittest
from datetime import datetime
class StockData:

    def ver_stock_symbol(self, symbol): # capitalized, 1-7 alpha characters

        if(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7):
            return True
        else:
            return False
        # # enter stock symbol
        # while(stock_symbol == ""):
        #     #prompt for input
        #     symbol_input = input("Enter Stock Symbol: ")
        #     return symbol_input

    def ver_chart_type(self, chart_type):
        if(chart_type == 1 or chart_type == 2):
            return True
        else:
            return False
        # chart_type = 0
        # enter chart type
        # print("\nChart Types")
        # print("-----------")
        # print("1. Bar \n2. Line")
        # while(chart_type == 0):
        #         #prompt for chart type
        #     chart_input = input("\nEnter the chart type you want (1,2): ")
        #         #validate input
        #     if (chart_input == "1"):
        #         chart_type = 1
        #         print("bar graph")
        #     elif (chart_input == "2"):
        #         chart_type = 2
        #         print("line graph")
        #     else:
        #         print("Please select a valid option.")

    def get_time_series(self, time_series):
        if(1 <= time_series <= 4):
            return True
        else:
            return False
        # time_series = ""
        # # enter a valid time series type
        # print("\nSelect the Time Series of the chart you want to generate")
        # print("-----------")
        # print("1. Intraday \n2. Daily \n3. Weekly\n 4. Monthly")
        # # loops until the user enters a valid choice, with an error catch incase a random unexpected value is entered
        # while True:
        #     try:
        #         user_choice = int(input("\nEnter time series option (1, 2, 3, 4):"))
        #         if user_choice == 1:
        #             time_series = "TIME_SERIES_INTRADAY"
        #             return time_series
        #         elif user_choice == 2:
        #             time_series = "TIME_SERIES_DAILY"
        #             return time_series
        #         elif user_choice == 3:
        #             time_series = "TIME_SERIES_WEEKLY"
        #             return time_series
        #         elif user_choice == 4:
        #             time_series = "TIME_SERIES_MONTHLY"
        #             return time_series
        #         else:
        #             print("A valid option must be selected!")
        #     except ValueError as exc:
        #         print("Fatal Error: Invalid input!")
        #         return
            
    def ver_start_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        # print("Select desired time period")
        # print("-----------")
        # startDate = input('Enter the start date (YYYY-MM-DD): ')
        # endDate = input('Enter the end date (YYYY-MM-DD): ')
    def ver_end_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

class TestStockData(unittest.TestCase):
    def setUp(self):
        self.calc = StockData()
    def test_add(self):
        self.assertEqual(self.calc.ver_stock_symbol('M'), True)
        self.assertEqual(self.calc.ver_stock_symbol('54R'), False)
        self.assertEqual(self.calc.ver_stock_symbol('goog'), False)
    def test__chartType(self):
        self.assertEqual(self.calc.ver_chart_type(1), True)
        self.assertEqual(self.calc.ver_chart_type(2), True)
        self.assertEqual(self.calc.ver_chart_type(5), False)
    def test_time_series(self):
        self.assertEqual(self.calc.get_time_series(2), True)
        self.assertEqual(self.calc.get_time_series(3), True)
        self.assertEqual(self.calc.get_time_series(6), False)
    def test_dates(self):
        self.assertEqual(self.calc.ver_start_date('2023-02-15'), True)
        self.assertEqual(self.calc.ver_end_date('2022-11-25'), True)
        self.assertEqual(self.calc.ver_end_date('09-15-2025'), False)
        self.assertEqual(self.calc.ver_start_date('30d2-02-15'), False)




if __name__ == '__main__':
    unittest.main()
