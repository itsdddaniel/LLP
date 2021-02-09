;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Ejemplo de programa en Common LISP
;
; @author Daniel Arteaga
; @date 2020/07/22
; @version 0.1
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;Mensaje de bienvenida
(write-line "")
(write-line "")
(write-line "Escriba en pantalla un dato numerico")
(write-line "")

;Definir una variable y se le solicita el dato al usuario
(defvar *unaVariableCualquiera*)
(setf *unaVariableCualquiera* (read))

;Se imprimen los resultados de una operacion una cualquiera
(write-line "El resultado de su numero es * 5 es: ")
(write (* 5 *unaVariableCualquiera*))
(write-line "")

