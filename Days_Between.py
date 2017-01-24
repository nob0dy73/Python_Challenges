from datetime import datetime, date, time

def days_diff(date1, date2):
    year1, month1, day1 = date1
    d1 = date(year1, month1, day1)
    year2, month2, day2 = date2
    d2 = date(year2, month2, day2)
    return abs((d2 - d1).days)
    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

