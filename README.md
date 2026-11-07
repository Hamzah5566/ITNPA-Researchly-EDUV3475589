# ITNPA4-34 – Natural Language Processing with Python: Project 1

**Student:** Hamzah Suleman · **Student number:** EDUV3475589 · **Campus:** Eduvos Midrand Campus



## Repository structure

```
ITNPA-Researchly-EDUV3475589/
├── README.md                  ← this file
├── requirements.txt           ← packages needed to run the notebooks
├── data/                      ← project datasets
│   ├── research_abstracts.json        (Questions 1 & 2)
│   ├── research_corpus.zip            (Questions 3 & 4, original archive)
│   └── research_corpus/               (Questions 3 & 4, extracted .txt articles)
├── notebooks/                 ← analytics flow for Questions 1–4
│   ├── Q1_Q2_Classification.ipynb
│   ├── Q3_Q4_Topic_Modelling.ipynb
│   └── lda_intertopic_map.html        (pyLDAvis map, Question 4.2)
├── docs/                      ← project documentation (notebooks rendered with outputs)
│   ├── Q1_Q2_Classification.html
│   └── Q3_Q4_Topic_Modelling.html
└── deployment/                ← Streamlit web app for Questions 1 & 2
    ├── README.md              ← deployment instructions
    ├── app.py
    ├── researchlyModel.pkl
    └── requirements.txt
```

## Project documentation

| Question | Topic | Notebook | Rendered documentation |
|----------|-------|----------|------------------------|
| 1 | Preprocessing, feature engineering, baseline model | [`Q1_Q2_Classification.ipynb`](notebooks/Q1_Q2_Classification.ipynb) | [`docs/Q1_Q2_Classification.html`](docs/Q1_Q2_Classification.html) |
| 2 | Model comparison, performance enhancement, deployment | [`Q1_Q2_Classification.ipynb`](notebooks/Q1_Q2_Classification.ipynb) | [`docs/Q1_Q2_Classification.html`](docs/Q1_Q2_Classification.html) |
| 3 | Corpus dataframe, denoising, summarisation | [`Q3_Q4_Topic_Modelling.ipynb`](notebooks/Q3_Q4_Topic_Modelling.ipynb) | [`docs/Q3_Q4_Topic_Modelling.html`](docs/Q3_Q4_Topic_Modelling.html) |
| 4 | LDA topic modelling, pyLDAvis intertopic map | [`Q3_Q4_Topic_Modelling.ipynb`](notebooks/Q3_Q4_Topic_Modelling.ipynb) | [`docs/Q3_Q4_Topic_Modelling.html`](docs/Q3_Q4_Topic_Modelling.html) |



## Running the notebooks

```bash
git clone https://github.com/Hamzah5566/ITNPA-Researchly-EDUV3475589.git
cd ITNPA-Researchly-EDUV3475589
python -m venv venv
venv\Scripts\activate          # Windows  (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt jupyter
python -m spacy download en_core_web_sm
jupyter notebook notebooks/
```

The notebooks read data from `../data/`, so open them from inside the `notebooks/` folder.

## Deployment (Questions 1 & 2)

See [`deployment/README.md`](deployment/README.md). Quick start:

```bash
cd deployment
pip install -r requirements.txt
streamlit run app.py
```
