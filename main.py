# import requests
# import json
# from bs4 import BeautifulSoup
# import re
# import time





# start_time = time.time()
# s = requests.Session() 

# def refresh_cookie(root_url):
#     response = requests.get(root_url + "cookie/")
#     return response.cookies



# def clean_par(first_paragraph): # Define a regular expression pattern to match references and HTML tags
#     pattern =r'\([^)]*uitspraakⓘ[^)]*\)|\[\d+\]|\n' + f'|{r"//w+?;"}'


# #     # Use re.sub() to replace matched patterns with an empty string
#     cleaned_text = re.sub(pattern, '', first_paragraph)
#     return cleaned_text

# #
# # @clean_par
# def first_par(url):
#     root_url = "https://country-leaders.onrender.com/cookie/"
#     refresh_cookie(root_url)
    
#     # Make a request to the Wikipedia page
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')

#     # Find the specific div with the given id
#     target_div = soup.find('div', id="mw-content-text")

#     # Find all paragraphs within the target div
#     paragraphs = target_div.find_all("p")

#     for paragraph in paragraphs:
#         # Check if the paragraph starts with a bold word
#         if paragraph.find("b") and len(paragraph.get_text())>15:
#             # Return the cleaned text or the original text
#             cleaned_text = clean_par(paragraph.get_text())
#             return cleaned_text






# def to_json_file(leaders_data,filepath):
#         with open(filepath, 'w') as file:
#             json.dump(leaders_data, file)
            
            
# # Set the initial time




# #check statues
# def get_country(url):
#     root_url = url
#     endpoint=["status/","cookie/","countries/"]

#     for i in endpoint:
#         response = s.get(f"{root_url}/{i}")
#         #print(response.json())
#         countries=response.json()
#     return countries



# root_url = "https://country-leaders.onrender.com"
# countries=get_country(root_url)


# dict = {}


# for country in countries:
    
    
#     print(country)
#     get_country(root_url)
    
#     endpoint4 = "leaders?country="+country
#     response = s.get(f"{root_url}/{endpoint4}")
#     all_leaders=response.json()
    
    
#     dict[country] = [{'first_name': leader["first_name"],"url":leader["wikipedia_url"],"first_paragraph":first_par(leader["wikipedia_url"])} for leader in all_leaders]

#     print("post leader request")


# to_json_file(dict,"leaders_data.json")

# #print(dict["ma"][0]["url"])



# Example usage:
from src.scraper import WikipediaScraper

def main():
    # Create an instance of the WikipediaScraper
    scraper = WikipediaScraper()

    # Get the list of supported countries
    countries = scraper.get_countries()

    # Get leaders for each country and populate the leaders_data dictionary
    for country in countries:
        scraper.get_leaders(country)

    # Save the data to a JSON file
    scraper.to_json_file("leaders_data.json")

if __name__ == "__main__":
    main()