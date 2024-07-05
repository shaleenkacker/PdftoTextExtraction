import fitz  # PyMuPDF

doc = fitz.open("test.pdf")  # open a document

for page_index in range(len(doc)):  # iterate over pdf pages
    page = doc[page_index]  # get the page
    image_list = page.get_images(full=True)

    # print the number of images found on the page
    if image_list:
        print(f"Found {len(image_list)} images on page {page_index}")
    else:
        print("No images found on page", page_index)

    for image_index, img in enumerate(image_list, start=1):  # enumerate the image list
        xref = img[0]  # get the XREF of the image
        pix = fitz.Pixmap(doc, xref)  # create a Pixmap

        if pix.n - pix.alpha > 3:  # CMYK: convert to RGB first
            pix = fitz.Pixmap(fitz.csRGB, pix)

        pix.save(f"page_{page_index}-image_{image_index}.png")  # save the image as png
        pix = None
