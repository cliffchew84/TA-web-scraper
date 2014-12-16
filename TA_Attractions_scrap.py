import urllib2, csv, os
from bs4 import BeautifulSoup

# Masking nature of the bot
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

# Creating of text file to save all the locations
current_folder = os.path.dirname(os.path.realpath(__file__))
txt_f = (current_folder + r"/attraction_corpus.txt")

f=csv.writer(open(txt_f,'w+'))
f.writerow(["Attraction Names","Links"])

base_link = "http://www.tripadvisor.com.sg/"
counter = 0 # This is the counter the allows the program to loop through all the attractions on TA.

link1 = base_link + "Attractions-g294265-Activities-Singapore.html#TtD"
while counter<30: # 360 for entire attractions list
    print ("Scraping " + link1)

    f_url = urllib2.urlopen(link1)
    soup = BeautifulSoup(f_url)

    attractions = []
    linkages = []
    # Names of attractions
    for links in soup.find_all("a", attrs={"class":"property_title"}):
        name = links.get_text("\n",strip=True)
        link = links.get('href')
        print name
        print link
        attractions.append(name)
        linkages.append(link)
        print " "

    list_total = list(zip(attractions,linkages))

    # Copying the data into the text file
    for i in list_total:
        f=csv.writer(open(txt_f,'a+'))
        f.writerow(i)

    counter+=30
    link1 = base_link + "Attractions-g294265-Activities-oa" + str(counter) + "-Singapore.html#TtD"
    print ("Moving to next 30: " + link1)
    print (" ")

print("Congrats, your web scraper has successfully scrapped all the sites you wanted.")
