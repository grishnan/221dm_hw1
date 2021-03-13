#!/usr/bin/env python3

codetable = [chr(i) for i in range(1072, 1109)]

text = input("Введите исходный текст: ")
key = int(input("Введите ключ шифрования: "))

codetext = [codetable.index(sym) for sym in text]
codecypher = [(c + key) % 37 for c in codetext]

cypher = ''.join([codetable[c] for c in codecypher])
print("Шифр: ", cypher)


text = input("Введите шифр: ")
key = int(input("Введите ключ шифрования: "))

codetext = [codetable.index(sym) for sym in text]
codecypher = [(c + key) % 37 for c in codetext]

cypher = ''.join([codetable[c] for c in codecypher])
print("Расшифровка: ", cypher)
