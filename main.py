import requests
from bs4 import BeautifulSoup


# Function to fetch the Google Doc content
def fetch_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


# Function to parse the HTML document
def parse_document(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')[1:]  # Skip the first row (header)

    grid_data = {}

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:
            try:
                # Extract the x-coordinate, character, and y-coordinate
                x = int(cells[0].text.strip())
                character = cells[1].text.strip()
                y = int(cells[2].text.strip())

                # Store the character at the (x, y) coordinates
                grid_data[(x, y)] = character
            except ValueError as e:
                print(f"Skipping row due to error: {e}")
                continue  # Skip this row if there's an error parsing the coordinates or character

    return grid_data



# Function to render the grid
def render_grid(grid_data):
    # Determine the bounds of the grid
    if not grid_data:
        print("No valid grid data found.")
        return

    max_x = max(x for x, _ in grid_data.keys())
    max_y = max(y for _, y in grid_data.keys())

    # Create and print the grid, reversed row order
    for y in range(max_y, -1, -1):  # Loop from max_y to 0 (reverse order)
        row = ''.join(grid_data.get((x, y), ' ') for x in range(max_x + 1))
        print(row)



# Main function to fetch, parse, and render the grid
def print_grid_from_google_doc(url):
    html = fetch_google_doc(url)
    grid_data = parse_document(html)
    render_grid(grid_data)


# Example URL (replace with the actual URL you provided)
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
print_grid_from_google_doc(url)
