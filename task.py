# A program by Noah Calhoun, Alex Lubrano, and Dacin Titus
#
#

import string


def conv_num_int_helper(num_str):
    """
    Parses through string to verify integrity
    and check if value is negative.
    """
    symbols = [".", "-"]
    neg_found = 0
    for i in range(len(num_str)):
        # Handle base10 num
        num = num_str[i]
        # Check if not a number nor symbol
        if not num.isnumeric() and num not in symbols:
            return None
        if num == "-":
            if neg_found >= 1:
                return None
            else:
                neg_found += 1
    int_value = conv_num_str_to_int(num_str, neg_found)
    return int_value


def conv_num_str_to_int(num_str, neg_found):
    """
    Converts and returns a Base10 string
    as a base10 int
    """
    result = 0
    deci_found = 0
    deci_location = 0
    for char in num_str:
        if char == '.':
            deci_found = True
        elif char == '-':
            continue
        else:
            digit = ord(char) - ord('0')
            if deci_found:
                deci_location += 1
                result += digit / (10 ** deci_location)
            else:
                result = result * 10 + digit
    if neg_found:
        result *= -1

    return result


def conv_num_hex_helper(num_str):
    """
    Takes in a base16 string,
    Returns a base10 int
    """
    result = 0
    hex_index = len(num_str) - 1
    allowed_alph = ["0", "1", "2", "3", "4",
                    "5", "6", "7", "8", "9",
                    "A", "B", "C", "D", "E", "F"]
    # Iterate through string to convert
    #   base16 string to base10 int
    for i in range(len(num_str)):
        num = num_str[i]
        if i == 1 or i == 0:        # ignore 0x values in hex
            hex_index -= 1
            continue
        if num not in allowed_alph:
            return None
        # Convert hex vlaue to base10, add to total, and decrement hex_index
        else:
            value = allowed_alph.index(num)
            result += value * (16 ** hex_index)
            hex_index -= 1

    return result


def conv_num(num_str):
    """
    This function takes in a string, parses it for base10 or base16 input,
    then converts and returns it as a base 10 int.
    """
    hex_based = False
    int_based = False

    # Check if input is base16 or base10
    if num_str[0] == "0" and len(num_str) > 1 and num_str[1] == "x":
        hex_based = True
        hex_value = conv_num_hex_helper(num_str)
    else:
        int_based = True
        int_value = conv_num_int_helper(num_str)

    # Return None if hex or int conversion failed
    if hex_based and hex_value is None:
        return None
    if int_based and int_value is None:
        return None

    # Return converted values
    if int_based:
        return int_value
    elif hex_based:
        return hex_value
    else:
        return None
      

def conv_endian(num, endian='big'):
    """Converts an integer from base 10 to a hexadecimal string in
    either big or little endian byte order. Returns None if value for
    endian is incorrect.

    :param int num: A negative or positive integer
    :param str endian: A byte order, 'big' or 'little', defaults to 'big'
    :return: The converted hex number string in specified byte order
    :rtype: string or None
    """
    hex_str = string.digits + string.ascii_uppercase[0:6]  # '0123456789ABCDEF'
    char_stack = []

    if endian != 'big':
        return None

    out_str = '' if num >= 0 else '-'
    num = abs(num)

    # Get hex digit chars and append to char_stack
    if num == 0:
        char_stack.append(hex_str[num])
    while num != 0:
        modulo = num % 16
        char_stack.append(hex_str[modulo])
        num //= 16

    # Construct string
    if len(char_stack) % 2 != 0:
        out_str += '0'
    while len(char_stack) != 0:
        out_str += char_stack.pop()
        # Insert space between each pair of hex digits, unless none left
        if len(char_stack) > 0 and len(char_stack) % 2 == 0:
            out_str += ' '

    return out_str




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
