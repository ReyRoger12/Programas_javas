import ply.lex as lex
import ply.yacc as yacc

# Configuración del lexer
tokens = (
    'ENTERO',
    'FLOTANTE',
    'OPERADOR',
    'EXPONENTE',
    'PARENIZQ',
    'PARENDER'
)

t_OPERADOR = r'[\+\-\*/]'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_EXPONENTE(t):
    r'E[\+\-]?\d{1,2}'
    t.type = 'EXPONENTE'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Configuración del parser
def p_exp(p):
    'exp : termino exp_prima'
    pass

def p_exp_prima(p):
    '''exp_prima : OPERADOR termino exp_prima
                 | empty'''
    pass

def p_termino(p):
    '''termino : PARENIZQ exp PARENDER
               | numero'''
    pass

def p_numero(p):
    '''numero : ENTERO nc
              | FLOTANTE nc'''
    pass

def p_nc(p):
    '''nc : EXPONENTE
          | empty'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Error de sintaxis en la expresión.")

parser = yacc.yacc()

# Función para validar la expresión ingresada por el usuario
def validar_expresion(expresion):
    try:
        resultado = parser.parse(expresion)
        if resultado is None:
            print("La expresión es sintácticamente correcta.")
        else:
            print("Error de fórmula: La expresión no es válida.")
    except Exception as e:
        print("La expresión es incorrecta.", e)

# Solicitar entrada del usuario
expresion = input("Ingrese una expresión matemática: ")
validar_expresion(expresion)
