# coding=utf-8

symboltable_list = []
table_index = 0
current_scope = 0
constant_table = {}


def dprint(str, debug=0):
    if debug == 1:
        print(str)


class Content(object):
    def __init__(self, entry={}, data_type=0):
        self.truelist = []
        self.falselist = []
        self.nextlist = []
        self.continuelist = []
        self.breaklist = []
        self.addr = ''
        self.code = ''
        self.entry = entry
        self.data_type = data_type


def create_new_scope(table_index: int, current: int):
    dprint('create new scope with tableIndex={} and parent = {}'.format(table_index, current))
    table_index += 1
    symboltable_list[table_index] = {
        'symboltable': {},
        'parent': current,
    }
    return table_index


def exit_scope():
    if symboltable_list[current_scope]['parent'] == -1:
        return 0
    else:
        return symboltable_list[current_scope]['parent']


def create_entry(lexme: str, value: int, data_type: int):
    return {
        'lexme': lexme,
        'value': value,
        'parameter_list': [],
        'array_dimension': -1,
        'is_constant': 0,
        'num_params': 0,
        'data_type': data_type,
    }


def search(symboltable: dict, lexme: str):
    if lexme in symboltable:
        return symboltable[lexme]
    else:
        return None


def recursive_search(lexme: str, current: int):
    idx = current
    entry = None
    while idx != -1:
        entry = search(symboltable_list[idx]['symboltable'], lexme)
        dprint('search lexme={} in {}'.format(lexme, symboltable_list[idx]))
        dprint('result = {}'.format(entry))
        if entry:
            break
        idx = symboltable_list[idx]['parent']
    return entry


def insert(symboltable: dict, lexme: str, value, data_type: int):
    entry = search(symboltable, lexme)
    if entry and entry['is_constant'] == 1:
        return entry
    elif entry:
        return None
    else:
        entry = create_entry(lexme, value, data_type)
        symboltable[lexme] = entry
    return entry


def check_parameter_list(entry: dict, params: list, m: int):
    if m != entry.get('num_params'):
        raise Exception('Number of parameters and arguments do not match')
    i = 0
    for param in entry.get('parameter_list'):
        if param != params[i]:
            raise Exception('Parameter and argument types do not match')
        i += 1
    return 1


def fill_parameter_list(entry: dict, params: list, m: int):
    entry['parameter_list'] = params
    entry['num_params'] = m
