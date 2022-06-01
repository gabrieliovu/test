Colibri
==========

Gabriel Iovu


------------------------

# Prerequirements
- python v3.8.5
- postgresql v14

# Installation
1. Clone the repository.

    ```
    git clone Url_Repository
    ```

2. cd into it

    ```
    cd test
    ```
   
3. create virtual env & activate
   
    ```
    python3 -m venv colibri
    source colibri/bin/activate
    ```

4. install requrirements
    ```
    pip install -r requirements.txt
    ```
5. migrate
    ```
    ./manage.py migrate
    ```
6. run server
    ```
    ./manage.py runserver
    ```
   
7. run tests
    ```
    ./manage.py test
    ```
   
8. to see api swagger schema
   ```
   GET http://127.0.0.1:8000/
   ```

9. check flake8
   ```
   flake8 .
   ```