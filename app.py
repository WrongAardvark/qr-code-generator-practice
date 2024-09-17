import qrcode

# insert URL here:
url = ""
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size (number of boxes)
)

qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(fill="black", back_color="white")

# image is saved as png
qr_img.save("qr_image.png")
