"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам,
представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок.
"""

from tabulate import tabulate
from task_2 import host_range_ping


def host_range_ping_tab():
    """
        Requesting a range of ip addresses, checking their availability, displaying the results in a table
        :param
        :return:
    """
    res_dict = host_range_ping(True) 
    print()
    print(tabulate([res_dict], headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == "__main__":
    host_range_ping_tab()
