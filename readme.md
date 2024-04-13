# Bulbapedia Pokemon Name Webscraper 

This Python script is designed to scrape Pokémon numbers and names from Bulbapedia.

## Why This Project?
After discovering that the [pokemon npm](https://www.npmjs.com/package/pokemon) package was missing some of the Generation 9 Pokémon, and finding myself with a spare afternoon, I decided to create a simple scraper to pull this data directly from Bulbapedia. This was partly for fun, and partly to fulfill a personal need for the most up-to-date Pokémon data. 😄

## Requirements
Before you can run this script, you will need to have Python installed on your system along with a couple of Python libraries:

- BeautifulSoup4
- requests

You can install these libraries using pip:
```
pip3 install -r requirements.txt
```

## Usage
- Download or clone this repository.
- Navigate to the directory containing the script.
- Run the script using Python:
```
python3 pokemon_scraper.py
```

## Output
The output JSON file will have the following format:
```json
{
    // Scraping Hangul names
    "1": "이상해씨",
    "2": "이상해풀",
    // continues...
}
```
Where the keys are the Pokémon numbers (as integers), and the values are the corresponding Hangul names.

## Contributing
Feel free to fork this project and submit pull requests. You can also open an issue if you find any bugs or if you have any suggestions for future improvements.

## License
This project is open source and available under the MIT License.

