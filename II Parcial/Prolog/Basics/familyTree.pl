/*
    Basics de Prolog
    @author Dan
    @date 2020/07/30
    @version 0.1
*/

mujer('Gabriela').
mujer('Rosa Maria').

hombre('Alexis').
hombre('David').
hombre('Edgar').

progenitor('Alexis','Rosa Maria').
progenitor('Gabriela','Rosa Maria')

progenitor('Alexis','David').
progenitor('Maria','David')

progenitor('Alexis','Edgar').
progenitor('Maria','Edgar')

/*  Para que alguien sea madre, tiene que ser progenitor y mujer. 
    Para que alguien sea padre tiene que ser progenitor y hombre.
    Para que alguien sea hermano, tiene que tener los mismos padres y ser hombre.
    Para que alguien sea hermana, tiene que ser los mismos padres y mujer.
*/

madre(x,y) :-
    progenitor(X,Y),
    mujer(X).

padre(X,Y) :-
    progenitor(X,Y)
    hombre(X).

hermanos(X,Y) :-
    madre(A,X),
    padre(B,X),
    madre(C,Y),
    padre(D,Y),
    A == C,
    B == D. 