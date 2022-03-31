work_schedules = {
    '40Hours_Week': [
        ['Monday', (8,12)],# Monday Morning Half 8am-12pm
        ['Monday', (13,17)],# Monday Afternoon Half 1-5pm
        ['Tuesday', (8,12)],
        ['Tuesday', (13,17)],
        ['Wednesday', (8,12)],
        ['Wednesday', (13,17)],
        ['Thursday', (8,12)],
        ['Thursday',(13,17)],
        ['Friday',(8,12)],
        ['Friday',(13,17)],
    ],
    '20Hours_Morning': [
        ['Monday', (8,12)],
        ['Tuesday', (8,12)],
        ['Wednesday', (8,12)],
        ['Thursday', (8,12)],
        ['Friday',(8,12)],
    ],
    '16Hours_Weekend': [
        ['Saturday', (8,12)],
        ['Saturday', (13,17)],
        ['Sunday', (8,12)],
        ['Sunday', (13,17)],
    ],
}

employees = {
    'Mark Watney': '40Hours_Week',
    'Rocky Balboa': '20Hours_Morning',
    'Tommy Pickles': '16Hours_Weekend',
}

example_input = [{
        'employee': 'Mark Watney',
        'start_day': 'Tuesday',
        'start_hour': 14, # 2pm
        'task_duration': 12
    },
]

for input in example_input:
    schedule_key = employees[input['employee']]
    work_schedule_list = work_schedules[schedule_key]

    start_hour = input['start_hour']
    task_duration = input['task_duration']
    start_day = input['start_day']

    for w_schedule in work_schedule_list:
        current_day = w_schedule[0]
        current_range = w_schedule[1]

        if current_day == start_day:
            print(w_schedule)