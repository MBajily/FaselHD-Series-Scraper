from bs4 import BeautifulSoup  # Importing BeautifulSoup for HTML parsing
import os  # Importing os for file and directory operations
import re  # Importing re for regular expressions
import requests  # Importing requests for making HTTP requests
import urllib.parse  # Importing urllib.parse for URL parsing
from selenium import webdriver  # Importing Selenium for browser automation

site = "https://web1.faselhd-watch.shop/series/page/"  # Base URL for series pages

series_pages = []  # Empty list to store series page URLs

# Iterate over a range of pages (in this case, only page 1)
for page in range(1, 2):
    r = requests.get(site + str(page))  # Send GET request to the current page
    soup = BeautifulSoup(r.content, 'html.parser')  # Parse the HTML content
    series = soup.findAll('div', attrs={'class': 'postDiv'})  # Find all div elements with class 'postDiv'

    # Extract URLs of series pages
    for serie in series:
        urls = serie.find_all('a')  # Find all anchor tags within the current div
        for url in urls:
            if 'seasons' in url.get('href'):  # Check if the URL contains 'seasons'
                series_pages.append(url.get('href'))  # Append the URL to series_pages list

series = {}  # Empty dictionary to store information about series
os.makedirs("faselhd", exist_ok=True)  # Create a 'faselhd' directory to store downloaded videos

# Process each series page
for serie in series_pages:
    r = requests.get(serie)  # Send GET request to the series page
    soup = BeautifulSoup(r.content, 'html.parser')  # Parse the HTML content
    serie_name = serie.split("/seasons/")[-1].replace("-", ' ').replace("%d9%85%d8%b3%d9%84%d8%b3%d9%84 ", '').title()  # Extract and format the series name from the URL
    serie_name = urllib.parse.unquote(serie_name)  # Decode URL-encoded characters
    os.makedirs("faselhd/" + serie_name, exist_ok=True)  # Create a directory for the current series
    series[serie_name] = {}  # Add an empty dictionary for the current series
    print(serie_name)

    seasons = soup.findAll('div', attrs={'class': 'seasonDiv'})  # Find all div elements with class 'seasonDiv'
    season_number = 1  # Counter for season number

    try:
        # Process each season
        for season in seasons:
            season_path = os.makedirs("faselhd/" + serie_name + "/" + ("S" + str(season_number).zfill(2)), exist_ok=True)  # Create a directory for the current season
            onclick = season.get('onclick')  # Get the 'onclick' attribute value of the current season element
            url = onclick.split("'")[1]  # Extract the URL from the 'onclick' attribute value
            url = "https://web1.faselhd-watch.shop/series" + url  # Construct the complete URL

            r = requests.get(url)  # Send GET request to the season page
            soup = BeautifulSoup(r.content, 'html.parser')  # Parse the HTML content

            eps = soup.find('div', attrs={'class': 'epAll'})  # Find the div element with class 'epAll'
            eps = eps.find_all('a')  # Find all anchor tags within the div

            ep_number = 1  # Counter for episode number

            # Process each episode
            for ep in eps:
                url = ep.get('href')  # Get the URL of the current episode
                r = requests.get(url)  # Send GET request to the episode page
                soup = BeautifulSoup(r.content, "html.parser")  # Parse the HTML content
                video_url = soup.find('iframe', attrs={})  # Find the iframe element
                filename = "E" + str(ep_number).zfill(2) + '.m3u8'  # Construct the filename for the episode
                print("==== 10% ====")
                response = requests.get(video_url.get('src'))  # Send GET request to the video URL
                soup = BeautifulSoup(response.content, "html.parser")  # Parse the HTML content
                video = soup.findAll('div', attrs={'class': "quality_change"})  # Find div elements with class 'quality_change'
                print("==== 20% ====")
                options = webdriver.ChromeOptions()  # Create options for the Chrome browser
                print("==== 30% ====")
                options.add_argument("--headless")  # Run the browser in headless mode (without GUI)
                options.add_argument("--log-level=3")  # Set log level to suppress WebDriver logs

                print("==== 40% ====")
                driver = webdriver.Chrome(options=options)  # Create a Chrome WebDriver with the specified options
                print("==== 50% ====")

                try:
                    # Download the video
                    driver.get(video_url.get('src'))  # Navigate the browser to the video URL
                    print("==== 60% ====")
                    html_content = driver.page_source  # Get the HTML content of the page
                    print("==== 70% ====")
                    download_url = re.search(r'"file":"([^"]+)"', html_content).group(1)  # Extract the download URL using regular expressions
                    print("==== 80% ====")
                    download = requests.get(download_url)  # Send GET request to the download URL
                    print("==== 90% ====")
                    with open(("faselhd/" + serie_name + "/" + "S" + str(season_number).zfill(2) + "/" + filename), 'wb') as file:  # Open a file to save the video content
                        file.write(download.content)  # Write the video content to the file
                    print("==== 100% ====")
                    print(f"{'E' + str(ep_number).zfill(2)} => Video downloaded successfully.")
                except Exception as e:
                    print(e)

                ep_number += 1  # Increment the episode number

            season_number += 1  # Increment the season number
    except Exception as e:
        print(e)

# print(series)  # Print the dictionary containing information about the series (currently commented out)