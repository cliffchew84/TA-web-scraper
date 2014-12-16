import urllib2, csv, os, time
from bs4 import BeautifulSoup

# Masking nature of the bot
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

base_link = "http://www.tripadvisor.com.sg/"
# Update if there are errorsbefore the loop ends
with open (r'C:\Users\User\Downloads\EM Project\Python Scripts\text files\attraction_links.txt', "r") as myfile:
    data=myfile.readlines()

''' This loop goes through the entire list from shopping_links.txt'''
# The new review_header identifier was included
for i_links in data[:]:
    print "Going through " + str(i_links)
    item = i_links
    link1 = base_link + item
    # print link1 

    # Setting up the place for amenity saving
    listing = item.split("-")
    place = listing[4]
    indexing_number = listing[2]
    # print place

    # test link: link1= "http://www.tripadvisor.com.sg/Attraction_Review-g294265-d2007558-Reviews-Loof-Singapore.html"
    # link1= "http://www.tripadvisor.com.sg//Attraction_Review-g294265-d1635998-Reviews-10_Scotts-Singapore.html"
    f_url = urllib2.urlopen(link1)
    soup = BeautifulSoup(f_url)

    # Reviewer information
    names = []
    locations = []
    review_titles = []
    review_dates = []
    actual_reviews = []
    review_scores = []
    # review_numbers = []
    
    # This is the counter the allows the program to loop through all TA attraction reviews.
    counter = 0 # Increments are done in 10s, ie, the number of reviews per page

    # Extracting a final counter from the top of the page
    # For the reviewers page ONLY: Pretty ugly coding I have to admit
    counter_limit = soup.find_all("h3", attrs={"class":"reviews_header"})
    if counter_limit ==[]:
        continue
    counter_l = str(counter_limit)
    counter_ll = counter_l.split(">")
    counter_lll = counter_ll[1].split(' ')
    counter_llll = counter_lll[0]
    counter_lllll = int(counter_llll.replace(',', ''))
    counter_x = int(round(counter_lllll/10.0)*10)

    while counter<counter_x: #counter_x is the limiting amount
        print ("Scraping " + link1)
        print " "
        f_url = urllib2.urlopen(link1)
        soup = BeautifulSoup(f_url)

        for mem in soup.find_all("div",attrs={"class":"member_info"}):
            # Names of reviewers
            for name in mem.find_all("div", attrs={"class":"username mo"}):
                n = name.get_text("\n",strip=True).encode('ascii', 'ignore')
                n = n.replace("/","").replace("\\","").replace(":","").replace("*","").replace("?","").replace("<","").replace(">","").replace("|","")
                names.append(n)

            # Locations
            for location in mem.find_all("div", attrs={"class":"location"}):
                l = location.get_text("\n",strip=True).encode('ascii', 'ignore')
                locations.append(l)

        # Review Titles
        for review_title in soup.find_all("span", attrs={"class":"noQuotes"}):
            rt = review_title.get_text("\n",strip=True).encode('ascii', 'ignore')
            review_titles.append(rt)

        # Review Dates
        for review_date in soup.find_all("span", attrs={"class":"ratingDate"}):
            rd = review_date.get_text()[9:].replace("\nNEW","").rstrip("\n").encode('ascii', 'ignore')
            review_dates.append(rd)

        # Actual Reviews
        for links in soup.find_all("div", attrs={"class":"quote"}):
            link = links.a.get('href')
            # print link
            link2 = base_link + link
            f_url2 = urllib2.urlopen(link2)
            soup2 = BeautifulSoup(f_url2)
            for review in soup2.find_all("p", attrs={"property":"v:description"},limit=1):
                ar = review.get_text().replace('\n', ' ').encode('ascii', 'ignore')
                # print actual_review
                actual_reviews.append(ar)

        # Reviews Scores
        for review_score in soup.find_all("div", attrs={"class":"rating reviewItemInline"}):
            rs = str(review_score.img)[10:11]
            review_scores.append(rs)
        '''
        # Reviews Numbers
        for review_number in soup.find_all("span", attrs={"class":"more"}):
            rn = review_number.get_text().split(" ")[0]
            print rn
        '''
        amenity = []
        for i in range(len(names)):
            amenity.append(place)
            
        # Gone through the entire loop
        list_total = list(zip(amenity,names,locations,review_titles, \
                              review_dates,review_scores,actual_reviews))
         
        # Save file into text
        # txt_f = (r"C:\Users\cliffchew84\Dropbox\SAS BIA\EM Project\Python Scripts\text files\shopping_" + place + ".txt")
        print "Copying all the info into each text file"
        for i in list_total:
            txt_f = (r"C:\Users\User\Downloads\EM Project\Python Scripts\text files\attractions\_" + place + "_" + i[1] + ".txt")
            f=csv.writer(open(txt_f,'w+'))
            f.writerow(i)
        
        print "FINISHED 10 TEXT FILES!!"
        # Note: Non_English text seems to be automatically removed? That needs to be confirmed '''

        counter+=10
        link1 = base_link + "Attraction_Review-g294265-" + str(indexing_number) + "-Reviews-or" + str(counter) + "-" + str(place) + "-Singapore.html#REVIEWS"
        
        print "Please wait for 1 secs before we proceed"
        time.sleep(1)
        print ("Moving to next 10: " + link1)

print "The entire process is done!"
