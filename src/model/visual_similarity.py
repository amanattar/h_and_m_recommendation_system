import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(article_id, articles_df, top_n=10):
    """
    Calculate visual similarity for a given article using cosine similarity of precomputed visual features.

    Args:
        article_id: The article ID for which to calculate similar articles.
        articles_df: DataFrame containing article IDs and their corresponding visual features.
        top_n: Number of similar articles to return (default=10).

    Returns:
        List of similar article IDs.
    """
    # Ensure the article exists in the dataset
    if article_id not in articles_df['article_id'].values:
        print(f"Article {article_id} not found in the dataset.")
        return []

    # Extract the visual features for the specified article
    target_features = articles_df.loc[articles_df['article_id'] == article_id, 'visual_features'].values[0]

    # Calculate cosine similarity between the target article and all other articles
    all_features = np.vstack(articles_df['visual_features'].values)
    similarities = cosine_similarity([target_features], all_features)[0]

    # Get the indices of the top N most similar articles
    top_similar_indices = np.argsort(-similarities)[1:top_n+1]  # Exclude the article itself

    # Return the article IDs of the most similar articles
    similar_articles = articles_df.iloc[top_similar_indices]['article_id'].values

    return similar_articles
