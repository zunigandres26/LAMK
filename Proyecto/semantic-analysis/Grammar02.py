# -*- coding: utf-8 -*-

grammar = """

    //Axioma Inicial
    ?start:exp+

    //Expresiones Iniciales
    ?exp: print
        | var "=" string ";"? -> assignvar
        | var "=" bool ";"? -> assignvar
        | var "=" ar_operation ";"? -> assignvar

    ?print: "log" "(" string ")" ";"? -> printlog
        | "error" "(" string ")" ";"? -> printerror
        | "log" "(" var ")" ";"? -> printvarlog
        | "error" "(" var ")" ";"? -> printvarerror

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