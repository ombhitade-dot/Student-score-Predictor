# Streamlit Regression Lab

## Files
- `app.py` - Streamlit application
- `requirements.txt` - required Python packages

## Run locally

Open Command Prompt/PowerShell in this folder and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app opens in your browser.

## Important fixes from the Colab notebook
1. New-hour predictions are scaled before prediction because the models were trained using StandardScaler.
2. The prediction result DataFrame is constructed correctly.
3. The notebook's preprocessing demonstrations and all five regression models are included.
