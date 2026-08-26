from rembg import remove, new_session
from PIL import Image

def remover(path):
    anime = new_session(model_name="isnet-anime")
    opened = Image.open(path)
    removed = remove(opened, session=anime)
    removed.save("tmp/removed.png")