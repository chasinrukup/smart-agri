import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

interface SensorDataProps {
  temperature?: number;
  humidity?: number;
  soilMoisture?: number;
  pressure?: number;
  timestamp?: string;
}

const SensorDataCard: React.FC<SensorDataProps> = ({ temperature, humidity, soilMoisture, pressure, timestamp }) => {
  return (
    <Card sx={{ minWidth: 275, marginBottom: 2 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Real-Time Sensor Data
        </Typography>
        <Typography>Temperature: {temperature ?? '--'} °C</Typography>
        <Typography>Humidity: {humidity ?? '--'} %</Typography>
        <Typography>Soil Moisture: {soilMoisture ?? '--'} %</Typography>
        <Typography>Pressure: {pressure ?? '--'} hPa</Typography>
        <Typography variant="caption" color="text.secondary">
          Last updated: {timestamp ? new Date(timestamp).toLocaleString() : '--'}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default SensorDataCard; 