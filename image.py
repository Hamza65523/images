import csv
import requests
import boto3
from dotenv import load_dotenv
import os
import glob
import shutil


load_dotenv()

s3 = boto3.client('s3', 
                    aws_access_key_id=os.getenv('Access_key_ID'), 
                    aws_secret_access_key=os.getenv('Secret_access_key'), 
                  region_name=os.getenv('region_name')
                    )

                    
def images_fun(row,count):
    try:
        img = row['images_url']
        # print('Current Url: ','image_name'+str(count)+'.jpg')
        img_data = requests.get(img).content
        with open('img/image_name'+str(count)+'.jpg', 'wb') as handler:
            handler.write(img_data)
    except:
        print('error')

def main():
    with open('image.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        count = 0
        print("start")
        for row in csv_reader:
            count +=1
            images_fun(row,count)

            
        BUCKET_NAME = 'biodata-images'
        FOLDER_NAME = 'img'

        csv_files = glob.glob("img\image_name*.jpg")

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
    