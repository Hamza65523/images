import csv
import requests
import boto3
from dotenv import load_dotenv
import os
import glob
import shutil

load_dotenv()

brokenlink = []

s3 = boto3.client('s3', 
                    aws_access_key_id=os.getenv('Access_key_ID'), 
                    aws_secret_access_key=os.getenv('Secret_access_key'), 
                  region_name=os.getenv('region_name')
                    )

def images_fun(row,count):
    try:
        img = row['restaurant_logo']
        print('Current Url: ','image_name'+str(count)+'.jpg')
           # make a GET request to the image URL
        os.system(f'curl {img} > img/image{count}.jpg')

        # response = requests.get(img)
        # # check if the request was successful (status code 200)
        # if response.status_code == 200:
        #     # save the image to a file
        #     with open(f'img/image{count}.jpg', 'wb') as f:
        #         f.write(response.content)
        #     # increment the downloaded_images counter
        # # if the request was not successful, print an error message
        # else:
        #     print(f'Error downloading image (status code {response.status_code})')
    
        # img_data =  requests.get(img).content
        # with open('img/image_name'+str(count)+'.jpg', 'wb') as handler:
        #     handler.write(img_data)
    except:
        print('error')

def main():
    with open('demo1.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        count = 0
        print("start")
        for row in csv_reader:
            count +=1
            if count >=7354:
                images_fun(row,count)
        BUCKET_NAME = 'biodata-images'
        FOLDER_NAME = 'img'

        csv_files = glob.glob("img\image*.jpg")

        for filename in csv_files:
            key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
            print("Putting %s as %s" % (filename,key))
            s3.upload_file(filename, BUCKET_NAME, key)


        for filename in os.listdir(FOLDER_NAME):
            file_path = os.path.join(FOLDER_NAME, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        print("All_Done")

    
if __name__ == "__main__":
    main()
    

# ------------------------ Match start (https://media-cdn.) or end (.jpg) points  --------------------

# import re

# link = 'https://media-cdn.tripadvisor.com/media/photo-s/1d/8b/c9/41/caption.jpg'

# print(re.match(r'(https://media-cdn.|https)://.*\.(jpg|png)$', link)[0])