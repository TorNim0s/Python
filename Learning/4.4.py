import itertools

def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for min in range(60):
        yield min

def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hours in gen_hours():
        for minutes in gen_minutes():
            for seconds in gen_secs():
                time = "%02d:%02d:%02d" % (hours, minutes, seconds)
                yield time

def gen_years(start=2020):
    for count in itertools.count(start):
        yield count

def gen_months():
    for month in range(1,13):
        yield month

def gen_days(month, leap_year=True):
    days_false = (0,31,28,31,30,31,30,31,31,30,31,30,31)
    days_true = (0,31,29,31,30,31,30,31,31,30,31,30,31)
    if not (leap_year):
        for day in range(1,days_false[month] + 1):
            yield day
    else:
        for day in range(1, days_true[month] + 1):
            yield day

def gen_date():
    for years in gen_years():
        for month in gen_months():
            for days in gen_days(month, False):
                for gt in gen_time():
                    yield "%02d/%02d/%02d %s" % (years, month, days, gt)

for gd in gen_date():
    print(gd)
