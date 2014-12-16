import urllib2, csv, os
from bs4 import BeautifulSoup

# Masking nature of the bot
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

# Creating of text file to save all the locations
current_folder = os.path.dirname(os.path.realpath(__file__))
txt_f = (current_folder + r"/attraction_links.txt")

f=csv.writer(open(txt_f,'w+'))
base_link = "http://www.tripadvisor.com.sg/"
counter = 0 # This counter allows the program to loop through all attractions on TA.

link1 = base_link + "Attractions-g294265-Activities-Singapore.html#TtD"
while counter<360: # 360 for entire attractions list
    print ("Scraping " + link1)

    f_url = urllib2.urlopen(link1)
    soup = BeautifulSoup(f_url)

    attractions = []
    linkages = []
    # Names of attractions
    for links in soup.find_all("a", attrs={"class":"property_title"}):
        link = links.get('href')
        print link
        linkages.append([link,])
        print " "

    # Copying the data into the text file
    for i in linkages:
        f=csv.writer(open(txt_f,'a+'))
        f.writerow(i)

    counter+=30
    link1 = base_link + "Attractions-g294265-Activities-oa" + str(counter) + "-Singapore.html#TtD"
    print ("Moving to next 30: " + link1)
    print (" ")

print("Congrats, your web scraper has successfully scrapped all the sites you wanted.")
