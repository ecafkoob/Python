def format_duration(seconds):
    YEARS = 31536000
    DAYS = 86400
    HOURS = 3600
    MINS = 60
    if seconds % YEARS == 0:
        if int(seconds / YEARS) == 1:
            return '1 year'
        elif int(seconds / YEARS) == 0:
            return 'now'
        else:
            return str(int(seconds / YEARS)) + ' years'
    elif seconds > YEARS:
        year = int(seconds / YEARS // 1)
    else:
        year = 0
    print(year)
    if (seconds - YEARS * year) % DAYS == 0:
        if year==0:
            if int((seconds - YEARS * year) / DAYS // 1) == 1:
                return '1 day'
            else:
                return str(int((seconds - YEARS * year) / DAYS // 1)) + ' days'
        else:
            if int((seconds - YEARS * year) / DAYS // 1) == 1:
                return str(year)+'1 day'
            else:
                return str(int((seconds - YEARS * year) / DAYS // 1)) + ' days'
    elif (seconds - YEARS * year) > DAYS:
        day = int((seconds - YEARS * year) / DAYS // 1)
    else:
        day = 0
    print(day)
    if (seconds - YEARS * year - DAYS * day) % HOURS == 0:
        if year==0 and day==0:
            if int((seconds - YEARS * year - DAYS * day) / HOURS // 1) == 1:
                return '1 hour'
            else:
                return str(int((seconds - YEARS * year - DAYS * day) / HOURS // 1)) + ' hours'
        elif year==0 and day!=0:
            if int((seconds - YEARS * year - DAYS * day) / HOURS // 1) == 1:
                return str(day)+'1 hour'
            else:
                return str(day)+str(int((seconds - YEARS * year - DAYS * day) / HOURS // 1)) + ' hours'
        elif year!=0 and day==0:
            if int((seconds - YEARS * year - DAYS * day) / HOURS // 1) == 1:
                return str(year)+str(day) + '1 hour'
            else:
                return str(year)+str(day) + str(int((seconds - YEARS * year - DAYS * day) / HOURS // 1)) + ' hours'

    elif seconds - YEARS * year - DAYS * day > HOURS:
        hour = int((seconds - YEARS * year - DAYS * day) / HOURS // 1)
    else:
        hour = 0
    if (seconds - YEARS * year - DAYS * day - HOURS * hour) % MINS == 0:
        if year==0 and day==0 and hour==0:
            if int((seconds - YEARS * year - DAYS * day - HOURS * hour) / MINS // 1) == 1:
                return '1 minute'
            else:
                return str(int((seconds - YEARS * year - DAYS * day - HOURS * hour) / MINS // 1)) + ' minutes'
        else:
            if int((seconds - YEARS * year - DAYS * day - HOURS * hour) / MINS // 1) == 1:
                return str(year)+str(day)+str(hour)+'1 minute'
            else:
                return str(year)+' years, '+str(day)+' days, '+str(hour)+' hours and '+str(int((seconds - YEARS * year - DAYS * day - HOURS * hour) / MINS // 1)) + ' minutes'

    elif seconds - YEARS * year - DAYS * day - HOURS * hour > MINS:
        mins = int((seconds - YEARS * year - DAYS * day - HOURS * hour) / MINS // 1)
    else:
        mins = 0
    sec = seconds - YEARS * year - DAYS * day - HOURS * hour - MINS * mins
    if year == 0 | day == 0 | hour == 0 | mins == 0:
        if sec == 1:
            return str(sec) + ' second'
        else:
            return str(sec) + ' seconds'
    arr = [year, day, hour, mins, sec]
    sample = ['year, ', 'day, ', 'hour, ', 'minute and ', 'second']
    samples = ['years, ', 'days, ', 'hours, ', 'minutes and ', 'seconds']
    count = 0
    rearr = []
    for i in arr:
        if i == 1:
            string = str(i) + ' ' + sample[count]
            rearr.append(string)
            count += 1
        elif i > 1:
            string = str(i) + ' ' + samples[count]
            rearr.append(string)
            count += 1
        else:
            count += 1
    return ''.join(rearr)