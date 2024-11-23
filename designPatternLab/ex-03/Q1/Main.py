
from Difference import Difference
from Validity import Validity
from Convert import Convert
from Date import Date

# Date functionalities
date = Date()
print(date.currentDate()) # Output: Current date in dd-mm-yyyy format
print(date.currentDateFormatMDY()) # Output: Current date in mm-dd-yyyy format
print(date.currentTime()) # Output: Current time in hh:mm:ss format
print(date.currentDatestr()) # Output: Current date in 'Month Day, Year' format

# Conversion functionalities
convert = Convert()
print(convert.convert_hrs_days(48)) # Output: 2.0 (days)
print(convert.convert_days_hours(2)) # Output: 48 (hours)
print(convert.convert_man_hrs_days(16)) # Output: 2.0 (man-days)

# Validity check functionalities
validity = Validity()
print(validity.is_valid_time('12:00:00')) # Output: True
print(validity.is_valid_date('2024-08-28')) # Output: True

# Date difference functionalities
difference = Difference()
print(difference.difference_with_current('2024-08-28')) # Output: Number of days between current date and '2024-08-28'
print(difference.difference('2024-08-28', '2024-08-30')) # Output: 2
print(difference.days_after(2)) # Output: Date 2 days after current date
print(difference.days_before(2)) # Output: Date 2 days before current date
print(difference.month_after(1)) # Output: Date 1 month after current date
print(difference.month_before(1)) # Output: Date 1 month before current date
