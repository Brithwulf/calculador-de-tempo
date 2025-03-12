def add_time(start, duration, week_day=''):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    hours = list(range(1, 13))
    minutes = list(range(0, 60))
    hour_and_minute, period = start.split()
    start_hour, start_minute = hour_and_minute.split(':')

    duration_hour, duration_minute = duration.split(':')

    receive_hours = int(start_hour) + int(duration_hour)
    receive_minutes = int(start_minute) + int(duration_minute)
    calculate_hours = receive_hours

    if receive_minutes >= len(minutes):
        receive_minutes = receive_minutes - len(minutes)
        receive_hours += 1
    
    if receive_hours >= len(hours):
        calculate_period = int(receive_hours / 12)

    if receive_hours >= len(hours):
        calculate_period = receive_hours // 12
        if calculate_period % 2 != 0:
            period = 'PM' if period == 'AM' else 'AM'

    calculate_hours = receive_hours % 12 or 12

    days_passed = receive_hours // 24
    if period == 'AM' and receive_hours % 24 >= 12:
        days_passed +=1

    if week_day:
        week_day = week_day.capitalize()
        day_index = days.index(week_day)
        new_index = (day_index + days_passed) % len(days)
        calendar = days[new_index]
        day_string = f', {calendar}'
    else:
        day_string = ''

    if days_passed == 0:
        new_time = f'{calculate_hours}:{receive_minutes:02} {period}{day_string}'
    elif days_passed == 1:
        new_time = f'{calculate_hours}:{receive_minutes:02} {period}{day_string} (next day)'
    else:
        new_time = f'{calculate_hours}:{receive_minutes:02} {period}{day_string} ({round(days_passed)} days later)'

    return new_time

print(add_time('2:59 AM', '24:00'))
