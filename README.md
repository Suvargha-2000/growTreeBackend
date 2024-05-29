# Flask SQLite API

## Introduction
This repository contains a Flask API for interacting with a SQLite database. The API allows users to post data and retrieve data from the database based on specified date ranges.

## Features
- **SQLite Database:** Utilizes SQLite3 for data storage, ensuring a lightweight and portable solution.
- **RESTful API:** Implements a RESTful API using Flask, allowing seamless interaction with the database through HTTP requests.
- **Data Posting:** Enables users to post temperature, moisture, and soil moisture data to the database.
- **Data Retrieval:** Provides functionality to retrieve data from the database based on specified date ranges.

## Endpoints
- **/postData:** POST endpoint for posting temperature, moisture, and soil moisture data to the database.
- **/retData:** POST endpoint for retrieving data from the database based on specified start and end dates.

## Setup
1. Clone the repository: `git clone https://github.com/Suvargha-2000/growTreeBackend.git`
2. Install dependencies: `pip install -r req.txt`
3. Run the Flask application: `python app.py`

## Usage
- To post data to the database, send a POST request to `/postData` with JSON containing temperature (`temp`), moisture (`moisture`), and soil moisture (`smoisture`) values.
- To retrieve data from the database, send a POST request to `/retData` with JSON containing start date (`sDate`) and end date (`eDate`) values.

## Technologies Used
- ![Flask](https://img.shields.io/badge/-Flask-lightgrey?style=flat-square&logo=flask&logoColor=white)
- ![SQLite](https://img.shields.io/badge/-SQLite-blue?style=flat-square&logo=sqlite&logoColor=white)
- ![Python](https://img.shields.io/badge/-Python-yellow?style=flat-square&logo=python&logoColor=white)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- Suvargha
