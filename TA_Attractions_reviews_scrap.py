import urllib2, csv, os
from bs4 import BeautifulSoup

# Masking nature of the bot
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

'''
# Creating of text file to save all the locations
# txt_f = (r"C:\Users\User\Downloads\attraction_corpus.txt")
txt_f = (r"C:\Users\cliffchew84\Dropbox\SAS BIA\EM Project\Python Scripts\attraction_corpus.txt")

f=csv.writer(open(txt_f,'w+'))
f.writerow(["Attraction Names","Links"])
'''

base_link = "http://www.tripadvisor.com.sg/"
# This is the counter the allows the program to loop through all TA attraction reviews.
# Increments are done in 10s, ie, the number of reviews per page
counter = 0
''' This portion is '''

''' User profile
Location of reviewer --> div class="location"
Name of revier --> div class="username mo" next_sibling

Rating from reviewer -> span class="rate sprite-rating_s rating_s"
Rating Title --> span class="noQuotes"
Rating Date --> span class="ratingDate"

Actual Review --> div class="entry"
'''

link1 = base_link + "Attraction_Review-g294265-d2007558-Reviews-Loof-Singapore.html"
f_url = urllib2.urlopen(link1)
soup = BeautifulSoup(f_url)

# This provides with reviewer information
names = []
locations = []

for mem in soup.find_all("div",attrs={"class":"member_info"}):
    # Names of reviewers
    for name in mem.find_all("div", attrs={"class":"username mo"}):
        n = name.get_text("\n",strip=True)
        names.append(n)

    # Locations of reviewers
    for location in mem.find_all("div", attrs={"class":"location"}):
        l = location.get_text("\n",strip=True)
        locations.append(l)

# Review Titles
review_titles = []
for review_title in soup.find_all("span", attrs={"class":"noQuotes"}):
    rt = review_title.get_text("\n",strip=True)
    review_titles.append(rt)

# Review Dates
review_dates = []
for review_date in soup.find_all("span", attrs={"class":"ratingDate"}):
    rd = str(review_date.get_text("\n",strip=True))[9:]
    review_dates.append(rd)

# Actual Reviews
actual_reviews = []
for actual_review in soup.find_all("div", attrs={"class":"entry"}):
    ar = actual_review.get_text("\n",strip=True)
    actual_reviews.append(ar)

# Reviews Scores
review_scores = []
for review_score in soup.find_all("div", attrs={"class":"rating reviewItemInline"}):
    rs = str(review_score.img)[10:11]
    review_scores.append(rs)

'''
# Print everything for checks
for rt in review_titles:
        print rt
print ""

for rd in review_dates:
    print rd
print ""

for n in names:
    print n
print ""

for l in locations:
    print l
print ""
'''

list_total = list(zip(names,locations,review_titles, \
                      review_dates,review_scores,actual_reviews))

'''
link1 = base_link + "Attraction_Review-g294265-d2007558-Reviews-Loof-Singapore.html"
while counter<10: # __ for entire attractions list
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
    link1 = base_link + "Attraction_Review-g294265-d2007558-Reviews-or" + str(counter) + "Loof-Singapore.html#REVIEWS"
    print ("Moving to next 10: " + link1)
    print (" ")

print("Congrats, your web scraper has successfully scrapped all the sites you wanted.")
'''
