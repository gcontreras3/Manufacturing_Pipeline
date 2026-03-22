# Manufacturing Data Automation Pipeline

## Overview

This project is a Python-based automation pipeline that simulates manufacturing machine telemetry, processes and analyzes the data, detects anomalies, and stores results in a PostgreSQL database. The application is containerized using Docker to ensure consistent execution across environments.

The goal of this project is to model real-world automation and data workflows commonly found in manufacturing and production systems.

---

## Features

* Simulates machine telemetry data (temperature, pressure, cycle time)
* Processes and aggregates data using Polars
* Performs statistical analysis and anomaly detection using NumPy
* Stores processed results in PostgreSQL
* Containerized with Docker for portability and consistency

---

## Tech Stack

* **Python**
* **Polars** – Data processing and transformation
* **NumPy** – Numerical computation and anomaly detection
* **PostgreSQL** – Persistent data storage
* **Docker** – Containerization

---

## Project Structure

```
automation-pipeline/
│
├── app/
│   ├── main.py            # Entry point for pipeline
│   ├── data_generator.py  # Simulates machine data
│   ├── processor.py       # Data processing and aggregation
│   ├── db.py              # PostgreSQL integration
│   └── utils.py           # (Optional) helper functions
│
├── data/                  # Generated CSV data
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container configuration
└── README.md
```

---

## How It Works

1. **Data Generation**

   * Simulates machine telemetry including temperature, pressure, and cycle time.

2. **Data Processing**

   * Loads data using Polars
   * Cleans and aggregates metrics by machine
   * Computes averages and maximum values

3. **Anomaly Detection**

   * Uses statistical thresholds (mean + standard deviation)
   * Flags abnormal machine behavior

4. **Data Persistence**

   * Stores processed results in PostgreSQL for querying and analysis

5. **Containerization**

   * Application runs inside Docker for consistent environments

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd automation-pipeline
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4. Set Up PostgreSQL

Create database:

```sql
CREATE DATABASE manufacturing_pipeline;
```

Create table:

```sql
CREATE TABLE machine_metrics (
    id SERIAL PRIMARY KEY,
    machine_id VARCHAR(50),
    avg_temp DOUBLE PRECISION,
    max_temp DOUBLE PRECISION,
    max_pressure DOUBLE PRECISION,
    avg_cycle_time DOUBLE PRECISION,
    anomaly BOOLEAN
);
```

---

### 5. Run the Application

```bash
cd app
python main.py
```

---

## Running with Docker

### Build the image:

```bash
docker build -t manufacturing-pipeline .
```

### Run the container:

```bash
docker run manufacturing-pipeline
```

> Note: On macOS, database host may need to be set to `host.docker.internal`

---

## Verification

To verify data insertion:

```bash
psql -d manufacturing_pipeline
```

```sql
SELECT * FROM machine_metrics ORDER BY id DESC;
```

---

## Challenges & Learnings

* Resolved Python import and module structure issues
* Configured PostgreSQL connectivity and schema setup
* Debugged Docker container networking (host vs container localhost)
* Learned how to integrate data processing with persistent storage

---

## Future Improvements

* Add environment variable configuration for database credentials
* Implement retry logic for database connections
* Expand anomaly detection using SciPy
* Add logging and monitoring
* Build a simple dashboard for data visualization

---

## Summary

This project demonstrates how automation, data processing, and system integration come together to create a production-style workflow. It highlights key skills in Python, data engineering, system troubleshooting, and containerization.

---
