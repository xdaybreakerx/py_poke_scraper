import requests
from bs4 import BeautifulSoup
import json

# This is used to scrape the Pokemon names from Bulbapedia
# This was created because https://www.npmjs.com/package/pokemon was missing some of the Gen 9 Pokemon and I had a spare afternoon ¯\_(ツ)_/¯


def scrape_pokemon_names(url, column):
    # Send a HTTP request to the specified URL and get the page content
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Initialize a dictionary to store Pokémon numbers and names
    pokemon_data = {}

    # Find all 'tr' tags since each Pokémon's info is in a row
    for tr in soup.find_all("tr"):
        # Extract the td elements; they contain the data we need
        tds = tr.find_all("td")
        if len(tds) >= 4:  # Make sure there are enough columns
            num_td = tds[0]
            name_td = tds[column]  # change this based on the column you require

            # Extract the Pokémon number from the first column
            # Text looks like "#0001" so we strip the '#' and convert to int
            try:
                number = int(num_td.text.strip("#"))
                name = name_td.text.strip()

                # Store the extracted data in the dictionary
                pokemon_data[number] = name
            except ValueError:
                continue  # Skip rows that don't contain a valid number

    return pokemon_data


def write_to_json(data, filename):
    # Convert dictionary into JSON and write to a file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Example usage
korean_url = "https://m.bulbapedia.bulbagarden.net/wiki/List_of_Korean_Pok%C3%A9mon_names"  # Replace with the actual URL
pokemon_names = scrape_pokemon_names(korean_url, 3)
write_to_json(pokemon_names, "hangul_pokemon_names.json")

# print(pokemon_names) - if you just want the names in Terminal

#### Other Bulbapedia URLs:

# english_url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number" - column 2
# japanese_url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names"
# german_url = "https://m.bulbapedia.bulbagarden.net/wiki/List_of_German_Pok%C3%A9mon_names"
# french_url = "https://m.bulbapedia.bulbagarden.net/wiki/List_of_French_Pok%C3%A9mon_names"
# thai_url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Thai_Pok%C3%A9mon_names"
# chinese_url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Chinese_Pok%C3%A9mon_names" - column 3 for han-t, 4 for han-s
# russian_url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Russian_Pok%C3%A9mon_names"
# korean_url = "https://m.bulbapedia.bulbagarden.net/wiki/List_of_Korean_Pok%C3%A9mon_names"
