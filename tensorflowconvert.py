import os
import requests
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
cred = credentials.Certificate("doyourgroceries-fea564651a4e.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Base directory to save images
base_directory = 'directory'
os.makedirs(base_directory, exist_ok=True)


def get_images():
    # Reference to the 'tags/legume' document
    legume_ref = db.collection('tags').document('legume')
    subcollections = legume_ref.collections()

    for subcollection in subcollections:
        subcollection_name = subcollection.id  # Get the subcollection name
        subcollection_directory = os.path.join(base_directory, subcollection_name)
        os.makedirs(subcollection_directory, exist_ok=True)

        # Fetch all documents in the subcollection
        docs = subcollection.stream()

        for doc in docs:
            data = doc.to_dict()
            image_url = data.get('image')
            name = data.get('name')

            if image_url and name:
                try:
                    # Download the image
                    img_data = requests.get(image_url).content
                    # Ensure the filename is safe and valid
                    safe_name = "".join([c if c.isalnum() else "_" for c in name])
                    # Save the image with the name field as the filename
                    image_path = os.path.join(subcollection_directory, f'{safe_name}.jpg')
                    with open(image_path, 'wb') as handler:
                        handler.write(img_data)
                    print(f'Successfully saved {safe_name}.jpg in {subcollection_name}')
                except Exception as e:
                    print(f'Failed to download {safe_name}.jpg from {image_url}: {e}')


if __name__ == '__main__':
    get_images()
