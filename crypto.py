from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    # Cifra un archivo utilizando AES
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk = pad(chunk, 16)
                outfile.write(cipher.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=24 * 1024):
    # Descifra un archivo cifrado utilizando AES
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        iv = infile.read(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(cipher.decrypt(chunk))
            outfile.truncate(unpad(outfile.tell(), 16))

def main():
    # Cifra el archivo de prueba utilizando una clave
    key = b'ThisIsMySecretKey'
    encrypt_file(key, 'prueba.txt')

    # Descifra el archivo cifrado utilizando la misma clave
    decrypt_file(key, 'prueba.txt.enc')

if __name__ == '__main__':
    main()
