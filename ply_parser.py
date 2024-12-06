from lexer import lexer  

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