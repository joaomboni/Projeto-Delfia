import tracemalloc #rastreamento de uso de memoria
tracemalloc.start()


from flask import Flask, request, send_file, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import logging
from crypto import encrypt_file, decrypt_file

app = Flask(__name__)
auth = HTTPBasicAuth()
logging.basicConfig(filename='app.log', level=logging.INFO)

#Carrega api key do arquivo .txt
def load_api_key():
    with open('api_key.txt', 'r') as file:
        return file.read().strip()

API_KEY = load_api_key()

def check_api_key(api_key):
    return api_key == API_KEY

@app.route('/upload', methods=['POST'])
def upload_file():
    api_key = request.headers.get('Authorization')
    if not api_key or not check_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401

    if 'file' not in request.files:
        return jsonify({'error': 'Nenhuma parte do arquivo'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado.'}), 400

    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        file_path = os.path.join('documents', filename)
        file.save(file_path)

        # Criptografar o arquivo
        encrypt_file(file_path)

        os.remove(file_path)  # Remove o arquivo original não criptografado

        logging.info(f'Upload realizado e criptografado: {filename}')
        return jsonify({'message': 'Upload realizado e criptografado com sucesso.'}), 201

    return jsonify({'error': 'Apenas arquivos PDF.'}), 400


@app.route('/list', methods=['GET'])
def list_files():
    api_key = request.headers.get('Authorization')
    if not api_key or not check_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401

    files = [f for f in os.listdir('documents') if f.endswith('.pdf.enc')]
    return jsonify(files), 200


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    api_key = request.headers.get('Authorization')
    if not api_key or not check_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401


    file_path = os.path.join('documents', filename)

    if not os.path.isfile(file_path):
        return jsonify({'error': 'File not found'}), 404

    # Descriptografar o arquivo antes do download
    decrypt_file(file_path)

    return send_file(file_path.replace('.enc', ''), as_attachment=True)


if __name__ == '__main__':
    if not os.path.exists('documents'):
        os.makedirs('documents')
    app.run(debug=True)



snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("Top 10 linhas com maior alocação:")
for stat in top_stats[:10]:
    print(stat)