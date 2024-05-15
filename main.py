import firebase_admin
import markets_data
import requests
import asyncio
import re
from bs4 import BeautifulSoup
from firebase_admin import credentials, firestore

from white_lists import whitelistLegume, allWhitelists

cred = credentials.Certificate("doyourgroceriesapp-49647ca24603.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()


# doc_ref = db.collection("pula").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

def parse_string(input_string, blacklist):
    words = re.findall(r'\b[\w.]+\b', input_string)

    filtered_words = [word.lower() for word in words if
                      len(word) > 2 and word not in blacklist and not any(char.isdigit() for char in word) and not any(
                          char == '.' for char in word)]

    tags = filtered_words

    return tags


def percentage_strings_in_whitelist(tags, whitelist):
    if not whitelist:
        return 0
    count = 0
    for tag in tags:
        if any(item in whitelist for item in tag.split()):
            count += 1
    return (count / len(tags)) * 100 if tags else 0


async def generate_products():
    pg_ct = 0

    for index_supermarkets in range(5):
        current_supermarket_name = markets_data.markets_names[index_supermarkets]
        print(current_supermarket_name)
        current_supermarket_data = markets_data.all_supermarkets.get(current_supermarket_name)

        for index, category in enumerate(markets_data.supermarket_categories):
            # print(category)
            url = current_supermarket_data.get(category)
            print(url)
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.select('div.product-non-food-card')

            pg_ct = 0
            for i, link in enumerate(links):
                if i % 40 == 0:
                    pg_ct += 1

                ref = db.collection(current_supermarket_name).document('categories') \
                    .collection(category).document('pages').collection(f'page_{pg_ct}').document()

                food_info = link.select_one('div.content-container')
                image = link.select_one('div.image-container > img')['src']

                price = food_info.select_one('div.price-container > span.price')

                pattern = r'\d*\.?\d+'
                match = re.search(pattern, price.text)
                if match:
                    price_item = match.group()
                    price_item = float(price_item)
                else:
                    price_item = 0.0

                title = food_info.select_one('div.title').text

                filtered_product_name = parse_string(title, markets_data.blacklist)

                max_percentage = 0
                best_match = None

                for item in allWhitelists[category]:
                    percentage = percentage_strings_in_whitelist(filtered_product_name, item)
                    if percentage > max_percentage:
                        max_percentage = percentage
                        best_match = item

                # print(f"The string '{best_match}' has the highest percentage of tags: {max_percentage}%")

                product = {
                    'productId': ref.id,
                    'name': title,
                    'price': price_item,
                    'image': image,
                    'page': pg_ct,
                    'tag': filtered_product_name,
                    'supermarket': current_supermarket_name,
                    'category': category
                }
                # print(product)

                db.document(f'tags/{category}/{best_match}/{ref.id}').set(product)
                ref.set(product)


async def main():
    await generate_products()


asyncio.run(main())
