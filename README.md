FaselHD Series Scarper
This is a Python script for downloading TV series from FaselHD website. It automates the process of navigating through the website, selecting seasons and episodes, and downloading the video files.

Requirements
To use this script, you need to have the following libraries installed:

BeautifulSoup: for HTML parsing
requests: for making HTTP requests
urllib.parse: for URL parsing
selenium: for browser automation
Chrome WebDriver: for running the Chrome browser in headless mode

Installation
Clone the repository:

bash
Copy
git clone https://github.com/MBajily/FaselHD-Series-Scraper.git
Navigate to the project directory:

bash
Copy
cd FaselHD-Series-Scraper
Install the required packages:

bash
Copy
pip install -r requirements.txt
Usage
Ensure that you have Python 3.x and the required packages installed.

Run the script:

bash
Copy
python faselhd.py
The script will start downloading the videos from the FaselHD website and save them in the "faselhd" directory.

The progress of each download will be displayed in the console.

Once the script finishes, you can find the downloaded videos in their respective series and season directories inside the "faselhd" directory.

Notes
The script is currently set to download videos from the first page of the series. You can modify the script to download videos from multiple pages by updating the range in the for loop.
The script is designed to work with the specific structure of the FaselHD website. If the website structure changes, the script may need modifications to adapt to the changes.

Disclaimer
Please note that downloading copyrighted content may be illegal in your country. This script is provided for educational purposes only. Use it responsibly and respect the rights of content creators.

Author
This script was developed by Mohammed Elgaily.