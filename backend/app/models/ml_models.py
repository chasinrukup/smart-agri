import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os
from typing import List, Dict, Any
import pandas as pd

class CropRecommendationModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        self.model_path = "app/models/saved/crop_recommendation_model.joblib"
        self.scaler_path = "app/models/saved/crop_scaler.joblib"
        
        # Try to load existing model
        self._load_model()

    def _load_model(self):
        """Load the trained model and scaler if they exist"""
        try:
            if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
                self.model = joblib.load(self.model_path)
                self.scaler = joblib.load(self.scaler_path)
                self.is_trained = True
        except Exception as e:
            print(f"Error loading model: {e}")
            self.is_trained = False

    def _save_model(self):
        """Save the trained model and scaler"""
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(self.model, self.model_path)
            joblib.dump(self.scaler, self.scaler_path)
        except Exception as e:
            print(f"Error saving model: {e}")

    def train(self, training_data: pd.DataFrame):
        """
        Train the model with historical data
        
        Parameters:
        training_data: DataFrame with columns:
            - temperature
            - humidity
            - soil_moisture
            - soil_ph
            - crop_name (target variable)
        """
        try:
            # Prepare features and target
            X = training_data[['temperature', 'humidity', 'soil_moisture', 'soil_ph']]
            y = training_data['crop_name']
            
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            # Train model
            self.model.fit(X_scaled, y)
            self.is_trained = True
            
            # Save model
            self._save_model()
            
            return True
        except Exception as e:
            print(f"Error training model: {e}")
            return False

    def predict(self, soil_conditions: Dict[str, float]) -> List[Dict[str, Any]]:
        """
        Predict suitable crops based on soil conditions
        
        Parameters:
        soil_conditions: Dictionary with keys:
            - temperature
            - humidity
            - soil_moisture
            - soil_ph
            
        Returns:
        List of dictionaries containing crop recommendations with confidence scores
        """
        if not self.is_trained:
            return [{
                "name": "Model not trained",
                "confidence": 0.0,
                "suitable_conditions": "Please train the model first"
            }]

        try:
            # Prepare input data
            X = np.array([[
                soil_conditions['temperature'],
                soil_conditions['humidity'],
                soil_conditions['soil_moisture'],
                soil_conditions['soil_ph']
            ]])
            
            # Scale features
            X_scaled = self.scaler.transform(X)
            
            # Get prediction probabilities
            probabilities = self.model.predict_proba(X_scaled)[0]
            
            # Get top 3 recommendations
            top_indices = np.argsort(probabilities)[-3:][::-1]
            recommendations = []
            
            for idx in top_indices:
                if probabilities[idx] > 0.1:  # Only include if confidence > 10%
                    recommendations.append({
                        "name": self.model.classes_[idx],
                        "confidence": float(probabilities[idx]),
                        "suitable_conditions": self._get_conditions_description(
                            self.model.classes_[idx],
                            soil_conditions
                        )
                    })
            
            return recommendations
        except Exception as e:
            print(f"Error making prediction: {e}")
            return [{
                "name": "Error",
                "confidence": 0.0,
                "suitable_conditions": f"Error making prediction: {str(e)}"
            }]

    def _get_conditions_description(self, crop_name: str, conditions: Dict[str, float]) -> str:
        """Generate a human-readable description of why a crop is suitable"""
        # This is a simplified version - in a real system, you would have more
        # detailed crop requirements and more sophisticated analysis
        return (
            f"Current conditions (Temp: {conditions['temperature']}°C, "
            f"Humidity: {conditions['humidity']}%, "
            f"Moisture: {conditions['soil_moisture']}%, "
            f"pH: {conditions['soil_ph']}) are suitable for {crop_name}"
        )

# Create a singleton instance
crop_recommendation_model = CropRecommendationModel() 