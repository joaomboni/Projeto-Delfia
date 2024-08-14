import tracemalloc #rastreamento de uso de memoria
tracemalloc.start()


from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("secret.key", "rb") as key_file: # Função with para fechar arquivo.
        return key_file.read()


def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted_data)


def decrypt_file(encrypted_file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(encrypted_file_path.replace(".enc", ""), "wb") as file:
        file.write(decrypted_data)



snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("Top 10 linhas com maior alocação:")
for stat in top_stats[:10]:
    print(stat)