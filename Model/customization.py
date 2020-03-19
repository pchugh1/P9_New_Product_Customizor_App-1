import base64
from io import BytesIO

from PIL import Image

def mask_loop(mask, wood_id):
    mask = Image.open(BytesIO(base64.b64decode(mask.decode('utf-8'))))
    mask = mask.convert("RGBA")
    wood = Image.open(BytesIO(base64.b64decode(wood_id.decode('utf-8'))))
    wood = wood.convert("RGBA")
    files = [wood, mask]

    result = Image.new("RGBA", (1000, 1000))

    for i in range(0, len(files)):
        result.paste(files[i], (0, 0), files[i])

    img = BytesIO()
    result.save(img, format='PNG')
    img = img.getvalue()
    result_encoded = base64.b64encode(img)
    return result_encoded
