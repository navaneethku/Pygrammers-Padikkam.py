import qrcode
qrCodeData = input("Enter your QRCode Data\n")
qr = qrcode.QRCode(
    version = 1,
    box_size = 5,
    border = 2
)
qr.add_data(qrCodeData)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("QRCode saved as qrcode.png")