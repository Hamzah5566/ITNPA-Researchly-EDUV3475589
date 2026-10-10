# Deployment – Researchly Abstract Classifier (Questions 1 & 2)

This folder holds everything needed to run the Streamlit web interface for the
best-performing model from Question 2.

| File | Purpose |
|------|---------|
| `app.py` | Streamlit web app (text box + **Classify Abstract** button) |
| `researchlyModel.pkl` | Saved scikit-learn pipeline (TF-IDF + classifier) |
| `requirements.txt` | Python packages needed to run the app |

> The model was saved with **scikit-learn 1.3.0**, so that exact version is pinned.
> Use **Python 3.9 – 3.11** (scikit-learn 1.3.0 has no wheels for newer Python versions).

---

## Option 1 – Run locally

```bash
# 1. Clone the repository
git clone https://github.com/Hamzah5566/ITNPA-Researchly-EDUV3475589.git
cd ITNPA-Researchly-EDUV3475589/deployment

# 2. Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 3. Install the requirements
pip install -r requirements.txt

# 4. Start the app
streamlit run app.py
```

The app opens at **http://localhost:8501**. Paste an abstract into the text box and
click **Classify Abstract**.

The first run downloads the NLTK `stopwords`, `wordnet` and `omw-1.4` resources
automatically, so an internet connection is needed the first time.

---

## Option 2 – Deploy online (Streamlit Community Cloud, free)

1. Push this repository to GitHub (public).
2. Go to <https://share.streamlit.io> and sign in with GitHub.
3. Click **Create app** → **Deploy a public app from GitHub**.
4. Fill in:
   - **Repository:** `Hamzah5566/ITNPA-Researchly-EDUV3475589`
   - **Branch:** `main`
   - **Main file path:** `deployment/app.py`
5. Open **Advanced settings** and choose **Python 3.11**.
6. Click **Deploy**. Streamlit installs `deployment/requirements.txt` and gives you a public URL.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `InconsistentVersionWarning` or error when loading the `.pkl` | Make sure `scikit-learn==1.3.0` is installed (`pip show scikit-learn`) |
| scikit-learn fails to install | You are on Python 3.12+; create the venv with Python 3.11 |
| `LookupError: Resource stopwords not found` | Run `python -m nltk.downloader stopwords wordnet omw-1.4` |
| `streamlit: command not found` | Activate the virtual environment, or run `python -m streamlit run app.py` |
| Port 8501 already in use | `streamlit run app.py --server.port 8502` |
