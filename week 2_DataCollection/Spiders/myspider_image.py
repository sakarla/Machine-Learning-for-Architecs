#The spider is designed to extract image URLs from a specific web page.

import scrapy

class ArchDailyImagesSpider(scrapy.Spider):
    # Define the name of the spider
    name = 'my_spider_img'
    
    # Specify the starting URL(s) for the spider
    start_urls = ['https://www.archdaily.com/882553/luminous-transparent-mixed-use-tower-will-mark-the-skyline-of-saint-malo?ad_medium=widget&ad_name=category-apartments-article-show']

    #The parse method is a mandatory function in Scrapy spiders. It's called with the web page's response as an argument.
    def parse(self, response):
        # Extract image URLs from the page using XPath
        
        # XPath is used to select all <img> elements on the page, and their 'src' attributes (image URLs) are extracted. 
        image_urls = response.xpath('//img/@src').extract()

        # Iterate over the extracted image URLs
        for img_url in image_urls:
            # Yield each image URL as a dictionary
            yield {
                'image_url': img_url,
            }
