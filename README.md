# Customer-Segmentation-Using-KMeans-PCA
📌 Project Description : This project demonstrates how unsupervised learning techniques can uncover hidden customer segments from raw behavioral data. By applying KMeans clustering and Principal Component Analysis (PCA), we identify distinct customer groups that can inform targeted marketing, personalized services, and strategic decision-making.


# 🚀 Key Features

Preprocessed raw customer dataset (handling missing values, scaling).

Applied K-Means clustering to segment customers.

Used PCA for visualization of high-dimensional data in 2D space.

Built an interactive Streamlit app for real-time segmentation.

# 📂 Dataset

The dataset contains customer attributes such as:

Age

Annual Income

Spending Score

Total Spending

Purchase behavior (online/store)

Recency (last purchase)

# 👉 You can use the Mall Customers Dataset or any retail dataset.
(Replace with your dataset link: e.g., Mall Customers Dataset on Kaggle
)

# 🛠️ Tech Stack

Python 🐍

Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, joblib

Dimensionality Reduction: PCA

Clustering Algorithm: K-Means

Deployment: Streamlit

# 📊 Workflow

Data Preprocessing

Handle missing values

Standardize features with StandardScaler

Feature Selection

Removed irrelevant columns (e.g., IDs)

Selected relevant features for clustering

Clustering with K-Means

Used Elbow Method & Silhouette Score to choose optimal clusters

Assigned cluster labels to each customer

PCA for Visualization

Reduced dimensions to 2 components

Visualized clusters in 2D

Deployment

Saved model & scaler (kmeans_model.pkl, scaler.pkl)

Built Streamlit app for predictions

# 📷 Visualizations

Elbow Method Plot (to determine optimal k)

PCA Scatter Plot (clusters visualized in 2D)

Cluster Insights (spending vs income, age distribution, etc.)

(Add screenshots here)

## ▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Jupyter Notebook (for training & EDA)
jupyter notebook

4️⃣ Run Streamlit App
streamlit run app.py

## 📌 Results


Cluster 0: 🛍️ High spenders
Cluster 1: 💻 Digital shoppers
Cluster 2: 🧊 Low engagement
Cluster 3: 📉 Drop-off

## 🌟 Future Improvements

Try other clustering algorithms (DBSCAN, Hierarchical).

Use advanced dimensionality reduction (t-SNE, UMAP).

Deploy as a web dashboard with Plotly for better visualizations.

## 🤝 Contributing

Contributions are welcome! Please fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License.
