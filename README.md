# web-scraping-challenge

This project is broken in to 2 parts:
- Scraping
- MongoDB and Flask Application



# Part 1: Scraping
- The initial scraping will be using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
- Site used for scraping: NASA Mars News
- Used Splinter to navigate the site and found the image URL for the current Featured Mars Image, then assigned the URL string to a variable called featured_image_url.

- Mars Facts:
- Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including diameter, mass, etc.
- Used Pandas to convert the data to a HTML table string.

- Mars Hemispheres:
- Visited the astrogeology site to obtain high-resolution images for each hemisphere of Mars.

# Part 2: MongoDB and Flask Application
- Used MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.
- I Started by converting the Jupyter notebook into a Python script called scrape_mars.py by using a function called scrape. This function executes all the scraping code from above and returns one Python dictionary containing all the scraped data.
- Next, I created a route called /scrape that will import the scrape_mars.py script and call the scrape function.
Store the return value in Mongo as a Python dictionary.




