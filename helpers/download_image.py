import requests


def download_image():
    picture_addresses = {
        'pic_1.png': 'http://www.tiptopglobe.com/forum/images/avatars/gallery/ostatni/0026.jpg',
        'pic_2.png': 'http://www.tiptopglobe.com/forum/images/avatars/gallery/ostatni/0225.jpg',
        'pic_3.png': 'http://www.tiptopglobe.com/forum/images/avatars/gallery/ostatni/0523.jpg'
    }
    for i in picture_addresses:
        with open(".\\images\\" + i, 'wb') as pic:
            response = requests.get(picture_addresses.get(i), stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break
                pic.write(block)
