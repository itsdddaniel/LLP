# -*- coding: utf-8 -*-
#Gramatica de Common LISP

grammar = """

    //Definicion de una expresion.
    ?start: exp+ 

    //Definición de una expresión.
    ?exp: function
        | arithmeticoperation
        | "(" "write" "-" "line" string ")" -> printline
        | "(" "write" "(" arithmeticoperation ")" ")" -> printwrite
        | "(" "defvar" "*" var "*" ")" 
        | "(" "setf" "*" var "*" "(" "read" ")" ")"
        | "(" "setf" "*" var "*" number ")" -> assignvar
        | "(" "setf" "*" var "*" string ")" -> assignvar
        | "(" "if" "(" statement ")" arithmeticoperation "(" exp ")" ")"
        | "(" "if" "(" statement ")" arithmeticoperation ")"

    //Definición de operación aritmética/
    ?arithmeticoperation: arithmeticoperationatom
        | "+" arithmeticoperation "*" arithmeticoperationatom "*" -> sum
        | "+" arithmeticoperation arithmeticoperationatom -> sum
        | "(" "+" arithmeticoperationatom arithmeticoperationatom ")" -> sum
        | "(" "+" var arithmeticoperationatom ")" -> sum
        | "(" "+" var var ")"

        | "-" arithmeticoperation "*" arithmeticoperationatom "*" -> sub
        | "-" arithmeticoperation arithmeticoperationatom -> sub
        | "(" "-" arithmeticoperationatom arithmeticoperationatom ")" -> sub
        | "(" "-" var arithmeticoperationatom ")" -> sub
        | "(" "-" var var ")"

        | "*" arithmeticoperation "*" arithmeticoperationatom "*" -> multi
        | "*" arithmeticoperation arithmeticoperationatom -> multi
        | "*" arithmeticoperation "(" arithmeticoperationatom ")" -> multi
        | "(" "*" arithmeticoperationatom arithmeticoperationatom ")" -> multi
        | "(" "*" var arithmeticoperationatom ")" -> multi
        | "(" "*" var var ")"

        | "/" arithmeticoperation "*" arithmeticoperationatom "*" -> div
        | "/" arithmeticoperation arithmeticoperationatom -> div
        | "(" "/" arithmeticoperationatom arithmeticoperationatom ")" -> div
        | "(" "/" var arithmeticoperationatom ")" -> div
        | "(" "/" var var ")"

    //Definicon de una funcion.
    ?function: "(" "defun" var "(" param ")" exp ")"

    //Definicion de operadores.
    ?op: "+"
        | "-"
        | "*"
        | "/"

    //Def
    ?infnum: number
        | number infnum

    //Definicion de statement.
    ?statement: "<" var arithmeticoperationatom

    //Definición de un átomo de operación aritmética.
    ?arithmeticoperationatom: var -> getvar
        | number
        | "(" arithmeticoperation ")"

    //Definicion de parametros de una funcion.
    ?param: var -> assingvar_alt
        | var param 

    //Definición de una cadena.
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definición de variable.
    ?var: /[a-zA-Z]\w*/

    //Definicion de numero.
    ?number: /\d+(\.\d+)?/

    //Ignorar comentarios
    COMMENT: /;.*/
    %ignore COMMENT

    //Ignorar espacios, saltos de linea y tabulados.
    %ignore /\s+/
"""
