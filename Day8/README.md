📅 Day 8 - Deploying My First AI Application
📚 What I Learned

How to organize a Streamlit project with app.py, README.md, requirements.txt, .gitignore, and .streamlit/secrets.toml

How to run a Streamlit app locally with:

python -m streamlit run app.py
How to test and debug the app before deployment
How to use requirements.txt to list required Python packages
How to use .gitignore to protect secret files
Why API keys should never be pushed to GitHub
How to store API keys safely using Streamlit Secrets
The difference between local Ollama and Ollama Cloud
Why localhost:11434 works locally but not from Streamlit Cloud
How to connect an AI app to Ollama Cloud using an API key
How to use cloud AI models so students do not have to download very large models
How to create a GitHub repository for a project

How to use:

git init
git status
git add .
git commit -m "message"
git push
How to connect a local project to a GitHub repository
How to rename the Git branch from master to main

How to fix a fetch first Git error using:

git pull --rebase origin main
How to deploy a GitHub project to Streamlit Community Cloud
How to select the repository, branch, and app.py file during deployment
How to create a public streamlit.app URL
How to update a live app by changing the code locally and pushing the new commit to GitHub
How to troubleshoot errors such as ModuleNotFoundError, missing models, missing API keys, and incorrect variable names
How to understand the complete deployment workflow:

BUILD
  ↓
TEST LOCALLY
  ↓
GIT ADD
  ↓
GIT COMMIT
  ↓
GIT PUSH
  ↓
STREAMLIT CLOUD
  ↓
PUBLIC AI APP
