import numpy as np
from src.utils.cooccurrence import get_cooccurrence_recommendations
from src.model.collaborative_filtering import generate_recommendations
from src.model.visual_similarity import calculate_similarity

def hybrid_recommendation_with_cooccurrence(customer_id, article_id, model, dataset, articles_df, cooccurrence_matrix, top_n=10):
    """
    Hybrid recommendation system that combines collaborative filtering, visual similarity, and co-occurrence-based recommendations.
    """
    # Get collaborative filtering recommendations
    collab_recs = generate_recommendations(model, customer_id, dataset, num_recommendations=top_n)

    # If collaborative filtering cannot recommend enough items, use visual similarity
    if len(collab_recs) < top_n:
        visual_recs = calculate_similarity(article_id, articles_df, top_n=top_n-len(collab_recs))
        collab_recs = np.concatenate([collab_recs, visual_recs])

    # If there are still not enough recommendations, use co-occurrence
    if len(collab_recs) < top_n:
        cooccurrence_recs = get_cooccurrence_recommendations(article_id, cooccurrence_matrix, top_n=top_n-len(collab_recs))
        collab_recs = np.concatenate([collab_recs, cooccurrence_recs])

    return collab_recs[:top_n]
