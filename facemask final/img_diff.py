from PIL import Image
import imagehash
import cv2

img = Image.open('img 100.jpg')
rgbimg = Image.new("RGBA", img.size)
rgbimg.paste(img)
rgbimg.save('img 100r.png')

img = Image.open('image1.jpg')
rgbimg = Image.new("RGBA", img.size)
rgbimg.paste(img)
rgbimg.save('image1r.png')

hash = imagehash.average_hash(Image.open('img 100r.png'))
otherhash = imagehash.average_hash(Image.open('image1r.png'))
 
x = hash - otherhash
print(x)

if (x>10):
    print("different")

else:
    print("same")