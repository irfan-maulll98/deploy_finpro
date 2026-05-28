# Cyber Bullying Dashboard

A Streamlit-based web application for analyzing cyberbullying tweets. This project provides an interactive dashboard to explore the dataset and a classification tool to predict cyberbullying types in tweets.

## Features

- **Dashboard**: Overview of the cyberbullying dataset with statistics, distribution charts, and sample tweets.
- **Classification**: Classify new tweets into cyberbullying categories using a trained machine learning model.

## Dataset

The dataset (`cyberbullying_tweets.csv`) contains tweets labeled with different cyberbullying types. It includes columns for tweet text and cyberbullying type.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd FinalProject
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit pandas matplotlib scikit-learn joblib
   ```

3. Ensure the model files (`model.pkl` and `tfidf.pkl`) are in the root directory.

## Usage

Run the Streamlit app:
```bash
streamlit run Dashboard.py

or

python -m streamlit run Dashboard.py

```

Navigate to the local URL provided (usually `http://localhost:8501`) to access the dashboard.

- **Dashboard Page**: View dataset overview, charts, and sample tweets.
- **Bullying Classification Page**: Enter a tweet text to classify it.

## Model

The classification uses a Logistic Regression model trained on TF-IDF vectorized tweet texts. The model predicts one of the cyberbullying types present in the dataset.

## Project Structure

- `Dashboard.py`: Main dashboard page.
- `pages/Bullying_Classification.py`: Classification page.
- `cyberbullying_tweets.csv`: Dataset file.
- `model.pkl`: Trained classifier model.
- `tfidf.pkl`: TF-IDF vectorizer.

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

This project is for educational purposes.
