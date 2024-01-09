import datetime
import pandas as pd

yearToday = int(datetime.datetime.now().year)
monthToday = int(datetime.datetime.now().month)
dateToday = int(datetime.datetime.now().day)

daysToChrismas = pd.Timestamp(2024, 6, 22).dayofyear
dayToday = pd.Timestamp(yearToday, monthToday, dateToday).dayofyear

if dayToday > daysToChrismas:
    print(f'Det er {daysToChrismas + (pd.Timestamp(yearToday + 1, 12, 31).dayofyear - dayToday)} dager til jul')
elif dayToday < daysToChrismas:
    print(f'Det er {daysToChrismas - dayToday} dager til sommerferie')
