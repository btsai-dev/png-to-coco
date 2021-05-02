import gen_annotation.flags as flags
import gen_annotation.segcolor as segcolor

def generate(img_raw, file_name, image_id, flag=0, categories=None):
    if categories is None:
        categories = {}
    width, height = img_raw.size
    if flag == flags.COLOR:
        mask = segcolor.get_colors(img_raw)






