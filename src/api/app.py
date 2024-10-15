from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

# Load the trained LightFM model
with open('../../output/lightfm_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the co-occurrence matrix
with open('../../output/cooccurrence_matrix.pkl', 'rb') as cooccurrence_file:
    cooccurrence_matrix = pickle.load(cooccurrence_file)

# Load articles with visual features
with open('../../output/articles_with_visual_features.pkl', 'rb') as articles_file:
    articles_cleaned = pickle.load(articles_file)

# Load customer and transaction data
print("Loading customer and transaction data...")
customers_cleaned = pd.read_csv('../../data/customers_cleaned.csv')
transactions_cleaned = pd.read_csv('../../data/transactions_cleaned.csv')

# Load the interaction matrix (LightFM interactions and weights)
with open('../../output/interactions.pkl', 'rb') as dataset_file:
    interactions, weights = pickle.load(dataset_file)

# Initialize Flask app
app = Flask(__name__)

# Define the API route for recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()

    # Extract customer_id and article_id from the request
    customer_id = data.get('customer_id')
    article_id = data.get('article_id')

    # Check if the customer exists in the customer dataset
    if customer_id not in customers_cleaned['customer_id'].values:
        return jsonify({"error": f"Customer {customer_id} not found in the dataset"}), 404

    # Import the hybrid recommendation function
    from src.model.hybrid_model import hybrid_recommendation_with_cooccurrence

    # Generate recommendations using the hybrid model
    recommendations = hybrid_recommendation_with_cooccurrence(
        customer_id=customer_id,
        article_id=article_id,
        model=model,
        dataset=interactions,  # Pass interactions here
        articles_df=articles_cleaned,
        cooccurrence_matrix=cooccurrence_matrix
    )

    # Return the recommendations as JSON
    return jsonify({"recommendations": recommendations})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5005)
