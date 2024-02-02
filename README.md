
# Wikipedia Scraper for Country Leaders

A Python class for scraping leader data from the Country Leaders API and retrieving information from Wikipedia pages.


## Introduction

The `WikipediaScraper` class is designed to retrieve leader data from the Country Leaders API and gather additional details from the Wikipedia pages of each leader. It provides methods to refresh the API cookie, get a list of supported countries, fetch leaders for a specific country, clean paragraphs, retrieve the first paragraph from Wikipedia, and store the data structure into a JSON file.


## Features

- **Country Leaders API Integration:** Fetches detailed information about leaders for supported countries.

- **Wikipedia Page Scraping:** Extracts the first paragraph of leader details from their Wikipedia page.

- **Data Cleaning:** Implements a method to clean specific patterns from the scraped text.

- **Data Storage:** Stores the scraped leader data in a JSON file.


## Usage

1. **Initialize WikipediaScraper:**

   ```python
   scraper = WikipediaScraper()

   

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:sahar-mahmoudi/wikipedia-scraper.git
   cd your-repository

2. Install the required dependencies:

    pip install -r requirements.txt
