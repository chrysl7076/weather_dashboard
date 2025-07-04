## Internship: CodTech Technologies - Python Internship
## Duration: 5th June - 5th July
## TASK 1: API INTEGRATION AND DATA VISUALIZATION

## Use Python to Fetch Data from a public API(e.g. OpemWeatherMap) and create visualizations using matplotlib or seaborn 
## Deliverable: A script and a visualization dashboard

## NAME - CHRYSL SHECKINA THOMAS 
## INTERN ID - CT04DG328 
## DOMAIN - PYTHON PROGRAMMING 
## DURATION - 4 WEEKS 
## MENTOR - MS. NEELA SANTHOSH KUMAR

## DESCRIPTION BELOW SCREENSHOTS

Screenshots

Combined Dashboard
![Combined Dashboard](static/weather_combined_dashboard.png)

Sample City Dashboard
![Delhi Dashboard](static/dashboard_1_Delhi.png)

## Objective:
The objective of this task was to integrate a public API using Python and visualize the fetched data through meaningful and aesthetic dashboards. Specifically, the project focused on real time weather data using the OpenWeatherMap API and its presentation through data visualization tools like matplotlib and seaborn. The goal was not only to fetch and present the data but also to build a dynamic and interactive user facing web application using the Flask framework.

## API Integration:
Using the OpenWeatherMap API, current weather data and 5 day forecasts were fetched programmatically for 10 major Indian cities. The data included key parameters such as: 

- Temperature
- Humidity
- Weather conditions
- Wind Speed 
- Time based forecast data

To make the solution scalable and adaptable, the API requests were dynamically structured using lopped city names, and responses were parsed using Python's requests and JSON libraries. Error handling was also implemented to deal with any failed API calls, incorrect city names, or rate limit errors. 

## Data Visualization
The core of the task was transforming ra JSON data into human readable visual content. This was achieved using the matplotlib library for plotting. For each city, two charts were generated:

1. Current Weather Overview: A bar showing temperature, humidity, am wind speed. 
2. 5 day Temperature trend: A line chart showing forecasted temperature over time. 

These charts were saved as PNG images into a static/ folder for web access. 

An additional challenge was combining all individual city charts into a single dashboard. Using Python's PIL(Pillow) Library, all images were programmatically stitched into a grid layout (5 cities x 2 rows) forming a combined dashboard image. 

## Web Dashboard with Flask 
To provide user friendly interface, a Flask application was created(app.py). this lightweight Python web server loaded all city images and rendered them in styled HTML template(templates/index.html). Features included:
- Viewing all individual dashboard per city 
- Displaying the combined dashboard
- Providing download buttons for each chart
- Adding optional input for custom city name(via text box)

The dashboard dynamically loaded images from the static/ folder and presented them in a clean scrollable layout with image label for clarity. 

## Challenges faced and solutions
API Failures : Resolved using conditional error checking and retry mechanisms

Layout Issues: Used PIL to align and scale images uniformly in the combined view

Image Management: Implemented naming conventions like dashboard_1_Delhi.png for automation

## Learning Outcomes: 

- Hands on experience with public API consumption
- Improved skills in parsing and handling JSON 
- Mastery of data visualization using matplotlib
- Experience in serving visual content through Flask
- Practice with organizing and automating Python Projects

This project stimulated a real world scenario of transforming raw live data into a visually engaging and downloadable dashboard. By combining Python scripting, API integration, data visualization and Flask web app development capabilities. It was a valuable experience that strengthened both backend logic and frontend presentation skills. 

## Tech Stack

- Python 3.13.2
- Flask  
- Matplotlib  
- HTML/CSS  
- OpenWeatherMap API

---


## How to run

## Clone the repository
```bash
git clone https://github.com/chrysl7076/weather_dashboard.git
cd weather_dashboard

