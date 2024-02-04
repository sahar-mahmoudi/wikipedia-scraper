from src.scraper import WikipediaScraper


def main():
    # Create an instance of the WikipediaScraper
    scraper = WikipediaScraper()

    # Get the list of supported countries
    scraper.get_countries()

    # Get leaders for each country and populate the leaders_data dictionary
    scraper.get_leaders()

    # Save the data to a JSON file or CSV file (default = JSON)
    scraper.export(filename='leaders_data', file_format='csv')


if __name__ == "__main__":
    main()
