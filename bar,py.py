import qrcode

data="https://github.com/nishatdbdlt"
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save={"my_qrcodee.png"}
print('save as:my_qrcodee.png')