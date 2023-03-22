#!/usr/bin/env python
import os
import argparse
from cryptography.fernet import Fernet

def generate_key():
    # Genera una clave de cifrado utilizando el algoritmo AES
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    # Carga una clave de cifrado desde el archivo key.key
    return open('key.key', 'rb').read()

def encrypt_file(filename, key):
    # Cifra un archivo utilizando la clave proporcionada
    f = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()

    encrypted = f.encrypt(original)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def encrypt_folder(foldername, key):
    # Cifra todos los archivos en una carpeta utilizando la clave proporcionada
    for subdir, dirs, files in os.walk(foldername):
        for file in files:
            filepath = subdir + os.sep + file
            encrypt_file(filepath, key)

def main():
    # Configura los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Cifra un archivo o carpeta utilizando el algoritmo AES')
    parser.add_argument('path', metavar='path', type=str, help='La ruta del archivo o carpeta que se cifrará')
    parser.add_argument('--keygen', action='store_true', help='Genera una nueva clave de cifrado')
    args = parser.parse_args()

    # Genera o carga la clave de cifrado
    if args.keygen:
        generate_key()
        print("Se generó una nueva clave de cifrado")
    key = load_key()

    # Cifra el archivo o carpeta especificado
    if os.path.isfile(args.path):
        encrypt_file(args.path, key)
        print(f"El archivo {args.path} se cifró correctamente")
    elif os.path.isdir(args.path):
        encrypt_folder(args.path, key)
        print(f"La carpeta {args.path} se cifró correctamente")
    else:
        print("La ruta especificada no es un archivo o carpeta")

if __name__ == '__main__':
    main()
