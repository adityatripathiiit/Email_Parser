import datefinder
import re
string_with_dates = '23 January 2019 to 26 december 2019'
matches = datefinder.find_dates(string_with_dates)
for match in matches:
    s=str(match)[:11]
    print(s)