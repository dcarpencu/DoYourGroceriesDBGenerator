import firebase_admin
import markets_data
import requests
import asyncio
import re
from bs4 import BeautifulSoup
from firebase_admin import credentials, firestore

cred = credentials.Certificate("doyourgroceries-fea564651a4e.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()


# doc_ref = db.collection("pula").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

def parse_string(input_string, blacklist):
    words = re.findall(r'\b[\w.]+\b', input_string)

    filtered_words = [word for word in words if
                      len(word) > 2 and word not in blacklist and not any(char.isdigit() for char in word) and not any(
                          char == '.' for char in word)]

    tags = filtered_words

    return tags


async def generate_products():
    pg_ct = 0

    for index_supermarkets in range(5):
        current_supermarket_name = markets_data.markets_names[index_supermarkets]
        print(current_supermarket_name)
        current_supermarket_data = markets_data.all_supermarkets.get(current_supermarket_name)

        for index, category in enumerate(markets_data.supermarket_categories):
            url = current_supermarket_data.get(category)
            print(url)
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')

            links = soup.select('div.product-non-food-card')

            for i, link in enumerate(links):
                if i % 40 == 0:
                    pg_ct += 1

                ref = db.collection(current_supermarket_name).document('categories') \
                    .collection(category).document('pages').collection(f'page_{pg_ct}').document()

                food_info = link.select_one('div.content-container')
                image = link.select_one('div.image-container > img')['src']

                price = food_info.select_one('div.price-container > span.price')
                if not price:
                    price = food_info.select_one('div.price-container > span.price.red')
                price_text = price.text if price else ''
                price_d = float(''.join(filter(str.isdigit, price_text))) if price_text else 0.0

                title = food_info.select_one('div.title').text

                filtered_product_name = parse_string(title, markets_data.blacklist)  # You may apply your filter here

                product = {
                    'productId': ref.id,
                    'name': title,
                    'price': price_d,
                    'image': image,
                    'page': pg_ct,
                    'tag': filtered_product_name,
                    'supermarket': current_supermarket_name,
                    'category': category
                }
                print(product)

                # db.document(f'tags/{category}/{item}/{ref.id}').set(product)
                # ref.set(product)


async def main():
    await generate_products()


asyncio.run(main())
