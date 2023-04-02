import requests

# set the URL of the image you want to download
url = 'https://media-cdn.tripadvisor.com/media/photo-s/18/14/08/f2/lucky-takeaway-saltney.jpg'

# set the number of images you want to download
num_images = 10

# set up a loop to download images until the desired number has been reached
downloaded_images = 0
while downloaded_images < num_images:
    # make a GET request to the image URL
    response = requests.get(url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
        # save the image to a file
        with open(f'image{downloaded_images}.jpg', 'wb') as f:
            f.write(response.content)

        # increment the downloaded_images counter
        downloaded_images += 1

    # if the request was not successful, print an error message
    else:
        print(f'Error downloading image (status code {response.status_code})')

    # break out of the loop if the desired number of images has been reached
    if downloaded_images == num_images:
        break