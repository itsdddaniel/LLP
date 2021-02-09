/*
    Basics de Prolog
    @author Dan
    @date 2020/07/30
    @version 0.1
*/

edge(0,1,1).
edge(1,5,1).
edge(1,2,1).
edge(2,6,1).
edge(2,3,1).

connected(Vertex1,Vertex2) :- edge(X,Y,1), edge(Y,X,1).

path(A,B,Path) :- 
    travel(A,B,[A],Q),
    reverse(Q,Path).

travel(A,B,P,[B|P]) :-
    connected(A,B)

travel(A,B,Visited,Path) :- 
    connected(A,C),
    C \== B,
    \+member(C,Visited),
    travel(C,B,[C|Visited],Path)