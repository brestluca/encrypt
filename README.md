# encrypt


Para ejecutar el script, debes proporcionar la ruta del archivo o carpeta que deseas cifrar como argumento en la línea de comandos. Además, puedes utilizar el argumento opcional "--keygen" para generar una nueva clave de cifrado. Por ejemplo, para cifrar un archivo llamado "example.txt", puedes ejecutar el siguiente comando:

python encrypt.py example.txt


Y para cifrar una carpeta llamada "folder", puedes ejecutar el siguiente comando:

python encrypt.py folder/


# crypto.py

Este script utiliza la biblioteca PyCryptodome de Python para cifrar y descifrar archivos utilizando el algoritmo de cifrado AES. En la función encrypt_file(), se cifra un archivo utilizando una clave AES y se escribe el archivo cifrado en un archivo de salida
