# FaselHD Series Scarper
This is a Python script for downloading TV series from FaselHD website. It automates the process of navigating through the website, selecting seasons and episodes, and downloading the video files.

## Requirements
To use this script, you need to have the following libraries installed:
<br>
<ul>
  <li><b>BeautifulSoup</b>: for HTML parsing</li>
  <li><b>requests</b>: for making HTTP requests</li>
  <li><b>urllib.parse</b>: for URL parsing</li>
  <li><b>selenium</b>: for browser automation</li>
  <li><b>Chrome WebDriver</b>: for running the Chrome browser in headless mode</li>
</ul>


## Installation

Clone the repository:

`git clone https://github.com/MBajily/FaselHD-Series-Scraper.git`
<br>

Navigate to the project directory:

`cd FaselHD-Series-Scraper`
<br>

Install the required packages:

`pip install -r requirements.txt`


## Usage
<ol>
  <li>Ensure that you have Python 3.x and the required packages installed.</li>
  
  <li>Run the script:</li>
  
  `python faselhd.py`
  <li>The script will start downloading the videos from the FaselHD website and save them in the "faselhd" directory.</li>
  
  <li>The progress of each download will be displayed in the console.</li>
  
  <li>Once the script finishes, you can find the downloaded videos in their respective series and season directories inside the "faselhd" directory.</li>
</ol>

## Notes
<ul>
  <li>The script is currently set to download videos from the first page of the series. You can modify the script to download videos from multiple pages by updating the range in the for loop.</li>
  <li>The script is designed to work with the specific structure of the FaselHD website. If the website structure changes, the script may need modifications to adapt to the changes.</li>
</ul>

## Disclaimer
Please note that downloading copyrighted content may be illegal in your country. This script is provided for educational purposes only. Use it responsibly and respect the rights of content creators.

## Author
This script was developed by Mohammed Elgaily.
