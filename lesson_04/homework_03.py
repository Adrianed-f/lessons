"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""


def xor_cipher(string, key):
    shifr = ""
    l1 = len(string)
    l2 = len(key)
    key = key * ((l1 // l2) + 1)   # берем длину строки с запасом, потому что может нацело не делиться
    while l2 != l1:   # укорачиваем до нужной длины(длины строки)
        key = key[0 : -1]
        l2 = len(key)
    i = 0
    while i < l1:
        shifr += chr(ord(string[i]) ^ ord(key[i]))
        i += 1
    return shifr


stroka_shifr = xor_cipher("Nikita", "14")
print(stroka_shifr)


def xor_uncipher(chiper, key):
    stroka = ""
    l1 = len(chiper)
    l2 = len(key)
    key = key * ((l1 // l2) + 1)
    while l2 != l1:
        key = key[0 : -1]
        l2 = len(key)
    i = 0
    while i < l1:
        stroka += chr(ord(chiper[i]) ^ ord(key[i]))
        i += 1
    return stroka

stroka = xor_uncipher(stroka_shifr, "14")
print(stroka)
