"""In this file, I created number of classes."""

__author__ = "Yoav Weller"
__copyright__ = "Copyright 2022, Purple Dove"
__credits__ = ["Yoav Weller"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yoav Weller"
__email__ = "yoav.weller@gmail.com"
__status__ = "Production"

# Importss
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

basic_headers = {
            'SOURCE': ['NA'], # The name of the site (e.g. 'Forbs')
            'Link': ['NA'], # The link for the article
            'Title': ['NA'], # Main heading of the article
            'Subtitle': ['NA'], # Subheading of the article
            'Body': ['NA'] # The rest of the articls conent
            }
        
news_raw_data = pd.DataFrame(basic_headers) # Creating the table.

r = requests.get("https://www.forbes.com/money/?sh=65fbdbb1c19a")

r_text = (r.text)
soup = BS(r_text, 'html.parser')

'''
class data_from_news(object):
    """
    This is the main class. It defines the basic features that needs to be establish
    for each news source.
    """
    def __init__(self, url):
        """ Importing """
        import requests
        from bs4 import BeautifulSoup
        import pandas as pd

        self.url = url
        
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

        """
        Creating an empty dataframe for the raw data:
        """
        # This is a dictionary with the name of the headers of the dataframe + one empty observation.
        basic_headers = {
            'SOURCE': ['NA'], # The name of the site (e.g. 'Forbs')
            'Link': ['NA'], # The link for the article
            'Title': ['NA'], # Main heading of the article
            'Subtitle': ['NA'], # Subheading of the article
            'Body': ['NA'] # The rest of the articls conent
            }
        
        news_raw_data = pd.DataFrame(basic_headers) # Creating the table.
        
        return news_raw_data
    
class data_from_forbs(data_from_news):
    """
    This is a class that gathers information from Forbs. It inherits the basic features from the 'data_from_news'
    class.
    """
    def __init__(self, url):
        
        super().__init__(url)
    
    def search_data(self):
        links = []
        for link in self.soup.find_all('href'):
            links.append(link.text)

        print(links)
'''
forbs_link = str("https://www.forbes.com/money/?sh=65fbdbb1c19a")
yahoo_link = 'https://finance.yahoo.com/'

# data_from_forbs(forbs_link)