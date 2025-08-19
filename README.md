# starter-api
Starter Code for API-Based challenges

## Getting Started
This project uses `uv` for Python dependencies. After you have cloned this project, you can install the dependencies:

```bash
$ uv sync
```

This project comes with a database with some test data in it. The file is `app.db`. If you want to create a new database, change the settings in `app/alembic/env.py` and `app/db.py` from `sqlite:///./app.db` to something else like `sqlite:///./another.db`. 

*OR*

You can delete `app.db` and run the following command to reinitialize the database:

```bash
$ uv run alembic upgrade head
```

## Launching the development server
This is a FastAPI application, so you should be able to run the app in either development mode or production mode. `fastapi-cli` is installed, so that command is available.

## Submitting your work
You will receive a particular task or set of tasks. Please complete those in a new branch. Push that branch to GitHub and let us know that you are done.