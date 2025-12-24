# Fuel Route Optimization API (Django)

# Overview
This API calculates an optimal driving route between two US locations and determines cost-effective fuel stops along the route based on fuel prices.

# Tech Stack
Django 5+
OpenRouteService API
Pandas
SQLite

# Features
Route calculation using external routing API
Fuel cost optimization
Supports vehicles with 500 mile range
Returns total fuel cost and fuel stop details

# Setup Instructions

```bash
git clone <repo>
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
