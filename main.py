import requests
from bs4 import BeautifulSoup
import lxml

link = "https://www.amazon.com/Apple-iPhone-11-256GB-Black/dp/B07ZPL6Y2D/ref=sr_1_3?crid=2O0FMYV6NSATI&keywords=iphone%2B13&qid=1668695412&sprefix=iphone%2B13%2Caps%2C249&sr=8-3&th=1"
user_agent = "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
accept_language = "ru"

headers = {
    "User_Agent": user_agent,
    "Accept-Language": accept_language,
}

response = requests.get(url=link, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(id="priceblock_ourprice").get_text()
print(price)

