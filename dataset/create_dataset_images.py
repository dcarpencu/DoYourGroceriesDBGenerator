import os
import requests
import firebase_admin
from firebase_admin import credentials, firestore

from database_writer import markets_data

cred = credentials.Certificate("doyourgroceries-fea564651a4e.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

base_directory = 'directory'
os.makedirs(base_directory, exist_ok=True)


def get_images():
    for category in markets_data.supermarket_categories:
        ref = db.collection('tags').document(category)
        subcollections = ref.collections()

        for subcollection in subcollections:
            subcollection_name = subcollection.id
            subcollection_directory = os.path.join(base_directory, subcollection_name)
            os.makedirs(subcollection_directory, exist_ok=True)

            docs = subcollection.stream()

            for doc in docs:
                data = doc.to_dict()
                image_url = data.get('image')
                name = data.get('name')

                if image_url and name:
                    try:
                        img_data = requests.get(image_url).content
                        safe_name = "".join([c if c.isalnum() else "_" for c in name])
                        image_path = os.path.join(subcollection_directory, f'{safe_name}.jpg')
                        with open(image_path, 'wb') as handler:
                            handler.write(img_data)
                        print(f'Successfully saved {safe_name}.jpg in {subcollection_name}')
                    except Exception as e:
                        print(f'Failed to download {safe_name}.jpg from {image_url}: {e}')


if __name__ == '__main__':
    get_images()
