import datetime
import time
import logging
import pandas as pd

data = pd.read_json("json/text.json").to_dict() 

def get_datetime_text() -> bool:
    print('Введите дату в формате YYYY-MM-DD HH:MM')
    date_time_str = input() + ':00.000'
    strdate = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    if(strdate.year < 2001): raise ValueError('Year less than 2001')

    date_words = data["days"][str(strdate.day)] + " "
    date_words += data["months"][str(strdate.month)] + " "
    date_words += data["hours"][str(strdate.hour)] + " "
    date_words += data["helpers"]["hour2" if (strdate.hour == 1 or strdate.hour == 21) else "hour3" if (strdate.hour%10 in [2, 3, 4] and strdate.hour not in [12, 13, 14]) else "hour1"] + " "
    date_words += data["minutes"][str(strdate.minute)] + " "
    date_words += data["helpers"]["minute2" if (strdate.minute%10 == 1 and strdate.minute != 11) else "minute3" if (strdate.minute%10 in [2, 3, 4] and strdate.minute not in [12, 13, 14]) else "minute1"] + " "
    date_words += data["helpers"]["2000"] + " "
    date_words += data["years"][str(strdate.year%2000)] + " "
    date_words += data["helpers"]['year']

    print(date_words)

    return True

if __name__ == '__main__':
    start_time = time.time()
    get_datetime_text()
    logging.info(f"\tProgram execution time: {time.time() - start_time} seconds")