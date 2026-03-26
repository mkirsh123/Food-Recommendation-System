import streamlit as st
import numpy as np
from model import load_and_train, get_recommendations

st.set_page_config(page_title="Food Recommender", layout="wide")
st.title("Food Recipe Recommender")
st.write("Set your nutrition targets and get matching recipes.")

# Load model only once — Streamlit caches this across all users
@st.cache_resource
def init():
    return load_and_train("recipes.csv")

data, scaler, neigh = init()

# --- Sidebar inputs ---
st.sidebar.header("Your nutrition targets")

calories  = st.sidebar.slider("Calories",          0, 2000, 500)
fat       = st.sidebar.slider("Fat (g)",            0, 100,  30)
sat_fat   = st.sidebar.slider("Saturated fat (g)",  0, 13,   5)
cholest   = st.sidebar.slider("Cholesterol (mg)",   0, 300,  100)
sodium    = st.sidebar.slider("Sodium (mg)",         0, 2300, 800)
carbs     = st.sidebar.slider("Carbohydrates (g)",  0, 325,  100)
fiber     = st.sidebar.slider("Fiber (g)",           0, 40,   10)
sugar     = st.sidebar.slider("Sugar (g)",           0, 40,   10)
protein   = st.sidebar.slider("Protein (g)",         0, 200,  30)

ingredient = st.sidebar.text_input("Must contain ingredient (optional)", placeholder="e.g. chicken")

search = st.sidebar.button("Find recipes")

# --- Results ---
if search:
    user_input = np.array([[calories, fat, sat_fat, cholest, sodium, carbs, fiber, sugar, protein]])
    
    ingredient_filter = [ingredient] if ingredient.strip() else None
    results = get_recommendations(data, scaler, neigh, user_input, ingredient_filter)
    
    if results.empty:
        st.warning("No recipes found. Try relaxing the ingredient filter.")
    else:
        st.success(f"Found {len(results)} recipes!")
        for _, row in results.iterrows():
            with st.expander(f"{row['Name']}"):
                col1, col2, col3 = st.columns(3)
                col1.metric("Calories",  f"{row['Calories']:.0f} kcal")
                col2.metric("Protein",   f"{row['ProteinContent']:.1f} g")
                col3.metric("Carbs",     f"{row['CarbohydrateContent']:.1f} g")
                
                col4, col5, col6 = st.columns(3)
                col4.metric("Fat",       f"{row['FatContent']:.1f} g")
                col5.metric("Fiber",     f"{row['FiberContent']:.1f} g")
                col6.metric("Sugar",     f"{row['SugarContent']:.1f} g")
                
                st.markdown("**Ingredients**")
                st.write(row['RecipeIngredientParts'])
                
                st.markdown("**Instructions**")
                st.write(row['RecipeInstructions'])