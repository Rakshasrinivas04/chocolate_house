# Chocolate House Management Application

## Overview
This Python application manages seasonal flavor offerings, ingredient inventory, and customer flavor suggestions and allergy concerns for a fictional chocolate house. The application uses SQLite for data management and can be run in a Docker container. The interface is command-line based, allowing users to add flavors, manage ingredients, and review customer suggestions.

---

## Project Structure
# Chocolate House Management Application

## Overview
This Python application manages seasonal flavor offerings, ingredient inventory, and customer flavor suggestions and allergy concerns for a fictional chocolate house. The application uses SQLite for data management and can be run in a Docker container. The interface is command-line based, allowing users to add flavors, manage ingredients, and review customer suggestions.



## Project Structure
# Chocolate House Management Application

## Overview
This Python application manages seasonal flavor offerings, ingredient inventory, and customer flavor suggestions and allergy concerns for a fictional chocolate house. The application uses SQLite for data management and can be run in a Docker container. The interface is command-line based, allowing users to add flavors, manage ingredients, and review customer suggestions.



## Project Structure
chocolate_house/ ├── app.py # Main application file ├── database.py # Database connection and setup ├── models.py # Models for database operations ├── requirements.txt # Dependencies ├── Dockerfile # Dockerfile for containerization ├── README.md # Project documentation └── tests/ # Folder for unit tests └── test_app.py # Test cases for application features

Install Dependencies:
pip install -r requirements.txt

Initialize the Database:
python database.py

Build the Docker Image
docker build -t chocolate_house_app .

Run The Docker Container
docker run -it --rm chocolate_house_app

Running the application
python app.py

