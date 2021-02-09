# -*- coding: utf-8 -*-

grammar = """

    //Definicion de una expresion.
    ?start: exp
    
    
    //Definición de una expresión.
    ?exp: var "=" string ";" -> assignvar
        | var "=" arithmeticoperation ";" -> assignvar
        | "print" "("? string ")"? ";" -> print_
        | "print" "("? var ")"? ";" -> printvar

    //Definición de operación aritmética/
    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation "+" arithmeticoperationatom -> sum
        | arithmeticoperation "-" arithmeticoperationatom -> sub

    //Definición de un átomo de operación aritmética.
    ?arithmeticoperationatom: var -> getvar
        | number
        | "-" arithmeticoperationatom
        | "(" arithmeticoperation ")"

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
