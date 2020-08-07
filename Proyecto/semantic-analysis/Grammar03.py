# -*- coding: utf-8 -*-

grammar = """
    ?start: exp+

    ?exp: print
        | assign
        | for_function

    // ******************************************************************************
    // Impresión
    // ******************************************************************************

    ?print: "console" "." "log" "(" var ")" ";"? -> printvarlog
        | "console" "." "error" "(" var ")" ";"? -> printvarerror 
        | "console" "." "log" "(" string ")" ";"? -> printlog
        | "console" "." "error" "(" string ")" ";"? -> printerror

    // ******************************************************************************
    // Asignación de Variables
    // ******************************************************************************

    ?assign: var "=" null ";"? -> assignvar
        | var "=" bool ";"? -> assignvar
        | var "=" string ";"? -> assignvar
        | var "=" ar_operation ";"? -> assignvar

    // ******************************************************************************
    // Operaciones Aritméticas
    // ******************************************************************************

    //Operación Aritmética
    ?ar_operation: factor
        | ar_operation "+" factor -> sum
        | ar_operation "-" factor -> sub

    ?factor: atom
        | factor "*" atom -> mul
        | factor "/" atom -> div

    ?atom: number
        | "-" atom
        | "(" ar_operation ")"
        | var -> getvar

    // ******************************************************************************
    // Ciclo For
    // ******************************************************************************

    ?for_function: "for" "(" var "=" ar_operation ";" condition ";" unary ")" "{" forstatements* "}" -> forfunction

    ?unary: var unary_op

    ?forstatements: log "(" var ")" ";"?
        | error "(" var ")" ";"?
        | log "(" string ")" ";"?
        | error "(" string ")" ";"?
        | varstatementdeclaration

    ?varstatementdeclaration: var "=" string ";"?
        | var "=" bool ";"?
        | var "=" null ";"?
        | var "=" operation ";"?

    ?operation: number
        | operation operator number
        | operation operator var

    ?operator: plus 
        | minus
        | star
        | slash

    !plus: "+"
    !minus: "-"
    !star: "*"
    !slash: "/"

    ?log: "console" "." "log"

    ?error: "console" "." "error"

    ?unary_op: /\+\+|\-\-/

    ?condition: var com_operator ar_operation
        | ar_operation com_operator var

    ?com_operator: /</
        | />/
        | />=/
        | /<=/
        
    // ******************************************************************************
    // Terminales
    // ******************************************************************************

    // Variable
    ?var: /[a-zA-Z]\w*/

    // Booleano
    ?bool: true 
        | false

    !true: "true"
    !false: "false"

    // Nulo o Vacio
    !null: "null"

    // Cadena
    ?string: /"[^"]*"/
        | /'[^']*'/

    // Número
    ?number: /\d+(\.\d+)?/

    //Ignorar espacios, saltos de línea y tabulados
    %ignore /\s+/
"""