import requests
import json
from bs4 import BeautifulSoup
import re

class WikipediaScraper:
    def __init__(self):
        """
        Initialize the WikipediaScraper object with necessary attributes
        """
        self.root_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.session = requests.Session()
        self.cookie = None

    def refresh_cookie(self):
        try:
            response = self.session.get(self.root_url + self.cookies_endpoint)
            response.raise_for_status()
            self.cookie = response.cookies
        except requests.exceptions.RequestException as e:
            print(f"Error refreshing cookie: {e}")
            self.cookie = None  # Set to None to handle the error appropriately in your code

    def get_countries(self):
        """
        Retrieve the list of supported countries from the API

        Returns:
        list: List of supported countries
        """
        # Refresh the cookie before scraping each country
        self.refresh_cookie()
        
        
        response = self.session.get(self.root_url + self.country_endpoint)
        return response.json()

    def get_leaders(self, country):
        """
        Retrieve the leaders of a specific country from the API and populate the leaders_data object.

        Args:
        country (str): The name of the country.
        """
           # Refresh the cookie before scraping each country
        self.refresh_cookie()
        
        
        endpoint = f"{self.leaders_endpoint}?country={country}"
        response = self.session.get(self.root_url + endpoint)
        all_leaders = response.json()

        self.leaders_data[country] = [
            {   "first_name": leader["first_name"],
                "last_name": leader["last_name"],
                "id": leader["id"],
                "birth_date": leader["birth_date"],
                "death_date": leader["death_date"],
                "place_of_birth": leader["place_of_birth"],
                "start_mandate": leader["start_mandate"],
                "end_mandate": leader["end_mandate"],
                "url": leader["wikipedia_url"],
                "first_paragraph": self.get_first_paragraph(leader["wikipedia_url"])
            } for leader in all_leaders
        ]

    def clean_paragraph(self, first_paragraph):
        """
        Clean the first paragraph by removing specific patterns.

        Args:
        first_paragraph (str): The original first paragraph.

        Returns:
        str: The cleaned first paragraph.
        """
        pattern = r'\([^)]*uitspraakⓘ[^)]*\)|\[\d+\]|\n' + f'|{r"//w+?;"}'
        cleaned_text = re.sub(pattern, '', first_paragraph)
        return cleaned_text

    def get_first_paragraph(self, wikipedia_url):
            """
            Get the first paragraph of details about a leader from their Wikipedia page

            Args:
            wikipedia_url (str): URL of the leader's Wikipedia page

            Returns:
            str: The cleaned first paragraph.
            """
            response = self.session.get(wikipedia_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the specific div with the given id
            target_div = soup.find('div', id="mw-content-text")

            # Find all paragraphs within the target div
            paragraphs = target_div.find_all("p")

            # Iterate over each paragraph
            for paragraph in paragraphs:
                # Check if the paragraph starts with a bold word and has a length greater than 15
                if paragraph.find("b") and len(paragraph.get_text()) > 15:
                    # Return the cleaned text or the original text
                    cleaned_text = self.clean_paragraph(paragraph.get_text())
                    return cleaned_text

            # Return an empty string if no suitable paragraph is found
            return ""

   

    def to_json_file(self, filepath):
        """
        Store the data structure into a JSON file

        Args:
        filepath (str): The path to the JSON file.
        """
        with open(filepath, 'w',encoding= "utf-8") as file:
            json.dump(self.leaders_data, file, indent=2,ensure_ascii=False)


