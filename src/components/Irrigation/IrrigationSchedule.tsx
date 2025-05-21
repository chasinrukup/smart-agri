import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

interface IrrigationScheduleProps {
  scheduledTime?: string;
  durationMinutes?: number;
  status?: string;
  reason?: string;
}

const IrrigationSchedule: React.FC<IrrigationScheduleProps> = ({ scheduledTime, durationMinutes, status, reason }) => {
  return (
    <Card sx={{ minWidth: 275, marginBottom: 2 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Irrigation Schedule
        </Typography>
        <Typography>Next Scheduled: {scheduledTime ? new Date(scheduledTime).toLocaleString() : '--'}</Typography>
        <Typography>Duration: {durationMinutes ?? '--'} minutes</Typography>
        <Typography>Status: {status ?? '--'}</Typography>
        <Typography>Reason: {reason ?? '--'}</Typography>
      </CardContent>
    </Card>
  );
};

export default IrrigationSchedule; 