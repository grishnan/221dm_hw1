#!/usr/bin/env python

alphabet = [chr(i) for i in range(1072, 1109)] # алфавит
length = len(alphabet) # мощность алфавита

text = input("Введите исходный текст: ")
key = int(input("Введите ключ шифрования: "))

textcode = [alphabet.index(symbol) for symbol in text] # исходный текст в кодовом представлении
cyphercode = [(value + key) % length for value in textcode]

cypher = ""
for c in cyphercode:
  cypher += alphabet[c]

print("Шифровка: ", cypher)
