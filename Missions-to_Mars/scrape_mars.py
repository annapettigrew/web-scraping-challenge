# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

def scrape():
        
    # Creating a path using ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Setting the URL to visit the Mars Site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    # Examine the results, then determine element that contains sought info
    print(soup.prettify())


    ### NASA Mars News

    # Printing the latest news title and paragraph on the Mars site
    results = soup.find_all('div', id='news')
    for result in results:
        latest_news = soup.find('div', class_='content_title').text 
        p_text = soup.find('div', class_='article_teaser_body').text
        print(latest_news)
        print('--------------------------------------------------------------------')
        print(p_text)


    ### JPL Mars Space Images -- Featured Image

    # Getting the URL for the Mars image
    image_url = "https://spaceimages-mars.com"
    browser.visit(image_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_two = bs(browser.html, 'html.parser')

    # Examine the results, then determine element that contains sought info
    print(soup_two.prettify())

    # Finding the Featured image url 
    mars_image = soup_two.find ('div', class_='floating_text_area')
    image_link = mars_image.find('a', class_='showimg fancybox-thumbs')['href']
    # Creating the link to the image
    featured_image_url = f'{image_url}/{image_link}'
    featured_image_url


    ### Mars Facts


    # Reading the Url using Pandas
    mars_facts_df = pd.read_html('https://galaxyfacts-mars.com')

    # Use Pandas to scrape the table containing facts about Mars
    mars_summary = mars_facts_df[1]

    # Rename columns
    mars_summary.columns = ['Facts','Value']

    # Reset Index to be description
    mars_summary.set_index('Facts', inplace=True)

    mars_summary

    # Use Pandas to convert the data to a HTML table string
    mars_facts_html = mars_summary.to_html('facts.html')


    # ### Mars Hemispheres

    # Creating blank lists to append in the for loop
    imgs = []
    titles = []

    # Setting the link to visit the Astrogeology Site 
    def hemispheres():
        hemispheres_url = 'https://marshemispheres.com'
        browser.visit(hemispheres_url)
        
    # Creating an empty list for all of the urls to go in
        urls = []

    # Locating the script and parsing
        soup_three = bs(browser.html, 'html.parser')
        hemisphere = soup_three.find_all('div', class_='item')
        
    # Creating a loop to gather title and thumbnail data 
        for hem in hemisphere:
            title = hem.h3.text
            urls.append(title)
            titles.append(title.replace(' Enhanced', ''))
    # Creating a loop to gather the url links for the data 
        for link in urls:
            browser.links.find_by_partial_text(link).click()
            soup_link = bs(browser.html, 'html.parser')
            hemisphere_link = soup_link.find('div', class_='downloads').find_all('li')
            link = hemisphere_link[0].a['href']
            img_link = f'{hemispheres_url}/{link}'
            imgs.append(img_link)
            browser.visit(hemispheres_url)
            
    hemispheres()


    # Creating a list that combines the data gathered above
    hemisphere_summary = [{'title': titles[n],'img_url': imgs[n]} for n in range(len(titles))]
    # hemisphere_summary

    # mars dict to export data
    mars = {
        'hemisphere_data': hemisphere_summary,
        'mars_facts': mars_facts_html,
        'news_title': latest_news,
        'news_p': p_text,
        'featured_img': featured_image_url,
    }

    return mars

