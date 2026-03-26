import requests
import os
from urllib.parse import quote

BASE_URL = "http://127.0.0.1:8080"


IMAGE_PATH = "mars_photo1.jpg"


def upload_image(image_path):
    url = f"{BASE_URL}/upload"

    with open(image_path, "rb") as f:
        files = {
            "image": (os.path.basename(image_path), f, "image/jpeg")
        }
        response = requests.post(url, files=files)

    response.raise_for_status()
    data = response.json()

    print("Uploaded:", data)
    return data["image_url"]


def get_image_url(filename):

    encoded_filename = quote(filename)
    url = f"{BASE_URL}/image/{encoded_filename}"

    headers = {
        "Content-Type": "text"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    print("GET response:", data)

    return data["image_url"]


def delete_image(filename):
    encoded_filename = quote(filename)
    url = f"{BASE_URL}/delete/{encoded_filename}"

    response = requests.delete(url)
    response.raise_for_status()

    data = response.json()
    print("DELETE response:", data)


def main():

    image_url = upload_image(IMAGE_PATH)


    filename = image_url.split("/")[-1]
    print("Filename:", filename)


    get_image_url(filename)


    delete_image(filename)


if __name__ == "__main__":
    main()