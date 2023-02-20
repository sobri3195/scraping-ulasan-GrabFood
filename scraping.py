import requests
from bs4 import BeautifulSoup

merchant_url = "https://www.grab.com/id/merchant/merchant-name/"

# Send HTTP request to merchant URL
response = requests.get(merchant_url)

# Parse HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find review elements and extract information
reviews = []
for review_element in soup.select(".review__list__item"):
    review = {
        "name": review_element.select_one(".review__list__item__user__name").get_text(),
        "rating": review_element.select_one(".review__list__item__star__text").get_text(),
        "comment": review_element.select_one(".review__list__item__comment__text").get_text(),
        "timestamp": review_element.select_one(".review__list__item__timestamp").get_text()
    }
    reviews.append(review)

# Print reviews
for review in reviews:
    print(review)
