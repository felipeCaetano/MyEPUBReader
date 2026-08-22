import os

from ebooklib import epub
import ebooklib
from ebooklib.utils import debug



# Abre o arquivo EPUB
livro = epub.read_epub('dokumen.pub_3d-printing-for-dummies-3nbsped-9781394169498-9781394169474-9781394169481.epub')

# Lê os metadados (ex: título)
titulo = livro.get_metadata('DC', 'title')
print("Título:", titulo)


# Export all images from the Book
for image in livro.get_items_of_type(ebooklib.ITEM_IMAGE):
    with open(os.path.basename(image.get_name()), "wb") as f:
        f.write(image.get_content())

# Percorre os documentos do livro
with open("output.html", "w", encoding="utf-8") as file:
    for item in livro.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        file.write(item.get_content().decode('utf-8'))
