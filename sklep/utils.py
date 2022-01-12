from mysql.connector import FieldType

def convert_types(mysql_rows: list):
    return [tuple(str(item) for item in row) for row in mysql_rows]


def pretty_print(description,
                 rows: list,
                 regular_col_width=15,
                 extended_col_width=35,
                 end = '\n'):
    col_width = []
    for id, desc in enumerate(description):
        if FieldType.get_info(desc[1]) == 'VAR_STRING':
            col_width.append(extended_col_width)
        else:
            col_width.append(regular_col_width)
        print(desc[0].ljust(col_width[id]), end='')
    line = '_' * sum(col_width)
    print('\n', line)
    for row in rows:
        for col_id, value in enumerate(row):
            value_size = len(value)
            preferable_size = col_width[col_id] - (extended_col_width // 10)
            if value_size > preferable_size:
                value_size = preferable_size
            value = value[:value_size]
            print(value.ljust(col_width[col_id]), end='')
        print()
    print(end=end)
