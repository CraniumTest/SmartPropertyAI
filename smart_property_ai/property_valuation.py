import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class PropertyValuation:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = RandomForestRegressor()
    
    def load_data(self):
        # Load data from CSV or any database connection
        self.data = pd.read_csv(self.data_path)
        print("Data Loaded.")

    def preprocess_data(self):
        # Basic preprocessing: handle missing values, encode categorical variables
        self.data.fillna(self.data.mean(), inplace=True)
        categorical_features = self.data.select_dtypes(include=['object']).columns
        self.data = pd.get_dummies(self.data, columns=categorical_features)
        print("Data Preprocessed.")

    def train_model(self):
        # Define features and target variable
        X = self.data.drop('Price', axis=1)
        y = self.data['Price']
        
        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the regression model
        self.model.fit(X_train, y_train)
        print("Model trained.")
        
        # Evaluate the model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print("Model evaluation completed with MSE:", mse)
