# -*- coding: utf-8 -*-
#Gramatica de C++

grammar = """

    //Definicion de una expresion.
    ?start: revst nams exp+ revend
        | revst nams exp+ 

    //Definición de una expresión.
    ?exp: cl
        | function
        | var "=" string ";" -> assignvar
        | var "=" string "+" var ";" -> assignvaralt
        | var "=" arithmeticoperation ";" -> assignvar

        | "cout" "<" "<" string ";" -> print_
        | "cout" "<" "<" string "<" "<" var ";" -> print_alt

        | "cout" "<" "<" var ";" -> printvar
        | "cout" "<" "<" var "<" "<" var ";" -> printvar_alt

        | "cin" ">" ">" var ";" -> docin

    //Definicion de una clase.    
    ?cl: "class" var "{" "public:" param ";" "}"
        | "class" var "{" "private:" param ";" "}"
        | "class" var "{" "protected:" param ";" "}"

    //Definicon de una funcion.
    ?function: vtypes var "(" param ")" "{" "pass" "}" ";"
        | vtypes var "(" param ")" "{" exp "}" ";"

    //Definicion de parametros de una funcion.
    ?param: vtypes var
        | vtypes var "," param

    //Definicion de mas de un cout.
    ?coutm: "<" "<" var 
        | "<" "<" string 

    //Definicion de mas de un cin.
    ?cinm: "<" "<" var cinm
        | "<" "<" var

    //Definición de operación aritmética/
    ?arithmeticoperation: arithmeticoperationatom

        | arithmeticoperation "+" arithmeticoperationatom -> sum
        | "(" arithmeticoperation ")" "+" arithmeticoperationatom -> sum

        | arithmeticoperation "-" arithmeticoperationatom -> sub
        | "(" arithmeticoperation ")" "-" arithmeticoperationatom -> sub

        | arithmeticoperation "*" arithmeticoperationatom -> multi
        | "(" arithmeticoperation ")" "(" arithmeticoperation ")" -> multi
        | number "(" arithmeticoperation ")" -> multi

        | arithmeticoperation "/" arithmeticoperationatom -> div
        | "(" arithmeticoperation ")" "/" arithmeticoperationatom -> div

    //Definición de un átomo de operación aritmética.
    ?arithmeticoperationatom: var -> getvar
        | number
        | "(" arithmeticoperation ")" 
        | "-" arithmeticoperationatom       

    //Definicion de una palabras reservadas.
    ?func: "def"
    | "if"

    //Definicion de reserved.
    ?revst: "#include<iostream>"
        | "#ifndef"
    ?revend: "#endif"
    ?nams: "using namespace std;"

    //Definicion de tipos de variables.
    ?vtypes: "float"
    | "int"
    | "void"
    | "string"
    | "double"

    //Definición de una cadena.
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definición de variable.
    ?var: /[a-zA-Z]\w*/

    //Definicion de numero.
    ?number: /\d+(\.\d+)?/

    //Ignorar espacios, saltos de linea y tabulados.
    %ignore /\s+/
"""
