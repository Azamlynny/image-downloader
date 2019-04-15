import io

from PIL import Image
import requests 

def download_image(url, image_file_path):
    try:
        r = requests.get(url, timeout=1.0) # Increase timeout on slower networks
    except:    
        print("Failed to connect to: " + url)
    else:
        try:
            with Image.open(io.BytesIO(r.content)) as im:
                im.save(image_file_path + ".jpg", "JPEG")
        except:
            print("Failed opening the image at the url: " + url)

        print('[' + str(i) + '/' + str(download_size) + "] Image downloaded from: " + str(url))
    
input = open('urls.txt', 'r')
url = input.readline()

download_size = 10 # Change this to download the first n links to images

for i in range(download_size + 1):
    try:
        url = input.readline()
    except:
        print("Could not read the link due to special characters")
    else:
        url = url.replace("\n", "")
        download_image(url, "./Images/image" + str(i + 1))
    
input.close()