import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard")

st.header('Final Project - Insights Igniters')
st.title('Cyber Bullying Dashboard')

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('cyberbullying_tweets.csv')
    return df

df = load_data()

# Display basic info
st.subheader('Dataset Overview')
st.write(f"Total tweets: {len(df)}")
st.write(f"Columns: {list(df.columns)}")

# Cyberbullying type distribution
st.subheader('Cyberbullying Type Distribution')
type_counts = df['cyberbullying_type'].value_counts()
st.bar_chart(type_counts)

# Pie chart
st.subheader('Proportion of Cyberbullying Types')
fig, ax = plt.subplots()
ax.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Sample tweets
st.subheader('Sample Tweets')
sample_size = st.slider('Number of samples', 1, 10, 5)
sample_df = df.sample(sample_size)
for idx, row in sample_df.iterrows():
    st.write(f"**Type:** {row['cyberbullying_type']}")
    st.write(f"**Tweet:** {row['tweet_text']}")
    st.write("---")
