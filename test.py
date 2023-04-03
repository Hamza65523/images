import os
import csv
from threading import Thread

def images_fun(row,count):
    try:
        img = row['restaurant_logo']
        print('Current Url: ','image_name'+str(count)+'.jpg')
        os.system(f'curl {img} > img/image{count}.jpg')
           # make a GET request to the image URL
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

        # print(count)
        # print(count /5 )
        # print(count /5 *2)
        # print(count /5 *3)
        # print(count /5 *4)
        # print(count /5 *5)
            # if 7604>count:
            images_fun(row,count)


    
if __name__ == "__main__":
    # Thread(target=fun1).start()
    # Thread(target=fun2).start()
    # Thread(target=fun3).start()
    # Thread(target=fun4).start()
    # Thread(target=fun5).start()
    main()
    



