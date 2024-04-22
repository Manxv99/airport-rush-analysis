import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Step 1: Data Preprocessing and Model Training
def train_model(data_file):
    # Read CSV file into DataFrame
    data = pd.read_csv(data_file)
    
    # Extract features
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
    data['Day_of_Week'] = data['Date'].dt.dayofweek
    data['Hour_of_Day'] = pd.to_datetime(data['Time']).dt.hour
    
    # Select features and target variable
    X = data[['Day_of_Week', 'Hour_of_Day', 'Gate Number']]
    y = data['Number of Passangers']
    
    # Train the model
    model = RandomForestRegressor()
    model.fit(X, y)
    
    # Get feature names
    feature_names = X.columns.tolist()
    
    return model, feature_names

# Train the model using the provided data file
model, feature_names = train_model('rushdata.csv')

# Step 2: Prediction
def predict_passengers(model, feature_names, gate_number, date_of_travel, time_of_travel):
    # Extract features from date and time
    day_of_week = date_of_travel.dayofweek
    hour_of_day = time_of_travel.hour
    
    # Make prediction
    prediction = model.predict([[day_of_week, hour_of_day, gate_number]])
    
    return prediction, feature_names

# Example usage
input_gate_number = input("Enter gate number:")

dateinput = input("Enter date in the format: yyyy-mm-dd\n")
timeinput = input("Enter time in the format: hh:mm:ss\n")
input_date_of_travel = pd.to_datetime(dateinput)
input_time_of_travel = pd.to_datetime(timeinput)

predicted_passengers, feature_names = predict_passengers(model, feature_names, input_gate_number, input_date_of_travel, input_time_of_travel)
print("Predicted number of passengers:", predicted_passengers)
