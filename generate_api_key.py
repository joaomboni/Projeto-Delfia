import secrets

def generate_api_key(length=32): 
    
    return secrets.token_hex(length)

def save_api_key(filename, api_key):
    
    with open(filename, 'w') as file:
        file.write(api_key)

if __name__ == "__main__":  
                            
    key_length = 32 # Define o comprimento da chave em bytes (32 bytes = 64 caracteres hexadecimais)
    api_key = generate_api_key(key_length)
    
    
    save_api_key('api_key.txt', api_key) #Salve a chave no arquivo de texto
    
    print(f'Chave API gerada e salva em api_key.txt: {api_key}')