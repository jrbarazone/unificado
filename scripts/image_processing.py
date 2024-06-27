from PIL import Image

def remove_background(image_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    datas = image.getdata()

    new_data = []
    for item in datas:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    output_path = image_path.replace(".png", "_no_bg.png")
    image.putdata(new_data)
    image.save(output_path, "PNG")
    return output_path
