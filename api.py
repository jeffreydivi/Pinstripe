# Pinstripe v1.0

# Image processing
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
from io import BytesIO

# Web server
from flask import Flask, send_file, request, Response
app = Flask(__name__)

@app.route('/')
def img():

    # Get data.
    data = request.args

    try:
        text = request.args["subject"].upper()
    except:
        text = "COT"

    try:
        text2 = request.args["course"].upper()
    except:
        text2 = "3103"

    try:
        # Take a hexadecimal color and convert it to RGB.
        hexStr = request.args["color"].replace("#","")
        r = int(hexStr[0:2], 16)
        g = int(hexStr[2:4], 16)
        b = int(hexStr[4:6], 16)
        color = (r, g, b)
    except:
        # The default color is #ffc904, or UCF Gold. Go Knights!
        color = (255, 201, 4)

    # Image size: 512x512
    size = 512

    # Create the image.
    img = Image.new("RGBA", (size, size), (35,31,32,255))

    # Load the fonts. These fonts are *not* included in this repo.
    
    # Since the goal is to resemble UCF's official font, Gotham, I'd take a look at the font family iCeil Gotham.
    
    normal = ImageFont.truetype("medium.otf", 106)
    ultra = ImageFont.truetype("ultra.otf", 126)

    d = ImageDraw.Draw(img)

    # Draw pinstripe
    pos = 150
    d.line((-(pos), (pos)) + ((pos), -(pos)), fill=color, width=300)

    # Licensing note: The text-centering algorithm below is adapted from https://stackoverflow.com/a/55774238

    # Draw ultra text
    w, h = d.textsize(text, font=ultra)
    d.text(((size-w)/2, ((size-h)/2)-60), text, font=ultra, fill=(255,255,255,255))

    # Draw normal text
    w, h = d.textsize(text2, font=normal)
    d.text(((size-w)/2, ((size-h)/2)+60), text2, font=normal, fill=(255,255,255,255))

    # Save to memory.
    file = BytesIO()
    img.save(file, "png")
    file.seek(0)

    return send_file(
            file,
            attachment_filename="icon.png",
            mimetype="image/png"
           )

if __name__ == '__main__':
   app.run()
