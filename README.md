# Smart HVAC Management System

An AI-powered Predictive Maintenance and Energy Optimization System for heating, ventilation, and air conditioning (HVAC) systems.

## Project Structure

```
Smart_HVAC_System/
│
├── datasets/                   # Raw and processed datasets (LBNL RTU, Building Genome, etc.)
│   ├── Fault_detect dataset/
│   └── Genome dataset/
│
├── notebooks/                  # Jupyter Notebooks for exploration and modeling
│   ├── 01_dataset_analysis.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_fault_model.ipynb
│   └── 06_energy_model.ipynb
│
├── src/                        # Source code for the HVAC system pipeline
│   ├── preprocessing/          # Data cleaning and ingestion
│   ├── features/               # Feature extraction and engineering
│   ├── models/                 # Model training and evaluation scripts
│   ├── analytics/              # Performance analytics and reporting
│   ├── utils/                  # Utility functions
│   └── config/                 # Configuration files and constants
│
├── backend/                    # Backend API (e.g., FastAPI, Flask)
├── frontend/                   # Frontend user interface (e.g., React, Vue)
├── models/                     # Saved model artifacts (serialized .pkl, .h5, etc.)
├── reports/                    # Generated project reports and analysis documentation
├── outputs/                    # Output logs, figures, and export files
└── README.md                   # Project documentation
```

## Getting Started

1. **Prerequisites**: Ensure you have Python 3.8+ installed.
2. **Environment Setup**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Data**: Place or verify raw datasets in the `datasets/` directory.
4. **Notebooks**: Use the `notebooks/` directory to run interactive analyses step-by-step.
