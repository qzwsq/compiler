# coding=utf-8
from ply import lex
from symboltable import SymbolTable

constant_table = SymbolTable()
tokens = [
  'IDENTIFIER',
  'DEC_CONSTANT', 'HEX_CONSTANT', 'CHAR_CONSTANT', 'FLOAT_CONSTANT', 'STRING',
  'LOGICAL_AND', 'LOGICAL_OR', 'LS_EQ', 'GR_EQ', 'EQ', 'NOT_EQ',
  'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN',
  'INCREMENT', 'DECREMENT',
  'SHORT', 'INT', 'LONG', 'LONG_LONG', 'SIGNED', 'UNSIGNED', 'CONST', 'VOID', 'CHAR', 'FLOAT', 'CHAR_STAR',
  'IF', 'FOR', 'WHILE', 'CONTINUE', 'BREAK', 'RETURN', 'ELSE', 'LOWER_THAN_ELSE'
]
reversed_tokens = {
    ',': 'COMMA',
    '(': 'LP',
    ')': 'RP',
    '[': 'MLP',
    '{': 'BLP',
    '}': 'BRP',
    ']': 'MRP',
    ';': 'SEMICOLON',
    '=': 'ASSIGN',
    '<': 'LS',
    '>': 'GR',
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MUL',
    '/': 'DIV',
    '%': 'MOD',
    '!': 'NOT',
}
tokens += reversed_tokens.values()


def t_INT(t):
    r'int'
    return t


def t_CHAR_STAR(t):
    r'char\*'
    return t


def t_CHAR(t):
    r'char'
    return t


def t_FLOAT(t):
    r'float'
    return t


def t_VOID(t):
    r'void'
    return t


def t_LONG(t):
    r'long'
    return t


def t_LONG_LONG(t):
    r'long long'
    return t


def t_SHORT(t):
    r'short'
    return t


def t_SIGNED(t):
    r'signed'
    return t


def t_UNSIGNED(t):
    r'unsigned'
    return t


def t_FOR(t):
    r'for'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_BREAK(t):
    r'break'
    return t


def t_CONTINUE(t):
    r'continue'
    return t


def t_IF(t):
    r'if'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_FLOAT_CONSTANT(t):
    r'[\+-]?[0-9]*\.[0-9]+'
    constant_table.insert(t.value, float(t.value), 5)
    return t


def t_DEC_CONSTANT(t):
    r'[\+-]?[0-9]+'
    constant_table.insert(t.value, int(t.value), 0)
    return t


def t_STRING(t):
    r'\"[^\"\n]*\"'
    constant_table.insert(t.value, 2147483647, 7)
    return t


def t_CHAR_CONSTANT(t):
    r'\'([a-zA-Z]|[0-9])\''
    constant_table.insert(t.value, t.value, 4)
    return t


t_IDENTIFIER = r'(_|[a-zA-Z])([a-zA-Z]|[0-9]|_){0,31}'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_LS_EQ = r'<='
t_GR_EQ = r'>='
t_NOT_EQ = r'!='
t_EQ = r'=='
t_COMMA = r','
t_LP = r'\('
t_RP = r'\)'
t_MLP = r'\['
t_MRP = r'\]'
t_BLP = r'{'
t_BRP = r'}'
t_SEMICOLON = ';'
t_ASSIGN = r'='
t_GR = r'>'
t_LS = r'<'
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_NOT = r'!'
t_ignore = ' \t\r\f\v'


# Error handling rule
def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
# with open('test-func.c', 'r') as code:
#     lexer.input(code.read())
# for tok in lexer:
#     print(tok)
