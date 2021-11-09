import re

date_regex = r'(?P<year>\d{2})/(?P<month>[a-zA-Z]{3})/(?P<day>\d{4})'
regex_time = r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})'
regex_time_2 = r'(?P<hour>\d{2}):(?P<minute>\d{2})'


def get_lines():
    file1 = open('access.log', 'r')
    lines = file1.readlines()
    objects = []
    for row in lines:
        splited = re.split(r'\s\s\s-\s', row)
        full_date = re.split(r'\s', splited[0])
        date = re.match(date_regex, full_date[0]).groupdict()
        time = re.match(regex_time, full_date[1]).groupdict()
        full_info = re.split(r';|:|::|;;', splited[1])
        name = full_info[0]
        full_action = re.split(r'\n', full_info[1])
        action = full_action[0]
        objects.append({'date': date, 'time': time, 'name': name, 'action': action})
    return objects


# dates have to be hh:mm
def get_users_logged_between_dates(date_from, date_to):
    date_from_reg = re.match(regex_time_2, date_from).groupdict()
    date_to_reg = re.match(regex_time_2, date_to).groupdict()
    hour_from = int(date_from_reg['hour'])
    minute_from = int(date_from_reg['minute'])
    hour_to = int(date_to_reg['hour'])
    minute_to = int(date_to_reg['minute'])
    names = []
    lines = get_lines()
    for line in lines:
        time = line['time']
        hour = int(time['hour'])
        minute = int(time['minute'])
        if line['action'] == ' Login':
            if hour_from <= hour <= hour_to:
                if hour_from == hour_to:
                    if minute_from <= minute <= minute_to:
                        names.append(line['name'])
                elif hour_from == hour:
                    if minute >= minute_from:
                        names.append(line['name'])
                elif hour_to == hour:
                    if minute <= minute_from:
                        names.append(line['name'])
    return names


# dates have to be hh:mm
def get_reports_between_dates(date_from, date_to):
    date_from_reg = re.match(regex_time_2, date_from).groupdict()
    date_to_reg = re.match(regex_time_2, date_to).groupdict()
    hour_from = int(date_from_reg['hour'])
    minute_from = int(date_from_reg['minute'])
    hour_to = int(date_to_reg['hour'])
    minute_to = int(date_to_reg['minute'])
    reports = []
    lines = get_lines()
    for line in lines:
        time = line['time']
        hour = int(time['hour'])
        minute = int(time['minute'])
        if 'Report' in line['name']:
            if not not line['action'].strip():
                if hour_from <= hour <= hour_to:
                    if hour_from == hour_to:
                        if minute_from <= minute <= minute_to:
                            reports.append(line['name'])
                    elif hour_from == hour:
                        if minute >= minute_from:
                            reports.append(line['name'])
                    elif hour_to == hour:
                        if minute <= minute_from:
                            reports.append(line['name'])
    return reports


def get_failed_logged_between_dates(date_from, date_to):
    date_from_reg = re.match(regex_time_2, date_from).groupdict()
    date_to_reg = re.match(regex_time_2, date_to).groupdict()
    hour_from = int(date_from_reg['hour'])
    minute_from = int(date_from_reg['minute'])
    hour_to = int(date_to_reg['hour'])
    minute_to = int(date_to_reg['minute'])
    names = []
    lines = get_lines()
    for line in lines:
        time = line['time']
        hour = int(time['hour'])
        minute = int(time['minute'])
        if line['action'] == ' LoginPage':
            if hour_from <= hour <= hour_to:
                if hour_from == hour_to:
                    if minute_from <= minute <= minute_to:
                        names.append(line['time'])
                elif hour_from == hour:
                    if minute >= minute_from:
                        names.append(line['time'])
                elif hour_to == hour:
                    if minute <= minute_from:
                        names.append(line['time'])
    return names


def get_action_for_user_between_dates(date_from, date_to, user):
    date_from_reg = re.match(regex_time_2, date_from).groupdict()
    date_to_reg = re.match(regex_time_2, date_to).groupdict()
    hour_from = int(date_from_reg['hour'])
    minute_from = int(date_from_reg['minute'])
    hour_to = int(date_to_reg['hour'])
    minute_to = int(date_to_reg['minute'])
    names = []
    lines = get_lines()
    for line in lines:
        time = line['time']
        hour = int(time['hour'])
        minute = int(time['minute'])
        if line['name'] == user:
            if hour_from <= hour <= hour_to:
                if hour_from == hour_to:
                    if minute_from <= minute <= minute_to:
                        names.append(line['action'])
                elif hour_from == hour:
                    if minute >= minute_from:
                        names.append(line['action'])
                elif hour_to == hour:
                    if minute <= minute_from:
                        names.append(line['action'])
    return names


print(get_users_logged_between_dates('08:00', '08:35'))
print(get_reports_between_dates('08:00', '10:35'))
print(get_failed_logged_between_dates('08:00', '09:35'))
print(get_action_for_user_between_dates('08:00', '09:35', 'Juan Alberto Casimiro'))