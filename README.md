Here is the content you requested in proper Markdown format:


# Project Overview

The project leverages three key recommendation techniques:

- **Collaborative Filtering**: Uses the LightFM library to make recommendations based on user-item interaction data.
- **Visual Similarity**: Recommends articles similar to a given article by comparing precomputed visual features using cosine similarity.
- **Co-occurrence**: Suggests articles frequently purchased together using a co-occurrence matrix.

## Requirements

To run the project, ensure you have the following libraries installed:

```bash
pip install -r requirements.txt
````

The key dependencies include:

*   **Flask** (for the backend API)
*   **Streamlit** (for the frontend)
*   **LightFM** (for collaborative filtering)
*   **Pandas**, **Numpy**, **Scikit-learn** (for data manipulation and similarity calculations)

How to Run the Project
----------------------

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/h_and_m_recommendation_system.git
cd h_and_m_recommendation_system
```

### Step 2: Set Up the Environment

Install dependencies:

```bash
pip install -r requirements.txt
```

Prepare the datasets:

*   Ensure that `customers_cleaned.csv` and `transactions_cleaned.csv` are in the `data/` folder.
*   Optional: Add article images in the `data/images/` folder (for visual similarity).

### Step 3: Run the Flask Backend

The Flask backend serves recommendations via an API. To run the backend:

```bash
cd src/api
python app.py
```

This will start the Flask API on `http://127.0.0.1:5005`. If you want to use a different port:

```bash
python app.py
```

### Step 4: Run the Streamlit Frontend

The Streamlit frontend provides an interface to input customer IDs and receive recommendations. To run the frontend:

```bash
cd ui
streamlit run streamlit_app.py
```

This will start the Streamlit app and open a browser window. The Streamlit app will communicate with the Flask API to fetch recommendations.

### Step 5: Test the Recommendation System

In the Streamlit app, you can input a **Customer ID** and optionally an **Article ID** to get personalized recommendations based on collaborative filtering, visual similarity, and co-occurrence.

API Overview
------------

The Flask API exposes a `/recommend` endpoint to generate recommendations. You can send a POST request with `customer_id` and optionally `article_id` to retrieve recommendations.

Example:

```bash
curl -X POST http://127.0.0.1:5005/recommend \
    -H "Content-Type: application/json" \
    -d '{"customer_id": "000659db9979238065fe1f032cd87839b9a6ccf97d404f8513d6279281bda7e0", "article_id": "123456"}'
```

Functionality
-------------

*   **Collaborative Filtering**:
    
    *   The system uses the LightFM model trained on customer-article interactions to recommend items.
    *   The model can handle implicit feedback such as user clicks or purchases.
*   **Visual Similarity**:
    
    *   Articles similar to the given article are recommended based on precomputed visual features using cosine similarity.
*   **Co-occurrence**:
    
    *   Articles frequently purchased together with the given article are recommended using a co-occurrence matrix.

Files Overview
--------------

*   **`src/api/app.py`**: Flask API that handles recommendation requests.
*   **`src/model/collaborative_filtering.py`**: Contains the collaborative filtering logic using the LightFM model.
*   **`src/model/visual_similarity.py`**: Computes visual similarity between articles based on visual features.
*   **`ui/streamlit_app.py`**: Streamlit app that serves as the frontend interface.

Future Enhancements
-------------------

*   Improve performance by caching results for frequently requested customers or articles.
*   Add more features to the recommendation algorithm, such as time decay or category-based filtering.
*   Implement model retraining pipelines and integrate more data for better recommendations.

License
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
