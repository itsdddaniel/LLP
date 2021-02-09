/*
    Basics de Prolog
    @author Dan
    @date 2020/07/30
    @version 0.1
*/

%Hechos
color(rojo).
color(azul).
color(verde).
color(amarillo).
color('Cian Semitaturado').

% ?- color(x) Da todos las reglas. y con ; da el 'next'

%Regla

colorPrimario(X) :- X == rojo ; X == verde ; X == azul.

% ?- colorPrimario(rojo). -> true colorPrimario('Cian Semisaturado'). -> false

colorPrimario(rojo).
colorPrimario(verde).
colorPrimario(azul).