# -*- coding: utf-8 -*-
"""cleaned_labeled_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ur_UbuoCshK43-qUJhvmg6CKrG5_ByqN
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('cleaned_labeled_data.csv')

data.head(10)

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "hello!! he said---- and want."

no_punct = " "
for char in my_str:
  if char not in punctuations:
    no_punct = no_punct + char
print(no_punct)

import pandas as pd

# Define the set of punctuations to remove
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~=`'''

# Input and output file paths
input_csv = 'cleaned_labeled_data.csv'   # Replace with your input CSV file
output_csv = 'cleaned_cleaned_labeled_data.csv'  # Replace with your desired output CSV file

# Load the dataset
df = pd.read_csv(input_csv)

# Check if the column exists (assuming the column is named 'Text')
if 'tweet' not in df.columns:
    raise ValueError("The CSV file must have a 'tweet' column with text data to clean.")

# Function to remove punctuation
def remove_punctuation(text):
    return ''.join(char for char in str(text) if char not in punctuations)

# Apply the function to the 'Text' column
df['Cleaned_Text'] = df['tweet'].apply(remove_punctuation)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv, index=False)

print(f"Cleaned dataset saved to {output_csv}")

df

import pandas as pd
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK Punkt tokenizer models (run once)
nltk.download('punkt_tab')

# Input and output file paths
input_csv = 'cleaned_cleaned_labeled_data.csv'   # Replace with your input CSV file
output_csv = 'tokenized_cleaned_cleaned_labeled_data.csv'  # Replace with your desired output CSV file

# Load the dataset
df = pd.read_csv(input_csv)

# Check if 'Cleaned_Text' column exists, adjust column name as necessary
if 'Cleaned_Text' not in df.columns:
    raise ValueError("The CSV file must have a 'Cleaned_Text' column with text data to tokenize.")

# Tokenize the 'Text' column
df['Tokenized_Cleaned_Text'] = df['Cleaned_Text'].apply(lambda x: word_tokenize(str(x)))

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv, index=False)

print(f"Tokenized dataset saved to {output_csv}")

df

import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download the stopwords and Punkt tokenizer models (run once)
nltk.download('stopwords')
nltk.download('punkt')

# Input and output file paths
input_csv = 'tokenized_cleaned_cleaned_labeled_data.csv'   # Replace with your input CSV file
output_csv = 'stopwords_tokenized_cleaned_cleaned_labeled_data.csv'  # Replace with your desired output CSV file

# Load the dataset
df = pd.read_csv(input_csv)

# Check if the column exists (assuming the column is named 'Cleaned_Text')
if 'Cleaned_Text' not in df.columns:
    raise ValueError("The CSV file must have a 'Cleaned_Text' column with text data to clean.")

# Define stopwords
stop_words = set(stopwords.words('english'))

# Function to remove stopwords
def remove_stopwords(text):
    words = word_tokenize(str(text))  # Tokenize the text
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Apply the function to the 'content' column
df['No_Stopwords_Content'] = df['Cleaned_Text'].apply(remove_stopwords)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv, index=False)
print(f"Dataset with stopwords removed saved to {output_csv}")

df

import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

# Download the Punkt tokenizer models (run once)
nltk.download('punkt_tab')

# Input and output file pathsstopwords_tokenized_cleaned_cleaned_kaggle_parsed_dataset.csv
input_csv = 'stopwords_tokenized_cleaned_cleaned_labeled_data.csv'   # Replace with your input CSV file
output_csv = 'stemmed_stopwords_tokenized_cleaned_cleaned_labeled_data.csv'  # Replace with your desired output CSV file

# Load the dataset
df = pd.read_csv(input_csv)

# Check if the column exists (assuming the column is named 'content')
if 'Cleaned_Text' not in df.columns:
    raise ValueError("The CSV file must have a 'Cleaned_Text' column with text data to stem.")

# Initialize the stemmer
stemmer = PorterStemmer()

# Function to perform stemming with recursion error handling
def stem_text(text):
    words = word_tokenize(str(text))  # Tokenize the text
    stemmed_words = []
    for word in words:
        try:
            stemmed_words.append(stemmer.stem(word))  # Stem each word
        except RecursionError:
            stemmed_words.append(word)  # Keep the original word if RecursionError occurs
            print(f"RecursionError encountered for word: {word}. Skipping stemming for this word.")
    return ' '.join(stemmed_words)

# Apply the function to the 'content' column
df['Stemmed_Content'] = df['Cleaned_Text'].apply(stem_text)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv, index=False)

print(f"Dataset with stemming applied saved to {output_csv}")

df

import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

# Download necessary NLTK data (run once)
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input and output file paths
input_csv = 'stemmed_stopwords_tokenized_cleaned_cleaned_labeled_data.csv'   # Replace with your input CSV file
output_csv = 'lemmatized_stemmed_stopwords_tokenized_cleaned_cleaned_labeled_data.csv'  # Replace with your desired output CSV file

# Load the dataset
df = pd.read_csv(input_csv)

# Check if the column exists (assuming the column is named 'content')
if 'Cleaned_Text' not in df.columns:
    raise ValueError("The CSV file must have a 'Cleaned_Text' column with text data to lemmatize.")

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to perform lemmatization
def lemmatize_text(text):
    words = word_tokenize(str(text))  # Tokenize the text
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]  # Lemmatize each word
    return ' '.join(lemmatized_words)

# Apply the function to the 'content' column
df['Lemmatized_Content'] = df['Cleaned_Text'].apply(lemmatize_text)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv, index=False)

print(f"Dataset with lemmatization applied saved to {output_csv}")

df

