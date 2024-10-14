from collections import defaultdict
import itertools
import pickle

# Function to build co-occurrence matrix
def build_cooccurrence_matrix(transactions):
    """
    Builds a co-occurrence matrix where rows and columns represent article IDs, 
    and values represent how often two articles were purchased together.
    
    Args:
    transactions: DataFrame with customer_id and article_id columns.
    
    Returns:
    cooccurrence_matrix: A defaultdict with article pairs as keys and counts as values.
    """
    cooccurrence_matrix = defaultdict(int)
    
    # Group transactions by customer_id
    grouped_transactions = transactions.groupby('customer_id')['article_id'].apply(list)
    
    # Iterate over each customer's purchase history
    for articles in grouped_transactions:
        # Generate all unique pairs of article_ids purchased together
        for pair in itertools.combinations(articles, 2):
            # Sort the pair to avoid (a, b) and (b, a) being considered different
            pair = tuple(sorted(pair))
            cooccurrence_matrix[pair] += 1
    
    return cooccurrence_matrix

# Save the co-occurrence matrix as a pickle file
def save_cooccurrence_matrix(transactions, output_path='../output/cooccurrence_matrix.pkl'):
    """
    Builds the co-occurrence matrix from transactions and saves it as a .pkl file.
    
    Args:
    transactions: DataFrame of transactions (e.g., transactions_cleaned).
    output_path: Path to save the co-occurrence matrix .pkl file.
    """
    # Build the co-occurrence matrix
    cooccurrence_matrix = build_cooccurrence_matrix(transactions)
    
    # Save it to a pickle file
    with open(output_path, 'wb') as f:
        pickle.dump(cooccurrence_matrix, f)
    
    print(f"Co-occurrence matrix saved to {output_path}")

# Example usage: Generate and save the co-occurrence matrix
if __name__ == "__main__":
    import pandas as pd
    
    # Load the cleaned transactions data
    transactions_cleaned = pd.read_csv('../../data/transactions_cleaned.csv')
    
    # Build and save the co-occurrence matrix
    save_cooccurrence_matrix(transactions_cleaned)
