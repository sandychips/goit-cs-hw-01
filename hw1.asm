section .data
    a db 10     ; Значення змінної a
    b db 20     ; Значення змінної b
    c db 5      ; Значення змінної c

section .text
global _start

_start:
    ; Віднімаємо значення c від b
    mov al, [b]
    sub al, [c]
    mov bl, al

    ; Додаємо значення a до результату попереднього кроку
    mov al, [a]
    add al, bl

    ; Виводимо результат на екран
    mov dl, al
    add dl, '0'  ; Конвертуємо число в символ
    mov ah, 02h
    int 21h

    ; Вихід з програми
    mov ah, 4Ch
    int 21h
