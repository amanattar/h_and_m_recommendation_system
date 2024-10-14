import pandas as pd
import numpy as np
from itertools import combinations
from collections import defaultdict
import pickle

# Function to build co-occurrence matrix
def build_cooccurrence_matrix(transactions):
    """
    Builds a co-occurrence matrix using pandas and article pairing logic.
    
    Args:
    transactions: DataFrame with customer_id and article_id columns.
    
    Returns:
    cooccurrence_matrix: A pandas DataFrame where rows and columns are articles, and values represent how often two articles were purchased together.
    """
    cooccurrence_dict = defaultdict(int)
    
    # Group transactions by customer_id
    print("Grouping transactions by customer_id...")
    grouped_transactions = transactions.groupby('customer_id')['article_id'].apply(list)
    print(f"Total unique customers: {len(grouped_transactions)}")

    # Generate co-occurrences by iterating over grouped transactions
    print("Building co-occurrence matrix...")
    for i, articles in enumerate(grouped_transactions, 1):
        # Get unique pairs of article_ids purchased together
        for pair in combinations(articles, 2):
            sorted_pair = tuple(sorted(pair))
            cooccurrence_dict[sorted_pair] += 1
        
        # Print progress for every 10,000 customers
        if i % 10000 == 0:
            print(f"Processed {i} customers...")

    # Convert the co-occurrence dictionary to a DataFrame
    print("Converting co-occurrence data into a pandas DataFrame...")
    cooccurrence_df = pd.DataFrame(list(cooccurrence_dict.items()), columns=['Article_Pair', 'Count'])
    
    # Split the article pairs into two columns
    cooccurrence_df[['Article_1', 'Article_2']] = pd.DataFrame(cooccurrence_df['Article_Pair'].tolist(), index=cooccurrence_df.index)
    cooccurrence_df = cooccurrence_df[['Article_1', 'Article_2', 'Count']]

    print("Co-occurrence matrix built successfully.")
    return cooccurrence_df

# Save the co-occurrence matrix to a pickle file
def save_cooccurrence_matrix(cooccurrence_df, output_path='../output/cooccurrence_matrix.pkl'):
    print(f"Saving the co-occurrence matrix to {output_path}...")
    with open(output_path, 'wb') as f:
        pickle.dump(cooccurrence_df, f)
    print(f"Co-occurrence matrix saved to {output_path}")

# Example usage:
if __name__ == "__main__":
    # Load the cleaned transactions data
    print("Loading transactions_cleaned.csv file...")
    transactions_cleaned = pd.read_csv('../data/transactions_cleaned.csv')
    print(f"Loaded {len(transactions_cleaned)} transactions.")

    # Build and save the co-occurrence matrix
    cooccurrence_matrix = build_cooccurrence_matrix(transactions_cleaned)
    save_cooccurrence_matrix(cooccurrence_matrix)