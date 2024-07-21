from PIL import Image,ImageFilter

img = Image.open("cat.jpg")

img.show()

print (img.size)
print (img.width)
print (img.height)

rotated_img = img.rotate(45)
rotated_img.save('rotate.png')


cropped_img = img.crop((20,20,400,400))  # leftest toppest pixel and rightest bottomest pixel
cropped_img.save('crop.jpg')


filtered_img = img.filter(filter = ImageFilter.FIND_EDGES)
filtered_img.save(f'filtered_edge.jpg')


filtered_img = img.filter(filter = ImageFilter.SHARPEN)
filtered_img.save(f'filtered_sharp.jpg')

resize_img = img.resize((2109,1389))
resize_img.save('resized.jpg')


r,g,b = img.split()

r.save('red.jpg')
g.save('green.jpg')
b.save('blue.jpg')

imerge = Image.merge("RGB", (r, g, b))
imerge.save('merged.jpg')