# %%
def time_func(value):
    second = int(value)

    minute = hour = day = month = year = 0
    
    if (second > 60):
        minute = second//60
        second = second%60
        if (minute > 60):
            hour = minute//60
            minute = minute%60
            if (hour > 24):
                day = hour//24
                hour = hour%60
                if (day > 30):
                    month = day//30
                    day = day%30
                    if (month > 12):
                        year = month//12
                        month = month%12
    
    print("{} year {} month {} day {} minute {} second".format(year, month, day, minute, second))


# %%
value = 1610869309116
value //= 1000
time_func(value)

# %%
