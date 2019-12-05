import pandas as pd
import gc

"""Create separate csv file with formatted logs sample"""
with open('data/tbird2.csv', 'r', newline='') as file:
    array = file.readlines()
    splt_char = ' '
    temp = [row.split(splt_char) for row in array]

    del array
    gc.collect()

    first_vars = [splt_char.join(row[:9]) for row in temp]
    first_vars = [row.split(splt_char) for row in first_vars]
    last_vars = [splt_char.join(row[9:]) for row in temp]

    del temp
    gc.collect()

    for first, last in zip(first_vars, last_vars):
        first[0] = first[0].lstrip('\"') # remove extra quotes
        first.append(last.rstrip('\r\n')) # remove trailing character from log messages

    df = pd.DataFrame(first_vars,
                      columns=["alert_class", "message_id", "IP", "host_name", "month", "day", "time", "host_privilege",
                               "app_name", "message"])
    df.to_csv('data/tbird2_sample.csv', index=None)
