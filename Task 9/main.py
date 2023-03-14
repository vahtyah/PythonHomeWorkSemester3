def main(data):
    unique_data = []
    for row in data:
        unique_cols = {}
        for elem in row:
            unique_cols[elem] = "True"
        unique_data.append([key for key in unique_cols])
    unique_rows = []
    for row in unique_data:
        if row not in unique_rows:
            unique_rows.append(row)
    emails = []
    status = []
    names = []
    scores = []
    for item in unique_rows:
        email = item[0]
        emails.append(email.split('@')[0])
        status.append('Да' if item[1] == 'да' else 'Нет')
        name_parts = item[2].split()
        first_name = name_parts[1][0] + '.'
        last_name = name_parts[2]
        patronymic = name_parts[0][0] + '.' if len(name_parts) > 2 else ''
        names.append(f"{patronymic}{first_name} {last_name}")
        scores.append('{:.2f}'.format(round(float(item[3]), 2)))
    return [emails, status, names, scores]


data = [['razecov25@rambler.ru', 'нет', 'Макар Ш. Рацечов', '0.799', '0.799'], ['fubskij33@rambler.ru', 'нет', 'Кирилл Г. Фубский', '0.147', '0.147'], ['valerij14@yahoo.com', 'нет', 'Валерий С. Небев', '0.180', '0.180'], ['ganamberg34@yandex.ru', 'да', 'Макар А. Ганамберг', '0.090', '0.090'], ['ganamberg34@yandex.ru', 'да', 'Макар А. Ганамберг', '0.090', '0.090']]

result = main(data)
print(result)
