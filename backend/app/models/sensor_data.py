from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    soil_moisture = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    sensor_id = Column(String, nullable=False, index=True)
    location = Column(String, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "temperature": self.temperature,
            "humidity": self.humidity,
            "soil_moisture": self.soil_moisture,
            "pressure": self.pressure,
            "sensor_id": self.sensor_id,
            "location": self.location
        }

class CropRecommendation(Base):
    __tablename__ = "crop_recommendations"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    crop_name = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    soil_temperature = Column(Float, nullable=False)
    soil_humidity = Column(Float, nullable=False)
    soil_moisture = Column(Float, nullable=False)
    soil_ph = Column(Float, nullable=False)
    location = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "crop_name": self.crop_name,
            "confidence": self.confidence,
            "soil_conditions": {
                "temperature": self.soil_temperature,
                "humidity": self.soil_humidity,
                "moisture": self.soil_moisture,
                "ph": self.soil_ph
            },
            "location": self.location
        }

class IrrigationSchedule(Base):
    __tablename__ = "irrigation_schedules"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    scheduled_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    status = Column(String, nullable=False)  # 'scheduled', 'completed', 'cancelled'
    reason = Column(String, nullable=False)
    location = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "scheduled_time": self.scheduled_time.isoformat(),
            "duration_minutes": self.duration_minutes,
            "status": self.status,
            "reason": self.reason,
            "location": self.location
        } 