import React from 'react';
import { Card, CardContent, Typography, List, ListItem, ListItemText } from '@mui/material';

interface CropRecommendation {
  name: string;
  confidence: number;
  suitable_conditions: string;
}

interface CropRecommendationsProps {
  recommendations: CropRecommendation[];
}

const CropRecommendations: React.FC<CropRecommendationsProps> = ({ recommendations }) => {
  return (
    <Card sx={{ minWidth: 275, marginBottom: 2 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Crop Recommendations
        </Typography>
        <List>
          {recommendations.map((rec, idx) => (
            <ListItem key={idx} divider>
              <ListItemText
                primary={`${rec.name} (${(rec.confidence * 100).toFixed(1)}%)`}
                secondary={rec.suitable_conditions}
              />
            </ListItem>
          ))}
        </List>
      </CardContent>
    </Card>
  );
};

export default CropRecommendations; 