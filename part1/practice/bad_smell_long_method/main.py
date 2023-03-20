# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`
from operator import itemgetter

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list(csv):
    list_data = _read(csv)
    sorted_list = _sort(list_data)
    filtered_list = _filter(sorted_list)
    return filtered_list

def _read(csv):
    return [data.split(";") for data in csv.split('\n')]

def _sort(list_data, reverse=True):
    return sorted(list_data, key=itemgetter(1), reverse=reverse)

def _filter(list_data):
    return [user for user in list_data if int(user[-1]) >= 10]


if __name__ == '__main__':
    print(get_users_list(csv))


