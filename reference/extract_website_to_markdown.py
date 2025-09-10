import requests
from bs4 import BeautifulSoup
import html2text

def website_to_markdown(url, output_file):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize html2text converter
        h = html2text.HTML2Text()
        h.ignore_links = False  # Keep links in Markdown
        h.ignore_images = False  # Keep images in Markdown
        h.body_width = 0  # Disable line wrapping

        # Convert HTML to Markdown
        markdown = h.handle(str(soup))

        # Save to a Markdown file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"Markdown content saved to {output_file}")

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = "https://docs.cognite.com/cdf/deploy/cdf_toolkit/references/resource_library/"  # Replace with your target URL
    output_file = "yaml_reference_library.md"     # Output file name
    website_to_markdown(url, output_file)