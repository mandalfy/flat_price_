# Flat Price Prediction Using Django

This project uses machine learning to predict the price of a flat based on various features and also calculates a feasibility score for the provided input data. The model is built using **Random Forest Regressor** and is deployed through a **Django web application**.

## Approach

- **Machine Learning Model**: 
  - We train a **Random Forest Regressor** on a dataset containing various features of flats and their corresponding prices. The model predicts flat prices based on user input.
  
- **Feasibility Score**: 
  - The feasibility score is calculated based on how closely the user's input aligns with the statistical properties of the dataset. If the values fall within a reasonable range (within two standard deviations of the feature mean), they are considered feasible.
  
- **Web Application**:
  - The application allows users to enter details like flat size, location, builder's rating, crime rate, floor number, etc., and the model returns the predicted price and feasibility score.

## Requirements

- Python 3.7+
- Django 3.2+
- Scikit-learn
- Pandas
- Numpy

Install required libraries with:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mandalfy/flat_price_predictor.git
   ```

2. **Install dependencies**:
   Navigate to the project directory and install required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations** (if applicable):
   ```bash
   python manage.py migrate
   ```

4. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

   Access the app at `http://127.0.0.1:8000/`.

## Features

- **Flat Price Prediction**: 
  - The user inputs various features (e.g., flat size, location, floor number) and the model predicts the price in lakhs.
  
- **Feasibility Score**: 
  - The feasibility score is calculated based on how the provided features align with the dataset. A score closer to 100 indicates high feasibility, meaning the provided data is within the normal range seen in the dataset.

## Usage

1. Navigate to the web application in your browser.
2. Input the following features for the flat:
   - **Flat Size**: e.g., 3BHK
   - **Location**: e.g., Mumbai
   - **Builder's Rating**: e.g., A/B/C
   - **Area Type**: e.g., Commercial
   - **Neighborhood Tier**: e.g., Mid-Tier
   - **Crime Rate**: Low/Medium/High
   - **Floor Number**: e.g., 10
   - **Age of Property**: e.g., 5
   - **Nearby Amenities**: Basic/Advanced
   - **Green Cover**: e.g., 0.5
   - **Market Demand**: e.g., 0.5
   - **Security Features**: Basic/Advanced
   - **RERA-Approved**: Yes/No
   - **Urban Integration Index**: e.g., 0.5

3. Click on **Predict Price** to receive:
   - **Predicted Price**: The price prediction for the flat.
   - **Feasibility Score**: A score (out of 100) indicating how feasible the given input is based on the model’s training data.

## Code Explanation

- **Data Preprocessing**: 
  - The dataset is loaded and processed using Pandas. Categorical variables are transformed into numerical ones via `pd.get_dummies()`.
  
- **Model Training**: 
  - A RandomForestRegressor is trained using the features from the dataset, and the model is tested on a separate 20% of the data.

- **Feasibility Calculation**: 
  - The feasibility score is calculated based on how close the input data is to the mean of each feature. If the values are within a reasonable range (within 2 standard deviations), the score increases.

- **Django Views**: 
  - The user input is processed via POST requests in the `home` function, and the predicted price and feasibility score are displayed on the results page.

## Model Details

The model uses **Random Forest Regressor** for the price prediction, a robust ensemble learning method that is suitable for regression tasks. The model is trained on features such as flat size, location, crime rate, floor number, and others. After training, the model is used to predict the price for unseen data.

## Folder Structure

```
.
├── predictor/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── manage.py
├── updated_flat_prices_dataset.csv
├── requirements.txt
└── flat_price_predictor/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Future Improvements

- **Model Improvement**: Implement other machine learning models or advanced techniques to improve prediction accuracy.
- **Frontend Improvements**: Enhance the user interface for a better experience.
- **Real-time Data**: Incorporate real-time data sources to dynamically update the predictions.

## License

This project is open-source and available under the MIT License. Feel free to contribute or suggest improvements.
