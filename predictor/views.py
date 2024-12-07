#Group 2(Flat price predictor with feasibilty calculator)
#group members
#Avinish-Group Leader(ML logic for finding the flat's price)
#Shibham-FrontEnd as well modifying some backend logics.
#Rahul-Debugging 
#Nitin-Makes code prettier and add comments for easy understanding and perform alpha testing

from django.shortcuts import render   
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load the dataset of flat prices
data = pd.read_csv('updated_flat_prices_dataset.csv')

# Preprocess the data
data = pd.get_dummies(data, drop_first=True)
X = data.drop('Flat Price (in Lakhs)', axis=1, errors='ignore')
y = data.get('Flat Price (in Lakhs)')

# This is for train the model here we used the randomForestregressor model for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

 # The Feasibility Score is a numerical rating that reflects the overall feasibility of a project
def calculate_feasibility(input_data, dataset):
    score = 0
    total_features = len(input_data)
    
    for feature, value in input_data.items():
        if feature in dataset.columns:
            feature_mean = dataset[feature].mean()
            feature_std = dataset[feature].std()
            
            if isinstance(value, (int, float)):
                if feature_mean - 2 * feature_std <= value <= feature_mean + 2 * feature_std:
                    score += 1
            else:
                if value in dataset[feature].unique():
                    score += 1
    
    feasibility_score = (score / total_features) * 100
    return feasibility_score

def predict_price(input_data):
    input_df = pd.DataFrame([input_data])
    input_df = pd.get_dummies(input_df, drop_first=True)
    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    predicted_price = model.predict(input_df)[0]
    feasibility_score = calculate_feasibility(input_data, data)

    return predicted_price, feasibility_score

#This part is for the input from user that what the features they are looking in the flat
def home(request):
    if request.method == 'POST':
        input_data = {           
            'Flat Size': request.POST.get('flat_size'),
            'Location': request.POST.get('location'),
            'Builder\'s Rating': request.POST.get('builder_rating'),
            'Area Type': request.POST.get('area_type'),
            'Neighborhood Tier': request.POST.get('neighborhood_tier'),
            'Crime Rate': request.POST.get('crime_rate'),
            'Floor Number': int(request.POST.get('floor_number')),
            'Age of Property': int(request.POST.get('age_of_property')),
            'Nearby Amenities': request.POST.get('nearby_amenities'),
            'Green Cover': float(request.POST.get('green_cover')),
            'Market Demand': float(request.POST.get('market_demand')),
            'Security Features': request.POST.get('security_features'),
            'RERA-Approved': int(request.POST.get('rera_approved')),
            'Urban Integration Index': float(request.POST.get('urban_integration_index')),
        }
        
        predicted_price, feasibility_score = predict_price(input_data)#This is for predicting price and for feasibility score-
                                                                       
        return render(request, 'predictor/result.html', {
            'predicted_price': round(predicted_price, 2),
            'feasibility_score': round(feasibility_score, 2),
        })
    
    return render(request, 'predictor/home.html')

