# Web Scraping Forbes Billionaires

This project involves web scraping the Forbes website to extract information about the world’s largest public companies. The data is fetched using the Forbes API and processed to extract relevant information.

## Project Structure


## Features

- Scrapes data from the Forbes website.
- Extracts details like organization name, country, revenue, profits, assets, and market value.
- Saves the extracted data to a CSV file.

## Setup

1. Clone the repository:
    cd web-scraping-forbes

2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install the required packages:
    pip install -r requirements.txt

## Usage

1. Run the main script to start scraping:
    python largest_public_companies.py

2. The output CSV file will be saved in the `data/` directory.
