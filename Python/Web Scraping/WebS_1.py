"""In this file, I created number of classes."""

__author__ = "Yoav Weller"
__copyright__ = "Copyright 2022, Yoav Weller"
__credits__ = ["Yoav Weller"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yoav Weller"
__email__ = "yoav.weller@gmail.com"
__status__ = "Production"

# Imports
import validators
from cmath import nan
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup as BS
import pandas as pd

class data_from_news(object):
    """data_from_news description

    Vast amount of data, in many fields of knowledge, is to be found in news websites. In many articles, the main structure is the same.
    Therefor, the role of this class is to scrape the basic features of every article given the website's url.
    
    Attributes:
        source_url: str
            The link to the main source. For example - if you want to get all articles
            from the NY Times, you should enter the following URL: 'https://www.nytimes.com/'
    """
    
    def __init__(self, source_url):
        """__init__ method, creates a base dataframe"""

        self.source_url = source_url # Link of the news website
        
        """Creating an empty dataframe for the raw data:"""
        
        # This is a dictionary with the name of the headers of the dataframe + one empty observation.
        basic_headers = {
            'SOURCE': [None], # The name of the site (e.g. 'Forbs')
            'Link': [None], # The link for the article
            'Title': [None], # Main heading of the article
            'Subtitle': [None], # Subheading of the article
            'Body': [None] # The rest of the articls conent
            }
        
        self.news_raw_data = pd.DataFrame(basic_headers) # Creating basic table. 
    
    def validating_url(self, link_inside_source):
        """Checking if a given URL is valid. If a link is valid, the function would return it. If not, the function will return nan.
        
        Parameter:
        link_inside_source: str
            This parameter is a url. Each webpage has many links embedded in it, some are valid and some are not.
            Therefor, I named this parameter with this name - it takes those embedded links.
        """
        
        valid = validators.url(link_inside_source) # A boolian variable. If 'True' thre URL is valid, returns it. If not, returns nan.

        if valid == True:
            return(link_inside_source)
        else:
            return nan
    
    def get_all_links(self):
        """Importing all links embedded in a webpage.
        
        In many webpages embedded links are to be found. In the process of finding them, the functions exists today find unvalid links as well.
        Beside of finding valid links, this function inserts the links into a dataframe.
        """
        
        r = requests.get(self.source_url) # Importing the source as a document
        soup = BS(r.text, 'html.parser') # Representing the document as a nested data structure

        embedded_in_source_urls = [] # Creating an empty container that would store all valid embedded in the source.

        for link in soup.find_all('a', href = True):
            """Takes all links embedded in a webpage, and if they are valid - inserts them to the embedded_in_source_urls container."""
            
            unchecked_link = link['href'] # Taking each link embedded in the source URL.
            validated_link = self.validating_url(unchecked_link) # Checking if valid 
        
            if validated_link is not nan: # If an embedded link is valid, add it to the list
                embedded_in_source_urls.append(validated_link)
            else:
                continue
        
        self.number_of_embedded_urls = len(embedded_in_source_urls)
        self.range_1_num_urls = range(0, self.number_of_embedded_urls, 1) # Creating a vector conatines all the numbers between 0 and the number of valid links
        
        for url_ in self.range_1_num_urls: # Inserting the links into the dataframe
            self.news_raw_data.loc[self.news_raw_data.shape[0]] = [None, None, None, None, None]
            self.news_raw_data.at[url_, 'Link'] = embedded_in_source_urls[url_] 
        
        return self.news_raw_data
    
    def get_source_name(self):
        """The source name is the name of the website (Forbs, Yahoo, etc.).
        
        This method ejectes the source name surce URL given by ther user.
        """

        source_name = self.source_url.split('.')[1] # Stores the name of the source website
        
        for i in self.range_1_num_urls:
            
            self.news_raw_data.at[i, 'SOURCE'] = source_name # Inserts the source name into the dataframe.

        return self.news_raw_data

class data_from_forbs(data_from_news):
    """data_from_forbs description
    
    Based on the 'data_from_news' class, this class is to provide further data scraping for data from Forbes.

    Attributes:
        source_url: str
            The link to the main source. For example - if you want to get all articles
            from the NY Times, you should enter the following URL: 'https://www.nytimes.com/'
    """

    def __init__(self, source_url):
        super().__init__(source_url)

    def get_article_title_and_body(self):
        """Getting the article title and body."""

        self.get_all_links() # Getting all links
        self.get_source_name() # Getting source name
        
        for n in self.range_1_num_urls:

            embedded_link = self.news_raw_data.iat[n, 1]
            
            page = requests.get(embedded_link) # Importing the source as a document
            soup_1 = BS(page.text, 'html.parser') # Representing the document as a nested data structure

           
            clean_title = [x.get_text() for x in soup_1.find_all('h1', attrs={'class': ['fs-headline speakable-headline font-base font-size color-base', 'fs-headline speakable-headline font-base font-size should-redesign']}, limit=1)]
            clean_body = [x.get_text() for x in soup_1.find_all('p')]
            self.news_raw_data.iat[n, 2] = clean_title
            self.news_raw_data.iat[n, 4] = clean_body

        return self.news_raw_data

forbs_link = str("https://www.forbes.com/money/?sh=65fbdbb1c19a")
yahoo_link = 'https://finance.yahoo.com/'

forbs = data_from_forbs(forbs_link)
forbs.get_article_title_and_body().to_csv('forbs_raw_data.csv')


