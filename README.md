# get-avalon-minimum-rent
Using Python web scraper to get the minimum rent price on Avalon apartment website.

# Before running it
Some prerequisites for running this script
* Python 3
* Python packages
    * bs4
    * requests

# Running the script
`python3 webscraper.py`
You may need to modify the url and current_least_price parameters to match the Avalon apartment website information that you like. 

# Known issues
The script will check the least rent price from the website every 5 seconds (based on the time sleep delay), and at some point the requests will time out and the script will terminate by itself. Will need to fix this so it can run in the background as a daemon.

# TODO
Fix requests time out issue. Run as a daemon. Log least current price into a CSV file for future reference. Send an email whenever the least price changes.

