PAC II 2020 - LL 1100
@author Daniel Arteaga
@date 2020/07/22
@version 0.1

LISP
====

* Es un lenguaje de proposito general.
* Integers, Ratios, Complex Numbers, Strings, Arrays, Vectors, Hash Tables, Functions, Streams.
* Expresiones-S se definen recursivamente, como:
    * Un tipo de dato simple, el cual se llama "atomo".
        * Un atomo corresponde con: numero, listas, cadenas de caracteres y simbolos.
    * Una lista de expresiones-S donde una expresion-S podria ser una lista de expresiones-S, que a su vez podria
    ser listas, y se pueden obtener expresiones anidadas de cualquier nivel de profundidad.

Expresion-S (S-expression)
---------------------------

* Expresion Simbolica: es una notacion de forma de texto usada en la representacion de estructudas de arbol, esta basada
en listas anidadas, en donde cada sublista es un subarbol. Las expresiones-S se usan en la familia de lenguajes de programacion
LISP. Su representacion es mediante secuencias de cadenas de caracteres, delimitadas por parentesis, y separadas por espacios:
(= 4 (+2 2)). En C este ejemplo seria 4 == 2+2.

Common Lisp
------------

* https://lisp-lang.org
* Requiere el uso de notacion pre-fija
* En consola lo ejecutamos usando un programa SBCL.
    * http://www.sbcl.org
    * http://www.sbcl.org/manual

    #
        $ sbcl
    #
* Ejemplos:
    #
        (+ 1 2) -> 3
        (+ 1 (+ 1 1)) -> 3
        (* (+ 1 2) (- 3 4))
        (+ (+ 3 3) (+ (+ 4 5) 6))
        (+ 3 4 5 6) ;La funcion de adicion puede tomar mas de un parametro.

        (defun funcion (x y) (+ x y 5)) ;La definicion de una funcion.
            (+ 1 2)
                (function 1 2) ;La ejecucion de una funcion.

        (let ((x 10)) x)
        (let ((y 10)) (- y 10))
        (list 4 5 6)
    #

* Para ejecutar un script:
    #
        $ sbcl --script program lisp
    #
* Tome en cuenta que:
    * SET puede establecer el valor de simbolos.
    * SETQ puede establecer el valor de variables.
    * SETF es un macro, posee la capacidad de definir varios elementos: simbolos, variables, elements de un arreglo, instacios, etc.
* Ejemplo de peticion de datos.
    #
        (write (+ 1 (read)))
    #
* Ejemplo (sin imprimir resultados):
    #
        (defvar *unaVariableCualquiera*)
        (setf *unaVariableCualquiera* 42.1)
        (write(* 2.1 *unaVariableCualquiera*))
    #
* Ejemplo de funcion y ejecucion de funcion
    #
        ; Se define una funcion
        (defun square(x) (* x x))

        ; Se usa la funcion
        (write (square 3))
    #
* Ejemplo de un programa que imprime mensajes en pantalla y recibe datos de usuario
    #

    #
* Ejemplo de factorial que imprime en resultado de pantalla de un numero fijo.
