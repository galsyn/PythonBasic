time_lst = []
tup_234 = ("2", "3", "4")
div = {"minutes": 60, "hours": 60 * 60, "days": 24 * 60 * 60}
user_number = input('Input number from 0 to 8 640 000: ')
if user_number.isdigit():
    user_number = int(user_number)
    if user_number < 8_640_000:
        days, hours = divmod(user_number, div["days"])
        if str(days).endswith("1") and not str(days).endswith("11"):
            day_str = "день"
        elif str(days).endswith(tup_234) and not str(days).endswith(("12", "13", "14")):
            day_str = "дні"
        else:
            day_str = "днів"
        day_str += ','
        hours, minutes = divmod(hours,  div["hours"])
        time_lst.append(str(hours).zfill(2))
        minutes, seconds = divmod(minutes,  div["minutes"])
        time_lst.append(str(minutes).zfill(2))
        time_lst.append(str(seconds).zfill(2))
        print(days, day_str, ":".join(time_lst))
    else:
        print('You input incorrect number!', user_number)
else:
    print('You don\'t input a number! ')
