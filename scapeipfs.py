import requests
import os
import time

def download_image(url, folder, image_number):
    print(f"Attempting to download image from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(folder, f'{image_number}.png')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image saved to {file_path}")
    else:
        print(f"Failed to download image from {url}. Status code: {response.status_code}")

def main():
    base_url = 'https://shdw-drive.genesysgo.net/9DEPA5HdWF9aWYuwWB6cpnT7exK7Cpw7WvDwx8qe9GqT'
    directories = {'': 8880}
    delay = 0.01  # Delay in seconds
    main_folder = 'SAGA MONKES'  # Main folder name

    print("Starting the image download process...")

    for directory, count in directories.items():
        folder = os.path.join(main_folder, directory)
        if not os.path.exists(folder):
            print(f"Creating folder: {folder}")
            os.makedirs(folder)

        for i in range(28, count + 1):
            url = f'{base_url}{directory}/{i}.png'  # Fetches the image without .png extension
            download_image(url, folder, i)  # Saves the image with .png extension
            print(f"Waiting for {delay} second(s) before next download...")
            time.sleep(delay)

    print("Image download process completed.")

if __name__ == "__main__":
    main()
