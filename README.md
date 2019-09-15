# Encrypted notes
What is it?
-----------
Encrypted notes is a simple app, developed with Django. The app allows you - what? well done, Watson! - allows you to encrypt your notes, using your secret key.

Not only encrypt. This small, but very proud app allows you to decrypt the notes with the same secret key.

If you are bored of your secret key, you can change it at any moment to another interesting and unpredictable key.

If you decide to modify your note - OK, you have such a possibility.

You can define a category to your note for more convenient storage and search.

And finally - good advice for you. Please, don't forget you secret key. Not. One. Bit.

Installation
------------
In fact, to install the app to the local server is a little bit easier than to land Falcon 9 first stage. Installation includes four stages:
- clone the repository;
- install virtual environment;
- install requirements;
- run.

So, let's begin in order.
1. Clone the repository:
- push "Clone or download" and copy the link
- open the terminal and change the current working directory to the folder, where you are going to keep the project (for example, "D:\Projects")
- clone copied repository with command "git clone <copied_link>"
- go to the folder "encrypted_note"
2. Install virtual environment:
- create virtual environment with command "python -m venv <venv_name>"
- activate your venv with command "<venv_name>\Scripts\activate
3. Install requirements:
- do it with command "pip install -r requirements.txt"
4. Run:
- just do it with command "python manage.py runserver"

Server is running! Now click on the link to run the app.

How to use the app
------------------
Home page an the first time shows nothing, except navbar. Navbar contains "Notes" and "Create note" buttons. "Notes" redirects you to the home page. "Create button" redirects you to create page.

Now, if you want to create new note, enter the text and secret key, which is used for encoding and decoding your notes. So, don't forget it. If you don't define category, the note will be saved with category "Other category". After saving you wil be redirect to the home page.

If some notes were created, home page presents list of category notes. You can click on the category name to show/hide all notes with that category. You can click on the note number to be redirected to note detail page.

Note detail page shows category name and encrypted note below it. When entering secret key and clicking on "Decode" you will be redirected to page, that shows you decrypted text of your note.

If you want to update it, click on "Update". You should enter current key to save changes. You also can enter new key, if you want to change it. After saving you will be redirected to the home page.

If you entered incorrect key, you will be redirected to the Great and Terrible Error Page. So, don't forget your secret key and... Why so serious?
