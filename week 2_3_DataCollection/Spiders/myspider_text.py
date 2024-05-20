#This code defines a web scraping spider using the Scrapy lib  to 
#extract data from a specific webpage. 
#Let's break down the key components and functionalities:

import scrapy

class MySpider(scrapy.Spider):
    # The spider is given a name, 'my_spider', which is used to identify it when running.
    name = 'my_spider_text'
    
    # This list contains the URL(s) from which the spider will start its web scraping process. In this example, it starts from the ArchDaily page mentioned in the URL.
    start_urls = ['https://www.archdaily.com/882553/luminous-transparent-mixed-use-tower-will-mark-the-skyline-of-saint-malo?ad_medium=widget&ad_name=category-apartments-article-show']

    #The parse method is a mandatory function in Scrapy spiders. It's called with the web page's response as an argument.
#   Inside the parse method, data is extracted from the HTML content of the web page using CSS selectors.
    def parse(self, response):
     
        
        # Example: Extract the title of the page
        #'title::text'. This selector targets the text content of the <title> tag.
        title = response.css('title::text').get()
        
        # Example: Extract all text content within <p> tags
        content = response.css('p::text').getall()
        
        # The extracted data, including the title and content, is stored in the data dictionary.
        data = {
            'title': title,
            'content': content,
        }

        # Yield (return) the extracted data as a Python dictionary
        yield data


'''
In summary, this Scrapy spider is set up to visit a specific web page,
 extract the title and text content from <p> tags, and yield this data as a
  Python dictionary. You can customize the CSS selectors and data extraction 
  logic to suit your specific web scraping needs. When you run this spider using Scrapy,
   it will crawl the specified URL(s) and collect the data defined in the parse method.'''