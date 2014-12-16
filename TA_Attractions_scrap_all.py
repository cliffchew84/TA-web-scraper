''' This scraps all
1. Name of the POI
2. HTML link POI
3. Review Totals
4. Address
5. Category (if any)
'''

import urllib2, csv, os
from bs4 import BeautifulSoup

# Masking nature of the bot
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

# Creating of text file to save all the locations
# txt_f = (r"C:\Users\User\Downloads\attraction_corpus.txt")
txt_f = (r"C:\Users\cliffchew84\Dropbox\SAS BIA\EM Project\Python Scripts\attraction_total.txt")

f=csv.writer(open(txt_f,'w+'))

base_link = "http://www.tripadvisor.com.sg/"
counter = 0 # This is the counter the allows the program to loop through all the attractions on TA.

link1 = base_link + "Attractions-g294265-Activities-Singapore.html#TtD"
while counter<360: # 360 for entire attractions list
    print ("Scraping " + link1)

    f_url = urllib2.urlopen(link1)
    soup = BeautifulSoup(f_url)
    
    attractions = []
    linkages = []
    tr_counts = []
    categories = []
    
    # Names and HTML links
    for links in soup.find_all("a", attrs={"class":"property_title"}):
        name = links.get_text("\n",strip=True)
        link = links.get('href')
        attractions.append(name)
        linkages.append(link)

    # Total review counts
    for r_total in soup.find_all("span", attrs={"class":"more"}):
        r_counts = float(r_total.get_text("\n",strip=True).split(" ")[0].replace(",",""))
        tr_counts.append(r_counts)
        
    list_total = list(zip(attractions,linkages,tr_counts))

    # Copying the data into the text file
    for i in list_total:
        f=csv.writer(open(txt_f,'a+'))
        f.writerow(i)
    
    counter+=30
    link1 = base_link + "Attractions-g294265-Activities-oa" + str(counter) + "-Singapore.html#TtD"
    print ("Moving to next 30: " + link1)
    print (" ")

print("Congrats, your web scraper has successfully scrapped all the sites you wanted.")
