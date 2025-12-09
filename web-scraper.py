import requests
# Imports the requests library to perform HTTP GET requests.

from bs4 import BeautifulSoup
# Imports BeautifulSoup from the bs4 package to parse and navigate HTML content.


def scrape_quotes() -> None:
    # Defines the main scraping function that fetches and prints quotes.

    url = "https://quotes.toscrape.com/"
    # Target URL that hosts sample quotes for web scraping practice.

    print(f"Fetching quotes from: {url}")
    # Logs the URL being requested for visibility in the console.


    try:
        response = requests.get(url, timeout=5)
        # Sends an HTTP GET request to the URL with a timeout to avoid hanging indefinitely.

        response.raise_for_status()
        # Raises an HTTPError if the response status indicates a client or server error.
    except requests.RequestException as exc:
        # Catches any network related or HTTP related exceptions from the request.

        print("Error fetching the page:")
        # Reports that an error occurred during the request phase.

        print(exc)
        # Outputs the detailed exception message for troubleshooting.

        return
        # Exits the function early since no valid response was obtained.


    soup = BeautifulSoup(response.text, "html.parser")
    # Parses the HTML response text into a BeautifulSoup object using the standard HTML parser.


    quote_blocks = soup.find_all("div", class_="quote")
    # Locates all div elements with class "quote", each representing an individual quote block.


    if not quote_blocks:
        # Checks whether any quote blocks were found on the page.

        print("No quotes were found on the page.")
        # Informs the user that there was no data to process.

        return
        # Exits the function since there is nothing to display.


    print()
    # Prints a blank line for readability.

    print("Quotes on the first page:")
    # Introduces the list of quotes that will follow.

    print("--------------------------")
    # Prints a simple separator line for formatting.


    for index, block in enumerate(quote_blocks, start=1):
        # Iterates over each quote block while tracking a 1 based index for numbering output.

        text_tag = block.find("span", class_="text")
        # Retrieves the span element containing the quote text.

        author_tag = block.find("small", class_="author")
        # Retrieves the small element containing the author name.


        text = text_tag.get_text(strip=True) if text_tag else "No text"
        # Extracts and trims the quote text, providing a fallback label if not present.

        author = author_tag.get_text(strip=True) if author_tag else "Unknown"
        # Extracts and trims the author name, with a fallback value when missing.


        print(f"{index}. {text}  - {author}")
        # Prints the quote and author in a numbered format.


    print()
    # Prints a trailing blank line after listing all quotes.

    print(f"Total quotes scraped: {len(quote_blocks)}")
    # Reports the total number of quotes processed from the page.


if __name__ == "__main__":
    # Ensures this block only runs when the script is executed directly, not when imported.

    print("Simple Web Scraper: Quotes")
    # Prints a title for the script in the console.

    print("==========================")
    # Prints a visual header separator.

    scrape_quotes()
    # Invokes the main scraping function to perform the workflow.
