from bs4 import BeautifulSoup
#import BeautifulSoup4
import requests
#import csv

source = requests.get('https://en.wikipedia.org/wiki/National_Football_League').text

soup = BeautifulSoup(source, 'lxml')

###for saving to csv file###
#csv_file = open('asdf.csv','w')

#csv_writer = csv.writer(csv_file)
#csv_writer.whiterow(['headline', 'summary', 'video_link'])
#########


#print(soup.prettify())

article = soup.find('table')
for article in soup.find_all('table'):


#print(article.prettify())

#headline = article.caption.text
#print(headline)

#summary = article.find('', class_='noprint').text
#print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
#print(vid_id)
#vid_id = 'asdf'

yt_link = f'https://youtube.com/watch?v={vid_id}'
#print(yt_link)

#In case code breaks because of missing youtube link or info

try: 
    vid_src = article.find('iframe', class_='youtube-player')['src']
    
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    
    yt_link = f'https://youtube.com/watch?v={vid_id}'
except Exception as e:
    yt_link = none
    
    print(yt_link)
    print()


#### for csv file ####
    csv_writer.writerow([headline, summary, yt_link])
    
csv_file.close()


