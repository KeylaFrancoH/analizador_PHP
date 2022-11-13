import ply.lex as lex

# Start Joby Farra

reserved = {
    # Control Structures
    "if": "IF",
    "else": "ELSE",
    "elseif": "ELSEIF",
    "endif": "ENDIF",
    "break": "BREAK",
    "pass": "PASS",
    "conntinue": "CONTINUE",
    "default": "DEFAULT",
    "return": "RETURN",
    "require": "REQUIRE",

    # Loop Structure
    "for": "FOR",
    "while": "WHILE",
    "switch": "SWITCH",
    "case": "CASE",
    "foreach": "FOREACH",
    "match": "MATCH",
    "endfor": "ENDFOR",
    "endwhile": "ENDWHILE",
    "endswitch": "ENDSWITCH",
    
    # Data Types
    "int": "INT",
    "double": "DOUBLE",
    "float": "FLOAT",
    "bool": "BOOL",
    "string": "STRING",
    "var": "VAR",
    "void": "VOID",
    "null": "NULL",
    "true": "TRUE",
    "false": "FALSE",
    "enum": "ENUM",
    "resource": "RESOURCE",
    "iterable": "ITERABLE",

    # Declaration words
    "function": "FUNCTION",
    "array": "ARRAY",
    "object": "OBJECT",
    "public": "PUBLIC",
    "private": "PRIVATE",
    "static": "STATIC",
    "protected": "PROTECTED",
    "class": "CLASS",
    "new": "NEW",
    "implements": "IMPLEMENTS",
    "extends": "EXTENDS",

    # Match Functions
    "sqrt": "SQRT",
    "abs": "ABS",
    "rand": "RAND",
    "min": "MIN",
    "max": "MAX",
    "pi": "PI",

    # Handle Error
    "try": "TRY",
    "catch": "CATCH",

    # Other words
    "exit": "EXIT",
    "global": "GLOBAL",
    "goto": "GOTO",
    "print": "PRINT",
    "echo": "ECHO",
}

# END Joby Farra

# START Keyla Franco
tokens = [
  #Operadores
  'SUMA', 
  'RESTA', 
  'MULTIPLICACION', 
  'DIVISION', 
  'MODULO', 
  'AND', 
  'OR', 
  'NOT', 
  'XOR', 
  'SL',
  'SR', 
  'BOOLEAN_AND', 
  'BOOLEAN_OR', 
  'BOOLEAN_NOT', 
  'IS_SMALLER',
  'IS_GREATER', 
  'IS_SMALLER_OR_EQUAL', 
  'IS_GREATER_OR_EQUAL', 
  'IS_EQUAL',
  'IS_NOT_EQUAL', 
  'IS_IDENTICAL', 
  'IS_NOT_IDENTICAL',
  
  #Tipos de datos
  'DIR',
  'FILE',
  'LINE',
  'FUNC_C',
  'CLASS_C', 
  'METHOD_C',
  'NS_C',
  'LOGICAL_AND',
  'LOGICAL_OR',
  'LOGICAL_XOR',
  'HALT_COMPILER',
  'STRING',
  'VARIABLE',
  'ENTERO', 
  'DECIMAL', 
  'NUM_STRING',
  'CONSTANT_ENCAPSED_STRING',
  'ENCAPSED_AND_WHITESPACE', 
  'QUOTE',
  'DOLLAR_OPEN_CURLY_BRACES', 
  'STRING_VARNAME', 
  'CURLY_OPEN',
  #Comparadores
  'EQUALS',
  'MUL_EQUAL', 
  'DIV_EQUAL', 
  'MOD_EQUAL',
  'PLUS_EQUAL',
  'MINUS_EQUAL',
  'SL_EQUAL', 
  'SR_EQUAL', 
  'AND_EQUAL', 
  'OR_EQUAL',
  'XOR_EQUAL', 
  'CONCAT_EQUAL',
  #ignorar comentarios
  'COMENTARIOS',
  'DOC_COMENTARIOS',
  #DELIMITADORES
  'LPAREN',
  'RPAREN', 
  'LBRACKET',
  'RBRACKET',
  'LBRACE', 
  'RBRACE', 
  'DOLLAR',
  'COMMA', 
  'CONCAT', 
  'QUESTION', 
  'COLON', 
  'SEMI', 
  'AT', 
  'NS_SEPARATOR',
#PHP TAGS
  'OPEN_TAG',
  'ECHO',
  'CLOSE_TAG',
#ESPACIO EN BLANCO
  'WHITESPACE'
] + list(reserved.values())
