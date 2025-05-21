from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random
from ..models.sensor_data import SensorData, CropRecommendation, IrrigationSchedule

# Use SQLite in-memory database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# Create SQLAlchemy engine with SQLite-specific settings
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize the database with dummy data"""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # Check if we already have data
        if db.query(SensorData).first():
            return

        # Create dummy sensor data
        locations = ["Field A", "Field B", "Greenhouse 1"]
        sensor_ids = [f"SENSOR_{i:03d}" for i in range(1, 4)]
        sensor_data = [
            SensorData(
                temperature=random.uniform(20, 30),
                humidity=random.uniform(40, 80),
                soil_moisture=random.uniform(30, 70),
                pressure=random.uniform(980, 1020),
                sensor_id=random.choice(sensor_ids),
                location=random.choice(locations),
                timestamp=datetime.now() - timedelta(hours=i)
            )
            for i in range(24)  # Last 24 hours of data
        ]
        db.add_all(sensor_data)

        # Create dummy crop recommendations
        crops = ["Tomato", "Potato", "Corn", "Wheat", "Rice"]
        recommendations = [
            CropRecommendation(
                crop_name=random.choice(crops),
                confidence=random.uniform(0.7, 0.95),
                soil_temperature=random.uniform(18, 28),
                soil_humidity=random.uniform(40, 80),
                soil_moisture=random.uniform(30, 70),
                soil_ph=round(random.uniform(5.5, 7.5), 1),
                location=random.choice(locations),
                timestamp=datetime.now()
            )
            for _ in range(5)  # 5 different recommendations
        ]
        db.add_all(recommendations)

        # Create dummy irrigation schedule
        irrigation_schedule = IrrigationSchedule(
            scheduled_time=datetime.now() + timedelta(hours=2),
            duration_minutes=30,
            status="scheduled",
            reason="Soil moisture below optimal level",
            location=random.choice(locations),
            timestamp=datetime.now()
        )
        db.add(irrigation_schedule)

        db.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

# Initialize the database when the module is imported
init_db() 