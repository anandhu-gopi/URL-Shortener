# URLShortner

The following document covers the following aspects

* How to run the program

## How to run the program
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies from the requirements.txt file.

```bash
    pip install -r requirements.txt
```

Set the following environment variables

```bash
    export FLASK_APP=app
    export FLASK_ENV=development
    export SECRET_KEY="SomeRandomSecret"
```

Run init_db.py to create the necessary tables
```bash
    python init_db.py
```


The following command will run the app on port number 5000

```bash
     python app.py
```

Example
```bash
    export FLASK_APP=app
    export FLASK_ENV=development
    export SECRET_KEY="SomeRandomSecret"
    pip install -r requirements.txt
    python init_db.py
    python app.py

```

Open a browser and type in the URL http://127.0.0.1:5000/ to access the URLShortner page from browser.