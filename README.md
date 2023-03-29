# todo-app

Flask Todo App

## Installation

    git clone https://github.com/ambroisehdn/todo-app.git

    cd todo-app

    python3 -m venv env

    source env/bin/activate.fish NB : am using shell fish

    pip install -r requirements.txt

    cp .env.example .env

    inside the .env file change the database information !

## Migration

    -- flask db init -- Run this  if you want to create a fresh migration folder ! but before you should delete the existant folder

    -- flask db migrate -- Your should also run this command if you create a fresh migration folder

    Finaly run  :  flask db upgrade to  apply the migration !

## Run App

```flask run```

## API COLLECTION
