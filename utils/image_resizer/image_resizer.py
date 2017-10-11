import PIL

# Queremos gerar uma imagem com tamanho 300x200
wsize = 300
hsize = 200

img = PIL.Image.open('/path/to/original_picture.png')

# redimensionamos sem perder a qualidade
img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
img.save('/path/to/new_img.png')