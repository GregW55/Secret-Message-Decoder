# Secret Message Decoder 
Secret Message Decoder is a Python-based tool designed to fetch, parse, and display a graphical grid encoded within a Google Doc. This tool is especially useful for retrieving hidden messages or encoded data formatted as a grid, represented through coordinates and characters.

## Features
- Fetches the content of a Google Doc via a public URL.
- Parses a table structure in the Google Doc that includes x, y coordinates and corresponding characters.
- Renders the grid in a visually readable format to reveal the hidden message or graphic.
- Handles errors in parsing, ensuring smooth operation even with imperfect data.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository: git clone https://github.com/GregW55/Secret-Message-Decoder.git
2. Navigate to the directory: cd Secret-Message-Decoder
3. Install the required libraries: pip install requests beautifulsoup4

## Usage
- Replace the url variable in the script with the URL of a Google Doc containing a grid structure (with x, y coordinates and characters in a table).
- Run the script: python main.py
- This will fetch the Google Doc, parse the coordinates, and render the grid in the terminal. The characters at the coordinates will be displayed in a grid-like format, revealing the hidden message.

## Example
- In the example provided, the script fetches a public Google Doc, processes the grid data, and renders it in the console. To use the tool with your own document, just update the url variable with the link to your Google Doc.

## How It Works
1. Fetching the Google Doc: The script uses the requests library to retrieve the HTML content of the document via a provided URL.
2. Parsing the Document: The BeautifulSoup library parses the document's HTML, extracting table rows that contain x and y coordinates along with the corresponding character.
3. Rendering the Grid: The script loops through the coordinates, placing characters in their appropriate locations to form a grid. The grid is then displayed, with row rendering occurring in reverse order to match the visual representation of the data.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
- If you find any issues or wish to enhance the tool, feel free to fork the repository and submit pull requests. Contributions are always welcome!

## Acknowledgements
- requests - Used for fetching content from the Google Doc.
- BeautifulSoup - Utilized for parsing HTML content and extracting table data.
