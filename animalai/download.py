from flickrapi import FlickrAPI 
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APキーの情報

key = "5043e3d8d855498409c8f15417aa7cea"
secret = "718d952fca5f6457"
wait_time = 1

#保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format ='parsed-json')
result = flickr.photos.search(
text = animalname,
per_paeg =400,
media = 'photos',
safe_search = 1,
extras = 'url_q, licence'
)

photos = result['photos']
#返り値を表示する
#pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + 'jpg'
    if os.path.exists(filepath): continue 
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
    


