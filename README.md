installation and usage
1. Install Python
#### On Linux:
Use the following commands to install Python with essential packages:
sudo apt update
sudo apt install python3 python3-dev python3-pip python3-setuptools
#### On Windows:
Download the Python installer from the official website [python.org](https://www.python.org/downloads/) and follow the installation instructions.
2. Create a Virtual Environment (optional but recommended)
A virtual environment isolates your project’s dependencies. To create one:
python3 -m venv your_virtual_env
> **Note:** `your_virtual_env` is a placeholder. You can name it whatever you prefer.
#### Activate the Virtual Environment
On Linux:**
   source your_virtual_env/bin/activate
On Windows:**
your_virtual_env\Scripts\activate.bat
3. Install Requirements
On Windows:
To install Django, simply run:
pip install django
On Linux:
To ensure Django's default SQLite3 database runs smoothly, install SQLite3 dependencies:
sudo apt install libsqlite3-dev
If you plan to use a different database system, adjust your database settings in `settings.py` under **DATABASES**.
Example configuration for SQLite in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
You can modify `'ENGINE'` and `'NAME'` fields based on the database you intend to use.
4. migrate the migrations
to migrate them,just run
python3 manage.py migrate
5. Run the Server
For development**: Use Django's built-in development server:

   
   python3 manage.py runserver
For production**: It’s recommended to use a robust web server like **Apache** or **Nginx** with additional configurations for better performance and security.
