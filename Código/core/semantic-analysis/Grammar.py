# -*- coding: utf-8 -*-

"""
    @author Alexis
    @date 2020/08/16
    @version 0.3    
"""

grammar = """
    ?start: exp+

    ?exp: print
        | assign
        | for_function
        | if
        | while
        | func
        | funccall
        | length

    // ******************************************************************************
    // Console Output
    // ******************************************************************************

    ?print: "console" "." "log" "(" var ")" ";"? -> printvarlog
        | "console" "." "error" "(" var ")" ";"? -> printvarerror 
        | "console" "." "log" "(" string ")" ";"? -> printlog
        | "console" "." "error" "(" string ")" ";"? -> printerror

    // ******************************************************************************
    // Variable Assignment
    // ******************************************************************************

    ?assign: var "=" null ";"? -> assignvar
        | var "=" bool ";"? -> assignvar
        | var "=" string ";"? -> assignvar
        | var "=" ar_operation ";"? -> assignvar

    // ******************************************************************************
    // Arithmetic Operation
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
    // For Loop
    // ******************************************************************************

    ?for_function: "for" "(" var "=" ar_operation ";" condition ";" unary ")" "{" statements* "}" -> forfunction

    ?unary: var unary_op

    ?statements: log "(" var ")" ";"?
        | error "(" var ")" ";"?
        | log "(" string ")" ";"?
        | error "(" string ")" ";"?
        | varstatementdeclaration

    ?varstatementdeclaration: var "=" string ";"?
        | var "=" bool ";"?
        | var "=" null ";"?
        | var "=" operation ";"?

    ?operation: number
        | operation operator operation
        | var
        | open_parenthesis operation close_parenthesis

    ?operator: plus 
        | minus
        | star
        | slash

    !open_parenthesis: "("

    !close_parenthesis: ")"

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
    // If-Else Condition
    // ******************************************************************************

    ?if: "if" "(" ifcondition ")" "{" statements* "}" -> ifdeclaration
        | "if" "(" ifcondition ")" "{" statements* "}" else "{" statements* "}" ->ifdeclaration
        | "if" "(" ifcondition ")" statements ";"? -> ifdeclaration

    ?ifcondition: var if_com_operator number
        | number if_com_operator var
        | number if_com_operator number
        | var if_com_operator var
        
    ?if_com_operator: com_operator
        | /==/
        | /!=/

    !else: "else"

    // ******************************************************************************
    // While Function
    // ******************************************************************************

    ?while: "while" "(" while_condition ")" "{" statements* "}" -> while_loop

    ?while_condition: ifcondition
        | var
        | bool

    // ******************************************************************************
    // Function
    // ******************************************************************************

    ?func: "function" var "(" parameters ")" "{" funcstatements* "}" -> declarefunction

    ?parameters: var?
        | var "," parameters
        | number?
        | number "," parameters

    ?funcstatements: return
        | statements
        | iffunc

    ?iffunc: "if" "(" ifcondition ")" "{" statements* "}" 
        | "if" "(" ifcondition ")" "{" statements* "}" else "{" statements* "}"
        | "if" "(" ifcondition ")" statements ";"?
        | "if" "(" ifcondition ")" return ";"?

    ?return: r operation ";"?
        | r bool ";"?
        | r null ";"?
        | r funccall ";"?

    ?funccall: var "(" parameters ")" ";"? -> functioncall

    ?r: "return"

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

    // Length
    ?length: var ".length" ";" -> getlength 

    //Ignorar espacios, saltos de línea y tabulados
    %ignore /\s+/

"""