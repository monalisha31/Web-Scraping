import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from itertools import zip_longest






filename = 'midwayusa.txt'

class scraper:
    def __init__(self):
        self.name = []
        self.purls = []
        self.pavails = []
        self.new_strings = []

    def get_url(self):
        with open(filename, 'r') as f:
            for url in f:
                url1 = url.strip()
                url2 = url1.strip('\n')
                self.purls.append(url2)

    def scrapping(self):
        for purl in self.purls:
            page = requests.get(purl)
      

         
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all(id="l-product-description")
            for result in results:
                name1 = result.text
                name2 = name1.strip()
                name3 = name2.strip('\n')
                name4 = name3.strip('\r')
                self.name.append(name4)
      
            stocks = soup.find_all("mw-modal-trigger",{'class':"product-block-status-availability"})
            for stock in stocks:
            
         

                avail = stock.text
                line = avail.strip()
                line1 = line.strip('\n')
                self.pavails.append(line1)
        
        for pavail in self.pavails:

            new_string = pavail.replace("Mixed Availability", "Variant")

            new_string = new_string.replace("Temporarily unavailable", "Out of Stock")

            new_string = new_string.replace("Discontinued", "Out of Stock")



            self.new_strings.append(new_string)

    def csv_file(self):
        d = [self.name, self.purls, self.new_strings]
        export_data = zip_longest(*d, fillvalue = '')

        with open('result1.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(("Name", "URL", "availability"))
            wr.writerows(export_data)
        myfile.close()

if __name__ == "__main__":
    
    nasdaq = scraper()
    nasdaq.get_url()
    nasdaq.scrapping()
    nasdaq.csv_file()
    



    
        













        

