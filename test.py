import wget
import csv



def images_fun(row):
    url = row['images_url']
    wget.download(url)

def main():
    with open('image.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        count = 0
        print("start")
        for row in csv_reader:
            count +=1
            images_fun(row)
     

    
if __name__ == "__main__":
    main()
