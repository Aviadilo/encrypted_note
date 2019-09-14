from django.test import TestCase
from .models import Note, Category
from .func import encrypt, decrypt
from django.urls import reverse_lazy

def create_encrypted_object(user_key, user_text):
    encrypted_text = encrypt(user_key, user_text)
    new_category = Category.objects.create(category_name="Greatest quotes")
    Note.objects.create(category=new_category, note_body=encrypted_text)


class EncryptingTestCase(TestCase):

    user_text = 'These are not the droids you are looking for'
    user_key = 'London is'

    def setUp(self):
        create_encrypted_object(self.user_key, self.user_text)

    def if_decrypted_text_equals_user_text(self):
        test_note = Note.objects.get(id=1)
        decrypted_text = decrypt(key=self.user_key, note_text=test_note.note_body)
        self.assertEqual(self.user_text, decrypted_text)

    def if_incorrect_key_was_used(self):
        test_note = Note.objects.get(id=1)
        decrypted_text = decrypt(key='London does', note_text=test_note.note_body)
        self.assertFalse(self.user_text == decrypted_text)
        self.assertTrue(decrypted_text == 'Invalid key')


class NoteUpdateViewTest(TestCase):
    user_text = 'These are not the droids you are looking for'
    user_key = 'London is'

    def setUp(self):
        create_encrypted_object(self.user_key, self.user_text)

    def update_view_url_exists_at_desired_location(self):
        response = self.client.post('/decoded/1', {'id': 1, 'password_for_decode': self.user_key})
        self.assertEqual(response.status_code, 200)

    def update_view_url_accessible_by_name(self):
        response = self.client.post(reverse_lazy('note-decoded-update', kwargs={'pk': 1}), {'id': 1, 'password_for_decode': self.user_key})
        self.assertEqual(response.status_code, 200)

    def update_view_uses_correct_template(self):
        response = self.client.post('/decoded/1', {'id': 1, 'password_for_decode': self.user_key})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_update.html')
