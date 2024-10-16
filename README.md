# H&M Personalized Fashion Recommendations

This project is an end-to-end system for personalized fashion recommendations using collaborative filtering, visual similarity, and co-occurrence techniques. The backend is powered by Flask, while the frontend uses Streamlit to provide a user-friendly interface.

## Key Dependencies

The key dependencies include:

- **Flask** (for the backend API)
- **Streamlit** (for the frontend)
- **LightFM** (for collaborative filtering)
- **Pandas**, **Numpy**, **Scikit-learn** (for data manipulation and similarity calculations)

## How to Run the Project

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/h_and_m_recommendation_system.git
cd h_and_m_recommendation_system
````

### Step 2: Set Up the Environment

1.  Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
2.  Download the dataset from Kaggle:
    
    *   Visit the [H&M Personalized Fashion Recommendations Dataset](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data).
    *   Download the dataset and extract the contents.
3.  Place the extracted files in the following directory:
    
    ```bash
    h_and_m_recommendation_system/data/data/
    ```
    
    Ensure that the files like `customers.csv`, `transactions_train.csv`, and `articles.csv` are in the `data/data/` directory.
    

### Step 3: Prepare the Datasets

*   Ensure that `customers_cleaned.csv` and `transactions_cleaned.csv` are placed in the `data/` folder after preprocessing.
*   Optional: Add article images in the `data/images/` folder (for visual similarity).

### Step 4: Run the Flask Backend

The Flask backend serves recommendations via an API. To run the backend:

```bash
cd src/api
python app.py
```

This will start the Flask API on `http://127.0.0.1:5000`. If you want to use a different port:

```bash
python app.py --port 5001
```

### Step 5: Run the Streamlit Frontend

The Streamlit frontend provides an interface to input customer IDs and receive recommendations. To run the frontend:

```bash
cd ui
streamlit run streamlit_app.py
```

This will start the Streamlit app and open a browser window. The Streamlit app will communicate with the Flask API to fetch recommendations.

### Step 6: Test the Recommendation System

In the Streamlit app, you can input a **Customer ID** and optionally an **Article ID** to get personalized recommendations based on collaborative filtering, visual similarity, and co-occurrence.

API Overview
------------

The Flask API exposes a `/recommend` endpoint to generate recommendations. You can send a POST request with `customer_id` and optionally `article_id` to retrieve recommendations.

### Example:

```bash
curl -X POST http://127.0.0.1:5000/recommend \
    -H "Content-Type: application/json" \
    -d '{"customer_id": "000659db9979238065fe1f032cd87839b9a6ccf97d404f8513d6279281bda7e0", "article_id": "123456"}'
```

Functionality
-------------

### Collaborative Filtering:

*   The system uses the LightFM model trained on customer-article interactions to recommend items.
*   The model can handle implicit feedback such as user clicks or purchases.

### Visual Similarity:

*   Articles similar to the given article are recommended based on precomputed visual features using cosine similarity.

### Co-occurrence:

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



### **Summary of Key Instructions**:

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Download and extract the dataset from Kaggle and place it in the `data/data/` directory.
4. Run the Flask backend (`app.py`) and the Streamlit frontend (`streamlit_app.py`).
5. Test the recommendation system by sending requests via the API or using the Streamlit interface.

Let me know if you need any additional help or modifications!
```