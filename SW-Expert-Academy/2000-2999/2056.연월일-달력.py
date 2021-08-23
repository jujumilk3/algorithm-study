case_count = int(input())

for i in range(1, case_count + 1):
    datetime = input()
    status = True
    result = -1
    year = datetime[0:4]
    month = datetime[4:6]
    day = datetime[6:8]

    day_to_be = ''
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        day_to_be = '31'
    elif month in ['04', '06', '09', '11']:
        day_to_be = '30'
    elif month == '02':
        day_to_be = '28'
    else:
        status = False

    if status:
        if day > day_to_be:
            status = False
    result = -1 if status is False else year + '/' + month + '/' + day

    print('#{} {}'.format(i, result))

"""
5
22220228
20150002
01010101
20140230
11111111
"""
