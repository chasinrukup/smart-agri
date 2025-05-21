# Smart Agriculture Dashboard 🌱

A modern, responsive web application for monitoring and managing agricultural data. Built with React, TypeScript, and Material-UI, this dashboard provides real-time insights into various agricultural parameters and crop recommendations.

## Cloud Architecture ☁️

### Overview
The Smart Agriculture Dashboard leverages AWS cloud services to provide a scalable, secure, and efficient IoT solution for agricultural monitoring.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  IoT Sensors    │────▶│  AWS IoT Core   │────▶│ Kinesis Streams │
│  (Temperature,  │     │                 │     │                 │
│   Humidity,     │     │                 │     │                 │
│   Soil Moisture)│     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  React Frontend │◀────│  API Gateway    │◀────│  Lambda         │
│  Dashboard      │     │                 │     │  Functions      │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │                 │
                                                │  DynamoDB       │
                                                │  (Sensor Data)  │
                                                │                 │
                                                └─────────────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │                 │
                                                │  S3             │
                                                │  (Historical    │
                                                │   Data/Reports) │
                                                │                 │
                                                └─────────────────┘
```

### Cloud Services Used

1. **AWS IoT Core**
   - Manages IoT device connections
   - Handles real-time sensor data ingestion
   - Provides secure device authentication
   - Enables bi-directional communication

2. **Amazon Kinesis Streams**
   - Processes real-time sensor data streams
   - Enables data analytics and processing
   - Provides scalable data ingestion
   - Maintains data order and durability

3. **AWS Lambda**
   - Serverless compute for data processing
   - Handles sensor data aggregation
   - Generates crop recommendations
   - Manages business logic

4. **Amazon DynamoDB**
   - Stores real-time sensor readings
   - Manages user preferences
   - Handles device metadata
   - Provides fast, scalable data access

5. **Amazon S3**
   - Stores historical sensor data
   - Archives reports and analytics
   - Hosts static frontend assets
   - Manages backup data

6. **Amazon API Gateway**
   - Provides RESTful API endpoints
   - Manages API authentication
   - Handles request/response routing
   - Enables API versioning

### Security & Compliance
- AWS IoT Core device authentication
- API Gateway authentication
- DynamoDB encryption at rest
- S3 bucket policies
- IAM role-based access control
- CloudWatch monitoring and logging

### Scalability
- Auto-scaling Lambda functions
- DynamoDB on-demand capacity
- Kinesis stream sharding
- S3 unlimited storage
- CloudFront CDN for global access

## Features 🌟

- **Real-time Sensor Data Monitoring**
  - Temperature tracking
  - Humidity levels
  - Soil moisture measurements
  - Atmospheric pressure readings

- **Interactive Dashboard**
  - Responsive grid layout
  - Real-time data visualization
  - Historical data charts
  - Dark/Light theme support

- **Crop Recommendations**
  - AI-powered crop suggestions
  - Confidence scoring
  - Growing condition details
  - Seasonal recommendations

## Tech Stack 💻

- **Frontend**
  - React 18
  - TypeScript
  - Material-UI (MUI)
  - React Router
  - Chart.js for data visualization

- **Development Tools**
  - Node.js
  - npm
  - ESLint
  - TypeScript

## Getting Started 🚀

### Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chasinrukup/smart-agri.git
   cd smart-agri
   ```

2. Install dependencies:
   ```bash
   cd smart-agri-frontend
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The application will be available at `http://localhost:3000`

## Project Structure 📁

```
smart-agri/
├── smart-agri-frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Layout/
│   │   │   ├── Charts/
│   │   │   ├── SensorData/
│   │   │   └── Recommendations/
│   │   ├── pages/
│   │   ├── theme/
│   │   └── utils/
│   ├── public/
│   └── package.json
└── README.md
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📧

Sachin Rukup - [@chasinrukup](https://github.com/chasinrukup)

Project Link: [https://github.com/chasinrukup/smart-agri](https://github.com/chasinrukup/smart-agri)

## Acknowledgments 🙏

- Material-UI for the component library
- React team for the amazing framework
- All contributors who have helped shape this project

---

Made with ❤️ by [Sachin Rukup](https://github.com/chasinrukup) 