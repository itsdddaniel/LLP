#-*- coding: utf-8 -*-
"""
Conforman la Gramática: Léxico, Sintaxis, Semántica.

    E.g.:
        Cuidado, ¡ladrón!.
        Cuidado ladrón. 

Manejo de errores en todo lenguaje de programción.
Existen errores léxicos, sintácticos, gramaticales y semánticos en la generación de código.
El manejo de errores identifica:
    El número de línea donde ocurre el error.
    El tipo de error.
    El caracter donde ocurre el error.

"""

"""
    ! Método factorial.
    * Permite calcular la multiplicación de n*(n-1)(n-2)*...*(n-k), donde n-k >= 1
    @author Dan
    @version 0.1

"""

def factorial(n):
    if n<2: return 1
    return n*factorial(n-1)

m = 5
n = m
print("El factorial en Python para '%d' es: %d" % (n,factorial(n)))    