# 🍽️ Food Recipe Recommender (ML-Based)

An intelligent food recommendation system that suggests recipes based on user-defined nutritional targets such as calories, fats, protein, sugar, etc.

Built using Machine Learning (K-Nearest Neighbors) and deployed using Streamlit on Hugging Face Spaces.

---

## 🚀 Live Demo
👉 https://huggingface.co/spaces/RamaKrishnaReddy/food-recommender

## 🚀 Dataset
👉 https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions
---

## 📌 Features

- 🎯 Recommend recipes based on nutritional constraints
- 🥗 Supports filters like:
  - Calories
  - Fat
  - Saturated Fat
  - Cholesterol
  - Sodium
  - Carbohydrates
  - Fiber
  - Sugar
  - Protein
- 🔍 Ingredient-based filtering (e.g., chicken, egg)
- ⚡ Fast recommendations using KNN (cosine similarity)
- 🌐 Deployed online using Streamlit + Hugging Face

---

## 🧠 Machine Learning Approach

- **Model Used:** K-Nearest Neighbors (KNN)
- **Similarity Metric:** Cosine Similarity
- **Why KNN?**
  - Works well for similarity-based recommendation
  - No training phase required (lazy learning)
  - Efficient for structured numerical data

---

## 📊 Dataset

- Source: Food.com Recipes Dataset
- Contains:
  - 500K+ recipes
  - Nutritional information
  - Ingredients
  - Instructions

---

## ⚙️ Tech Stack

- **Languages:** Python
- **Libraries:**
  - pandas, numpy
  - scikit-learn
  - matplotlib, scipy
  - Streamlit
- **Deployment:**
  - Hugging Face Spaces
  - Docker

---

## 🏗️ Project Workflow

1. **Data Loading**
   - Loaded dataset using pandas

2. **Data Cleaning & Filtering**
   - Removed recipes exceeding daily nutritional limits

3. **Feature Selection**
   - Selected nutritional columns for recommendation

4. **Feature Scaling**
   - Standardized data using `StandardScaler`

5. **Model Building**
   - Applied KNN with cosine similarity

6. **Pipeline Creation**
   - Combined scaling + model using sklearn Pipeline

7. **Recommendation**
   - Returns top 10 similar recipes

8. **Deployment**
   - Built UI with Streamlit
   - Hosted on Hugging Face Spaces

---

## 🧪 Example

Input:
