# -*- coding: utf-8 -*-

grammar = """

    //Axioma Inicial
    ?start:exp+

    //Expresiones Iniciales
    ?exp: vardeclaration
        | print
        | for_function
        | function

    ?vardeclaration: var "=" string ";"? -> assignvar
        | var "=" bool ";"? -> assignvar
        | var "=" ar_operation ";"? -> assignvar

    ?print: "console" "." "log" "(" var ")" ";"? -> printvarlog
        | "console" "." "error" "(" var ")" ";"? -> printvarerror 
        | "console" "." "log" "(" string ")" ";"? -> printlog
        | "console" "." "error" "(" string ")" ";"? -> printerror

    ?function: "function" var "(" ")" "{" statements "}"
        | "function" var "(" parameters ")" "{" statements "}"

    ?for_function: "for" "(" var "=" ar_operation ";" condition ";" unary ")" "{" forstatements* "}" -> forfunction

    ?unary: var unary_op

    ?forstatements: log "(" ar_operation ")" ";"?
        | error "(" ar_operation ")" ";"?
        | log "(" string ")" ";"?
        | error "(" string ")" ";"?

    ?log: "console" "." "log"

    ?error: "console" "." "error"

    ?unary_op: /\+\+|\-\-/

    ?condition: var com_operator ar_operation
        | ar_operation com_operator var

    ?com_operator: /</
        | />/
        | />=/
        | /<=/

    ?parameters: bool
        | var
        | var "," var

    ?statements: vardeclaration
        | print

    //Operación Aritmética
    ?ar_operation: factor
        | ar_operation "+" factor -> sum
        | ar_operation "-" factor -> sub

    ?factor: atom
        | factor "*" atom -> mul
        | factor "/" atom -> div 

    ?atom: var -> getvar
        | number
        | "-" atom
        | "(" ar_operation ")"

    // Definición de una Variable
    ?var: /[a-zA-Z]\w*/

    // Definición de un Número
    ?number: /\d+(\.\d+)?/

    // Booleano
    ?bool: /true|false/

    // Cadena
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Ignorar espacios, saltos de línea y tabulados
    %ignore /\s+/

"""