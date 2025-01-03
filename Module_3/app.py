from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model = pickle.load(open('best_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form

    # Convert dropdown values into dummy variables
    seller_type = form_data['seller_type']
    fuel_type = form_data['fuel_type']
    transmission_type = form_data['transmission_type']
    
    # Dummy variables for seller_type
    seller_type_dummies = {'Dealer': 0, 'Individual': 0, 'Trustmark Dealer': 0}
    seller_type_dummies[seller_type] = 1

    # Dummy variables for fuel_type
    fuel_type_dummies = {'CNG': 0, 'Diesel': 0, 'Electric': 0, 'LPG': 0, 'Petrol': 0}
    fuel_type_dummies[fuel_type] = 1

    # Dummy variables for transmission_type
    transmission_type_dummies = {'Automatic': 0, 'Manual': 0}
    transmission_type_dummies[transmission_type] = 1

    # Get the remaining form data
    input_features = [
        int(form_data['vehicle_age']),
        int(form_data['km_driven']),
        float(form_data['mileage']),
        int(form_data['engine']),
        float(form_data['max_power']),
        int(form_data['seats']),
        seller_type_dummies['Dealer'],
        seller_type_dummies['Individual'],
        seller_type_dummies['Trustmark Dealer'],
        fuel_type_dummies['CNG'],
        fuel_type_dummies['Diesel'],
        fuel_type_dummies['Electric'],
        fuel_type_dummies['LPG'],
        fuel_type_dummies['Petrol'],
        transmission_type_dummies['Automatic'],
        transmission_type_dummies['Manual']
    ]
    
    # Convert the input into a NumPy array for prediction
    final_features = [np.array(input_features)]
    
    # Predict the price using the model
    predicted_price = model.predict(final_features)
    
    # Render the result on the webpage
    return render_template('index.html', prediction_text=f'Predicted Selling Price: ₹{round(predicted_price[0], 2)}')

if __name__ == "__main__":
    app.run(debug=True, host="localhost",port=8001)
