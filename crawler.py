from bs4 import BeautifulSoup
import requests
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


# Crawler: Gets the the product title from a given URL
def get_product_title(url: str):

    # Loading the HTML tree
    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Extracting the product title and post-processing it
    title = soup.find("span", attrs={"id": 'productTitle'})

    return title.string.strip()


# Crawler: Extracts product titles from a list of URLs, returns list of commma separated title as a string
def url_to_product_name(url_str: str):
    return ', '.join([get_product_title(url) for url in url_str.replace(" ", "").split('|')])


# print(url_to_product_name('http://www.amazon.co.uk/Hornby-R8150-Catalogue-2015/dp/B00S9SUUBE | http://www.amazon.co.uk/Hornby-Book-Model-Railways-Edition/dp/1844860957 | http://www.amazon.co.uk/Peco-60-Plans-Book/dp/B002QVL16I | http://www.amazon.co.uk/Newcomers-Guide-Model-Railways-Step/dp/1857943295'))
