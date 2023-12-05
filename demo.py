import requests
from bs4 import BeautifulSoup

def get_technology_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the tag that often contains technology information
        technology_tag = soup.find('meta', attrs={'name': 'generator'})

        if technology_tag:
            technology_used = technology_tag.get('content')
            return f"Technology Used: {technology_used}"
        else:
            return "Technology information not found."

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    website_url = "https://microlise.com"  # Replace with the desired website URL
    technology_info = get_technology_info(website_url)
    print(technology_info)
