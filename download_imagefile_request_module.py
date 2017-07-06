import requests
url='http://www.motorcycle-usa.com/wp-content/uploads/2016/01/Ducati-Multi1200Pikes-20161.jpg?378220'
res=requests.get(url,stream=True)

if res.status_code==200:
    with open('download_image_file.jpg','wb') as f:
        for line in res:
            f.write(line)
else:
    print('file didnt download properly', res.raise_for_status())

