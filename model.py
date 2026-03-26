import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

max_list = [2000, 100, 13, 300, 2300, 325, 40, 40, 200]

def load_and_train(csv_path="recipes.csv"):
    data = pd.read_csv(csv_path)
    
    columns = [
        'RecipeId', 'Name', 'CookTime', 'PrepTime', 'TotalTime',
        'RecipeIngredientParts', 'Calories', 'FatContent', 'SaturatedFatContent',
        'CholesterolContent', 'SodiumContent', 'CarbohydrateContent',
        'FiberContent', 'SugarContent', 'ProteinContent', 'RecipeInstructions'
    ]
    data = data[columns]
    
    # Filter out recipes exceeding daily max values
    for col, max_val in zip(data.columns[6:15], max_list):
        data = data[data[col] < max_val]
    
    # Fit scaler and model ONCE
    scaler = StandardScaler()
    prep_data = scaler.fit_transform(data.iloc[:, 6:15].to_numpy())
    
    neigh = NearestNeighbors(metric='cosine', algorithm='brute')
    neigh.fit(prep_data)
    
    return data, scaler, neigh


def get_recommendations(data, scaler, neigh, user_input, ingredient_filter=None, n=10):
    scaled = scaler.transform(user_input)
    _, indices = neigh.kneighbors(scaled, n_neighbors=n)
    results = data.iloc[indices[0]]
    
    if ingredient_filter:
        for ingredient in ingredient_filter:
            results = results[
                results['RecipeIngredientParts'].str.contains(ingredient, case=False, regex=False)
            ]
    
    return results