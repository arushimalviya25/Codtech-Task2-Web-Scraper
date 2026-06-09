import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    # Target URL: A reliable, stable site for scraping practice
    url = "https://news.ycombinator.com/"
    
    print(f"Connecting to {url}...")
    
    # Send an HTTP GET request to the website
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    
    # Check if the connection was successful (Status Code 200)
    if response.status_code == 200:
        print("Successfully connected! Parsing data...\n")
        
        # Parse the raw HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the story titles on Hacker News (they use the CSS class 'titleline')
        articles = soup.find_all('span', class_='titleline')
        
        print(f"=== Found {len(articles)} Latest Headlines ===")
        
        # Loop through each article found and print its text
        for index, article in enumerate(articles, 1):
            # Extract the actual link text inside the span
            link = article.find('a')
            if link:
                headline_text = link.text
                print(f"{index}. {headline_text}")
                
        print("\n=== Scraping Complete! ===")
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")

if __name__ == "__main__":
    scrape_headlines()
