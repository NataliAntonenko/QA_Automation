import requests
import os

BASE_URL = "https://images-api.nasa.gov"


search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()

data = search_response.json()


items = data.get("collection", {}).get("items", [])

nasa_ids = []
for item in items:
    data_block = item.get("data", [])
    if data_block:
        nasa_id = data_block[0].get("nasa_id")
        if nasa_id:
            nasa_ids.append(nasa_id)


nasa_ids = nasa_ids[:2]

print("Selected NASA IDs:", nasa_ids)


def get_jpg_url(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    response = requests.get(asset_url)
    response.raise_for_status()

    asset_data = response.json()
    items = asset_data.get("collection", {}).get("items", [])


    for item in items:
        href = item.get("href", "")
        if href.lower().endswith(".jpg"):
            return href

    return None


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)


filenames = ["mars_photo1.jpg", "mars_photo2.jpg"]

for i, nasa_id in enumerate(nasa_ids):
    jpg_url = get_jpg_url(nasa_id)

    if jpg_url:
        print(f"Downloading {jpg_url}")
        download_image(jpg_url, filenames[i])
    else:
        print(f"No JPG found for {nasa_id}")

print("Done.")