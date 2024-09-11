# Air Quality Index Dataset

## Setup di Enviroment Anaconda

Ekstrak terlebih dahulu. Lalu buka CMD/Terminal dan ikuti langkah-langkah berikut:

```bash
conda create --name venv-ds python=3.12.4
conda activate venv-ds
pip install -r requirements.txt
```

## Setup di Environment Python

Jika menggunakan Windows:

```bash
python -m venv venv-ds
.\venv-ds\Script\activate
pip install -r requirements.txt
```

Jika menggunakan MacOS/Linux:

```bash
python -m venv venv-ds
source ./venv-ds/bin/activate
pip install -r requirements.txt
```

## Jalankan App

```bash
streamlit run .\dashboard\dashboard.py
```
