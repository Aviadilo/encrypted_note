from .models import Category
from cryptography.fernet import Fernet
import base64


def encode_key(key):
    while len(key) % 32 != 0:
        key += b' '
    return base64.urlsafe_b64encode(key)


def encrypt(key, note_text):
    # convert string to bytes
    byte_key = bytes(key, 'utf-8')
    byte_note_text = bytes(note_text, 'utf-8')
    # extend length of byte_key to 32 char and encode it
    padded_key = encode_key(byte_key)
    # make cipher based on padded_key
    cipher = Fernet(padded_key)
    # encrypt the text
    encrypted_text = cipher.encrypt(byte_note_text)
    return str(encrypted_text, 'utf-8')


def decrypt(key, note_text):
    # convert string to bytes
    byte_key = bytes(key, 'utf-8')
    byte_note_text = bytes(note_text, 'utf-8')
    # extend length of byte_key to 32 char and encode it
    padded_key = encode_key(byte_key)
    # make cipher based on padded_key
    cipher = Fernet(padded_key)
    # decrypt the text
    try:
        decrypted_text = cipher.decrypt(byte_note_text)
        return str(decrypted_text, 'utf-8')
    except:
        return 'Invalid key'


def set_category(self):
    category = self.request.POST.get('category')
    if category == '':
        category = 'No category'
    ctg, created = Category.objects.get_or_create(category_name=category, defaults={'category_name': category})
    return ctg


def set_key(self):
    user_key = self.request.POST.get('password_for_encode')
    if user_key == '':
        user_key = self.request.POST.get('password_for_decode')
    return user_key
