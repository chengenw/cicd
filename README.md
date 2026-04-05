# A Flask CI/CD Example

This project showcases a **simple Flask web app** integrated with **CI/CD** using GitHub Actions and deployed to **Railway**. It illustrates the end-to-end workflow of modern web development, including testing, continuous integration, and automated deployment.


## 🚀 Project Overview

- **Web App:** `app.py` – A minimal Flask application that returns a "Hello from CI/CD 🚀" message at `/`.
- **Testing:** `test_app.py` – Pytest tests to ensure the app works as expected.
- **Linting:** Flake8 to enforce Python code style.
- **CI/CD:** GitHub Actions workflow automatically runs linting, tests, and deploys the app if tests pass.
- **Deployment:** Railway hosting, using `gunicorn` to serve the Flask app in production.

---

## 📁 Project Structure
```
.
├─ app.py # Flask application
├─ test_app.py # Pytest tests for the app
├─ requirements.txt # Python dependencies
├─ Procfile # Gunicorn entry point for Railway
├─ .github/
│ └─ workflows/
│   └─ ci.yml # CI/CD workflow
└─ README.md
```
### app.py
app is the Flask instance used by Gunicorn (Procfile).

### test_app.py
- Simple test using Flask's test client.
- CI workflow runs this automatically.

### Procfile
- Tells Railway how to start the app in production.
- Format: `web: gunicorn <python_file>:<flask_app_variable>`

### CI/CD Workflow (.github/workflows/ci.yml)
- Lint: Ensures code style is consistent with Flake8.
- Test: Runs Pytest to verify functionality.
- Deploy: Only runs if linting and tests pass. Deploys to Railway using railway up CLI.

## Linting / Formatting
- Flake8: Checks your Python code for style issues and errors. Used in CI to ensure code quality.
- Black: Automatically formats your Python code to a standard style.
Run locally with:
```
black .
```

## 🔑 Setting GitHub Secrets for Railway

1. Go to your **Railway dashboard** → your project → **Settings** → **API Keys** (or Tokens).  
2. Copy your **Railway Token**.

3. Go to your **GitHub repository** → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.  
4. Add a secret with:
   - **Name:** `RAILWAY_TOKEN`
   - **Value:** paste your Railway token

5. In your GitHub Actions workflow (`ci.yml`), reference the secret:

```yaml
env:
  RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

## Deployment

- **Railway** – Free hosting with automatic deployments from GitHub.  
- **CI/CD Pipeline** – Every push to `main` or `master` triggers the test suite. If all tests pass, the application is deployed automatically.

> **Tip:** Ensure your `Procfile` correctly references your entry point (e.g., `app.py`). Misconfiguration can cause Gunicorn errors such as: `ModuleNotFoundError: No module named 'main'`.

## 📚 Learning Takeaways
- CI/CD Concepts: Automated lint → test → deploy pipeline.
- Flask Basics: Routes, app instance.
- Testing: How to use Flask test client with Pytest.
- Deployment: Gunicorn, Procfile, Railway hosting.
- Debugging: Common issues with Gunicorn module names.