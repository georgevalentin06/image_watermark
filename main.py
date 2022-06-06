from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageChops


window = Tk()
window.title("Image Watermark")
window.minsize(width=220, height=200)
window.config(padx=15, pady=15)

def browse_watermark():
    watermark_filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("JPG files",
                                                      ".jpg"),
                                                     ("JPEG files",
                                                      ".jpeg")
                                                     ))

    watermark_label.config(text=watermark_filename)

def browse_image():
    image_filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("JPG files",
                                                      ".jpg"),
                                                     ("JPEG files",
                                                      ".jpeg")
                                                     ))

    image_label.config(text=image_filename)


watermark_btn = Button(text="Upload watermark", width=16, command=browse_watermark)
watermark_btn.pack(pady=3)
watermark_label = Label(text="", width=35)
watermark_label.pack(pady=3)

image_btn = Button(text="Upload image", width=16, command=browse_image)
image_btn.pack(pady=3)
image_label = Label(text="", width=35)
image_label.pack(pady=3)

def merge_images(img1=watermark_label, img2=image_label):
    watermark_path = img1.cget("text")
    watermark_image = Image.open(watermark_path)

    image_path = img2.cget("text")
    main_image = Image.open(image_path)

    img_w, img_h = watermark_image.size
    bg_w, bg_h = main_image.size
    offset = ((bg_w - img_w - 50) // 1, (bg_h - img_h - 50) // 1)

    main_image.paste(watermark_image, offset)
    main_image.save(image_path)


submit_btn = Button(text="Submit", width=16, command=merge_images)
submit_btn.pack(pady=18)

window.mainloop()