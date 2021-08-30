from re import sub
from typing import List


def parse_money_str(money_str: str) -> float:
    if not money_str:
        return None

    return float(sub(r'[^\d.]', '', money_str))


fruits_list = ['banana', 'orange', 'apple', 'strawberry']
vegetables_list = ['cucumber',  'beetroot', 'celery', 'carrot']


def filter_fruits(foods: List[str]) -> List[str]:
    return [food for food in foods if food in fruits_list]


def filter_vegetables(foods: List[str]) -> List[str]:
    return [food for food in foods if food in vegetables_list]


def common_section(arr: List) -> List:
    common = arr[0]
    for item in arr[1:]:
        common = set(common).intersection(item)

    return common
