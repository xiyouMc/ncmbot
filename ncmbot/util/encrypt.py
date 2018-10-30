import json
import os

import binascii
from Crypto.Cipher import AES
import base64
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'

def createSecretKey(size):
    return binascii.hexlify(os.urandom(size))[:16]

def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + chr(pad) * pad
    encryptor = AES.new(secKey.encode('utf-8'), AES.MODE_CBC, b'0102030405060708')
    ciphertext = encryptor.encrypt(text.encode('utf-8'))
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    return ciphertext

def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text), 16), int(pubKey, 16), int(modulus, 16))
    return format(rs, 'x').zfill(256)

def encrypted_request(text):
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey.decode())
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {
        'params': encText,
        'encSecKey': encSecKey
    }
    return data


'''
class Encrypyed():
	"""
	解密算法
	"""
	def __init__(self):
		self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
		self.nonce = '0CoJUm6Qyw8W8jud'
		self.pub_key = '010001'

	# 登录加密算法, 基于https://github.com/stkevintan/nw_musicbox脚本实现
	def encrypted_request(self, text):
		text = json.dumps(text)
		sec_key = self.create_secret_key(16)
		enc_text = self.aes_encrypt(self.aes_encrypt(text, self.nonce), sec_key.decode('utf-8'))
		enc_sec_key = self.rsa_encrpt(sec_key, self.pub_key, self.modulus)
		data = {'params': enc_text, 'encSecKey': enc_sec_key}
		return data

	def aes_encrypt(self, text, secKey):
		pad = 16 - len(text) % 16
		text = text + chr(pad) * pad
		encryptor = AES.new(secKey.encode('utf-8'), AES.MODE_CBC, b'0102030405060708')
		ciphertext = encryptor.encrypt(text.encode('utf-8'))
		ciphertext = base64.b64encode(ciphertext).decode('utf-8')
		return ciphertext

	def rsa_encrpt(self, text, pubKey, modulus):
		text = text[::-1]
		rs = pow(int(binascii.hexlify(text), 16), int(pubKey, 16), int(modulus, 16))
		return format(rs, 'x').zfill(256)

	def create_secret_key(self, size):
		return binascii.hexlify(os.urandom(size))[:16]
'''
