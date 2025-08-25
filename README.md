# starter-api
Starter Code for API-Based challenges

## Getting Started
This project uses `uv` for Python dependencies. After you have cloned this project, you can install the dependencies:

```bash
$ uv sync
```

To initialize some sample data, there is a bootstrap script included called `bootstrap.py`. To initialize the database run migrations. amd then run the bootstrap script. This will create a file called `app.db` and populate it with data.

```bash
$ uv run alembic upgrade head
$ uv run bootstrap.py
```

## Launching the development server
This is a FastAPI application, so you should be able to run the app in either development mode or production mode. `fastapi-cli` is installed, so that command is available.

## Submitting your work
You will receive a particular task or set of tasks. To keep your work private, please create a private downstream repo:

```bash
$ git init private-repo
$ cd private-repo
$ git remote add upstream git@github.com:OneSpot-Learning/starter-code.git
$ git remote add origin git@github.com:<username>/private-repo.git
$ git push origin main
```

Then do your work on a feature branch, which you can name as you like.

Once you have completed the task, invite the hiring manager as a collaborator on your private repo, and open a PR in your private repository.

