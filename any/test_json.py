import json
import vk

import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_convert_json(json_content):
    if json_content:
        return json.dumps(json_content, ensure_ascii=False, sort_keys=True, indent=4)


def pretty_print_json(json_content):
    if json_content is None:
        print('The file is empty or does not exist.')
    else:
        print(json_content)

def dict_to_json(s):
    if s:
     return json.dumps(s, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    s = {'admin': {'Category': {'create': True, 'fields': ['name', 'category_type']}, 'User': {'fields': ['first_name', 'last_name', {'categories': {'fields': ['name']}}], 'read_only': ['categories']}}}
    print(dict_to_json(s))
    pass

    # file_path = input('Введите путь к файлу в формате json: \n')
    # convert_json_content = pretty_convert_json(load_data(file_path))
    # pretty_print_json(convert_json_content)

