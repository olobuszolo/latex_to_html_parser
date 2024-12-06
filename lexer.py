import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'VARIABLE',
    'INTEGRAL',
    'DOUBLE_INTEGRAL',
    'TRIPLE_INTEGRAL',
    'FRAC',
    'SUM',
    'SQRT',
    'UNDERSCORE',
    'CARET',
    'LBRACE',
    'RBRACE',
    'EQUAL',
    'ALPHA',
    'BETA',
    'GAMMA',
    'DELTA',
    'PI',
    'GEQ',
    'LEQ',
    'NEQ',
    'IN',
    'NOTIN',
    'FORALL',
    'EXISTS',
    'NEWLINE',
    'COMMENT',
    'LOG',
    'LN',
    'LEFT',
    'RIGHT',
    'MATH_LPAREN',
    'MATH_RPAREN',
    'MATH_LBRACKET',
    'MATH_RBRACKET',
    'MATH_LBRACE',
    'MATH_RBRACE'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_UNDERSCORE = r'_'
t_CARET = r'\^'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUAL = r'='
t_VARIABLE = r'[a-zA-Z]'
t_NEWLINE = r'\\\\'  

def t_LEFT(t):
    r'\\left'
    t.value = ""
    return t

def t_RIGHT(t):
    r'\\right'
    t.value = ""
    return t

def t_MATH_LPAREN(t):
    r'\('
    t.value = "("
    return t

def t_MATH_RPAREN(t):
    r'\)'
    t.value = ")"
    return t

def t_MATH_LBRACKET(t):
    r'\['
    t.value = "["
    return t

def t_MATH_RBRACKET(t):
    r'\]'
    t.value = "]"
    return t

def t_MATH_LBRACE(t):
    r'\\{'
    t.value = "{"
    return t

def t_MATH_RBRACE(t):
    r'\\}'
    t.value = "}"
    return t

def t_TRIPLE_INTEGRAL(t):
    r'\\iiint'
    t.value = "∭"
    return t

def t_DOUBLE_INTEGRAL(t):
    r'\\iint'
    t.value = "∬"
    return t

def t_INTEGRAL(t):
    r'\\int'
    t.value = "∫"
    return t

def t_FRAC(t):
    r'\\frac'
    return t

def t_SUM(t):
    r'\\sum'
    return t

def t_SQRT(t):
    r'\\sqrt(\[\d+\])?'
    if '[' in t.value:
        n = t.value[t.value.find('[')+1:t.value.find(']')]
        t.value = f"<sup>{n}</sup>&radic;"
    else:
        t.value = "&radic;"
    return t

def t_ALPHA(t):
    r'\\alpha'
    t.value = "&alpha;"
    return t

def t_BETA(t):
    r'\\beta'
    t.value = "&beta;"
    return t

def t_GAMMA(t):
    r'\\gamma'
    t.value = "&gamma;"
    return t

def t_DELTA(t):
    r'\\Delta'
    t.value = "&Delta;"
    return t

def t_PI(t):
    r'\\pi'
    t.value = "&pi;"
    return t

def t_GEQ(t):
    r'\\geq'
    t.value = "&ge;"
    return t

def t_LEQ(t):
    r'\\leq'
    t.value = "&le;"
    return t

def t_NEQ(t):
    r'\\neq'
    t.value = "&ne;"
    return t

def t_IN(t):
    r'\\in'
    t.value = "&in;"
    return t

def t_NOTIN(t):
    r'\\notin'
    t.value = "&notin;"
    return t

def t_FORALL(t):
    r'\\forall'
    t.value = "&forall;"
    return t

def t_EXISTS(t):
    r'\\exists'
    t.value = "&exist;"
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'%[^\n]*'
    pass  

def t_LOG(t):
    r'\\log'
    t.value = "log"
    return t

def t_LN(t):
    r'\\ln'
    t.value = "ln"
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Nieprawidłowy znak: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()