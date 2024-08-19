from cryptography.fernet import Fernet
Key = Fernet.generate_key()
f = Fernet(Key)
token = f.encrypt(b'This is a sample text')
token
b'...'
f.decrypt(token)
b'This is a sample text'
Key = Fernet.generate_key()
cipher_suite = Fernet(Key)
plain_text = b'This is a sample text'
cipher_text = cipher_suite.encrypt(plain_text)
decrypted_text = cipher_suite.decrypt(cipher_text)
print("ORIGINAL DATA : ",plain_text)
print("ENCRYPTED DATA : ",cipher_text)
print("DECRYPTED DATA : ",decrypted_text)
