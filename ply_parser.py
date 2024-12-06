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

def preprocess_latex(latex_input):
    lines = latex_input.splitlines()
    clean_lines = [line.split('%')[0] for line in lines] 

    clean_input = " ".join(line.strip() for line in clean_lines if line.strip())

    return clean_input

def latex_to_html(latex_input):
    latex_input = preprocess_latex(latex_input) 
    lexer.input(latex_input)
    html_output = ""
    stack = []  
    fraction_mode = False  
    numerator = ""  
    denominator = ""  

    for token in lexer:
        if token.type == 'NUMBER' or token.type == 'VARIABLE':
            if fraction_mode:
                if 'numerator' in stack:
                    numerator += str(token.value)
                elif 'denominator' in stack:
                    denominator += str(token.value)
            else:
                html_output += str(token.value)
        elif token.type == 'PLUS':
            html_output += " + "
        elif token.type == 'MINUS':
            html_output += " - "
        elif token.type == 'TIMES':
            html_output += " &times; "
        elif token.type == 'DIVIDE':
            html_output += " &divide; "
        elif token.type in ('LPAREN', 'RPAREN', 'MATH_LPAREN', 'MATH_RPAREN', 'MATH_LBRACKET', 'MATH_RBRACKET', 'MATH_LBRACE', 'MATH_RBRACE'):
            html_output += token.value
        elif token.type in ('INTEGRAL', 'DOUBLE_INTEGRAL', 'TRIPLE_INTEGRAL', 'SQRT'):
            html_output += token.value
        elif token.type == 'SUM':
            html_output += "&sum;"
        elif token.type == 'FRAC':
            fraction_mode = True
            html_output += "<span class='fraction'><span class='numerator'>"
            stack.append('numerator')
        elif token.type == 'UNDERSCORE':
            html_output += "<sub>"
            stack.append('sub')
        elif token.type == 'CARET':
            html_output += "<sup>"
            stack.append('sup')
        elif token.type == 'LBRACE':
            stack.append('{')
        elif token.type == 'RBRACE':
            if stack and stack[-1] == '{':
                stack.pop()
                if fraction_mode:
                    if 'numerator' in stack:
                        html_output += f"{numerator}</span><span class='denominator'>"
                        numerator = ""
                        stack.pop()
                        stack.append('denominator')
                    elif 'denominator' in stack:
                        html_output += f"{denominator}</span></span>"
                        denominator = ""
                        stack.pop()
                        fraction_mode = False
                elif 'sub' in stack:
                    html_output += "</sub>"
                    stack.pop()
                elif 'sup' in stack:
                    html_output += "</sup>"
                    stack.pop()
            else:
                html_output += "}"
        elif token.type == 'EQUAL':
            html_output += "="
        elif token.type == 'NEWLINE':
            html_output += "<br>"  
        elif token.type in ('ALPHA', 'BETA', 'GAMMA', 'DELTA', 'PI', 'GEQ', 'LEQ', 'NEQ', 'IN', 'NOTIN', 'FORALL', 'EXISTS'):
            html_output += token.value
        elif token.type == 'LOG':
            html_output += "log"
        elif token.type == 'LN':
            html_output += "ln"

    if fraction_mode:
        html_output += "</span></span>"

    return html_output

def save_html_to_file(html_content, filename="output.html"):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LaTeX to HTML</title>
        <style>
            .fraction {{
                display: inline-block;
                vertical-align: middle;
            }}
            .numerator {{
                display: block;
                text-align: center;
            }}
            .denominator {{
                display: block;
                text-align: center;
                border-top: 1px solid black;
            }}
            sub {{
                font-size: smaller;
                vertical-align: sub;
            }}
            sup {{
                font-size: smaller;
                vertical-align: super;
            }}
        </style>
    </head>
    <body>
        <h1>Wynik konwersji LaTeX na HTML</h1>
        <p>{html_output}</p>
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_template)


latex_input = r"""
\sqrt{x} \\ 
\sqrt[3]{y} + \int_{0}^{1} x^{2} dx \\ 
\iint_{0}^{1} x^{2} dx dy \\ 
\iiint_{0}^{1} x^{2} dx dy dz \\ 
\frac{1}{2} + \sum_{n=1}^{10} n^{2} \\ 
\alpha + \beta + \gamma + \Delta + \pi \\ 
x \geq y \\ 
x \leq y \\ 
x \neq y \\ 
x \in A \\ 
x \notin A \\ 
\forall x \exists y \\ 
\left( x + \frac{1}{2} \right) \\ 
\left[ \sqrt{y} \right] \\ 
\left\{ \int_{0}^{1} x dx \right\} \\ 
\log{x} + \log_{2}{x} + \ln{x}
"""

html_output = latex_to_html(latex_input)

save_html_to_file(html_output)
