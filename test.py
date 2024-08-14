import unittest
import os
import tempfile
from flask import Flask, request, jsonify
from flask_testing import TestCase
from app import app, encrypt_file, decrypt_file

class TestCaseApp(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.client = self.app.test_client()

        # Carregar a API key do arquivo
        with open('api_key.txt', 'r') as file:
            self.api_key = file.read().strip()
            
        # Cria um arquivo PDF temporário para os testes
        self.test_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        with open(self.test_file.name, 'wb') as f:
            f.write(b'%PDF-1.4\n%aaIO\n1 0 obj\n<</Type /Catalog /Pages 2 0 R>>\nendobj\n2 0 obj\n<</Type /Pages /Kids [3 0 R] /Count 1>>\nendobj\n3 0 obj\n<</Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R>>\nendobj\n4 0 obj\n<</Length 44>>\nstream\nBT\n/F1 24 Tf\n72 720 Td\n(Teste de PDF) Tj\nET\nendstream\nendobj\ntrailer\n<</Root 1 0 R>>\n%%EOF')
    
    def tearDown(self):
        if os.path.exists(self.test_file.name):
            os.remove(self.test_file.name)

    def test_upload_file(self):
        with open(self.test_file.name, 'rb') as f:
            response = self.client.post('/upload', headers={'Authorization': self.api_key}, data={'file': (f, 'test.pdf')})
        
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Upload realizado e criptografado com sucesso.', response.data)
    
    def test_list_files(self):
        response = self.client.get('/list', headers={'Authorization': self.api_key})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_download_file(self):
        # Primeiro faça o upload
        with open(self.test_file.name, 'rb') as f:
            self.client.post('/upload', headers={'Authorization': self.api_key}, data={'file': (f, 'test.pdf')})

        # Depois faça o download
        response = self.client.get('/download/test.pdf.enc', headers={'Authorization': self.api_key})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/pdf')

if __name__ == '__main__':
    unittest.main()