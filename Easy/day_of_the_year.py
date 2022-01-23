class Solution:
    def dayOfYear(self, date: str) -> int:
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
        return dayOfYear