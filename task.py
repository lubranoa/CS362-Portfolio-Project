

def my_func():
    return "Hello World"


def my_datetime(num_sec):
    """
    takes an integer value that represents the number of
    seconds since the last epoch: Jan 1st 1970.
    takes num_sec and converts it to date and returns it
    as a string in format MM-DD-YYYY
    """
    if num_sec == 0:
        return "01-01-1970"

    post_epoch_days = num_sec // (3600 * 24)

    # -1 as placeholder for indexing
    days_in_month = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_before_month = [-1]
    days_before = 0
    for days_in in days_in_month[1:]:
        days_before_month.append(days_before)
        days_before += days_in

    days_goal_year = post_epoch_days + my_datetime_days_from_year(1971)
    days_400_years = my_datetime_days_from_year(401)
    days_100_years = my_datetime_days_from_year(101)
    days_4_years = my_datetime_days_from_year(5)

    # n represents offset in days
    n = days_goal_year - 1
    n400, n = divmod(n, days_400_years)
    curr_year = n400 * 400

    n100, n = divmod(n, days_100_years)

    n4, n = divmod(n, days_4_years)

    n1, n = divmod(n, 365)

    curr_year += n100 * 100 + n4 * 4 + n1

    leap_year = my_datetime_is_leap(curr_year)
    month = (n + 50) >> 5

    prior_days = days_before_month[month] + (month > 2 and leap_year)
    if prior_days > n:  # overshot month
        month -= 1
        prior_days -= days_in_month[month] + (month == 2 and leap_year) + 1
    elif leap_year:
        n += 1
    n -= prior_days

    curr_year = str(curr_year)
    month = str(month)
    if len(month) == 1:
        month = "0" + month
    n = str(n + 2)

    return month + "-" + n + "-" + curr_year


def my_datetime_is_leap(year):
    """return True if leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def my_datetime_days_from_year(year):
    """returns number of days before Jan 1 of given year"""
    year -= 1
    return year * 365 + (year // 4) - (year // 100) + (year // 400)


def my_datetime_days_in_month(year, month, days_arr):
    """returns the number of days in given month of given year"""
    if month == 2 and my_datetime_is_leap(year):
        return 29
    else:
        return days_arr[month]
