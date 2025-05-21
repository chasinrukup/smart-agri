import React from 'react';
import DashboardLayout from '../components/Layout/DashboardLayout';
import SensorDataCard from '../components/SensorData/SensorDataCard';
import HistoricalChart from '../components/Charts/HistoricalChart';
import CropRecommendations from '../components/Recommendations/CropRecommendations';
import IrrigationSchedule from '../components/Irrigation/IrrigationSchedule';

const Dashboard: React.FC = () => {
  // Placeholder data
  const sensorData = {
    temperature: 25.5,
    humidity: 65.0,
    soilMoisture: 45.0,
    pressure: 1013.2,
    timestamp: new Date().toISOString(),
  };

  const historicalLabels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  const historicalData = [24, 25, 23, 26, 27, 25, 24];

  const cropRecommendations = [
    { name: 'Tomato', confidence: 0.85, suitable_conditions: 'Optimal for tomatoes.' },
    { name: 'Bell Pepper', confidence: 0.75, suitable_conditions: 'Good, but monitor soil moisture.' },
  ];

  const irrigationSchedule = {
    scheduledTime: new Date(Date.now() + 3600 * 1000).toISOString(),
    durationMinutes: 30,
    status: 'Scheduled',
    reason: 'Soil moisture below optimal level',
  };

  return (
    <DashboardLayout>
      <SensorDataCard {...sensorData} />
      <HistoricalChart labels={historicalLabels} data={historicalData} label="Temperature" />
      <CropRecommendations recommendations={cropRecommendations} />
      <IrrigationSchedule {...irrigationSchedule} />
    </DashboardLayout>
  );
};

export default Dashboard; 