import numpy as np

def generate_recommendations(model, customer_id, dataset, interactions, num_recommendations=10):
    """
    Generate collaborative filtering recommendations for a given customer.

    Args:
        model: Trained LightFM model.
        customer_id: The customer ID for which to generate recommendations.
        dataset: The LightFM dataset containing customer and article mappings.
        interactions: The interaction matrix.
        num_recommendations: Number of recommendations to return (default=10).

    Returns:
        List of recommended article IDs.
    """
    # Get LightFM mappings for user and item IDs
    user_id_map, _, _, reverse_item_id_map = dataset.mapping()

    # Check if the customer exists in the LightFM dataset
    if customer_id not in user_id_map:
        print(f"Customer {customer_id} not found in the dataset.")
        return []

    # Get the internal LightFM user ID
    customer_internal_id = user_id_map[customer_id]

    # Predict the scores for all articles
    scores = model.predict(customer_internal_id, np.arange(interactions.shape[1]))

    # Rank the articles based on the predicted scores
    top_items = np.argsort(-scores)[:num_recommendations]

    # Convert internal item IDs back to original article IDs
    recommended_articles = [reverse_item_id_map[item] for item in top_items]

    return recommended_articles
