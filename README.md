# Smart Agriculture System

An intelligent farming system that combines IoT sensors, cloud storage, and AI/ML to provide data-driven insights for modern agriculture.

## Features

- Real-time monitoring of soil conditions (temperature, humidity, moisture, pressure)
- AI-powered crop recommendations based on soil conditions
- Yield prediction using machine learning
- Smart irrigation scheduling
- Interactive dashboard for monitoring and insights
- Cloud-based data storage and analysis

## Tech Stack

### Backend
- Python 3.9+
- FastAPI (Web framework)
- SQLAlchemy (Database ORM)
- Scikit-learn (ML models)
- Pandas (Data processing)
- PostgreSQL (Database)

### Frontend
- React
- TypeScript
- Material-UI
- Chart.js (Data visualization)
- Axios (API client)

## Project Structure

```
smart-agri/
├── backend/          # FastAPI backend
├── frontend/         # React frontend
└── README.md         # This file
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL
- Docker (optional)

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 