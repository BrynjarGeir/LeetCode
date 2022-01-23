class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def daysSince1971(date: str) -> int:
            year, month, day = date.split('-')
            year = int(year); month = int(month)-1; day = int(day)
            if (year % 400 == 0 and (year/100).is_integer()) or (not (year/100).is_integer() and year % 4 == 0):
                isLeapYear = True
            else: isLeapYear = False
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if isLeapYear: months[1] += 1
            dayOfYear = 0
            for i in range(month):
                dayOfYear += months[i]
            dayOfYear += day
            days = 0
            for y in range(1971,year):
                if (y % 400 == 0 and (y/100).is_integer()) or (not (y/100).is_integer() and y % 4 == 0):
                    days += 366
                else:
                    days += 365
            return dayOfYear + days
        days1 = daysSince1971(date1); days2 = daysSince1971(date2)
        return abs(days1 - days2)
        