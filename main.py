from src.scraper import WikipediaScraper


def main():
    # Create an instance of the WikipediaScraper
    scraper = WikipediaScraper()

    # Get the list of supported countries
    scraper.get_countries()

    # Get leaders for each country and populate the leaders_data dictionary
    scraper.get_leaders()

    # Save the data to a JSON file
    scraper.to_json_file("leaders_data.json")
    
    
if __name__ == "__main__":
    main()