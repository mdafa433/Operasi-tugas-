import imghdr
import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
    )
img = qrcode.make(
    'https://api.whatsapp.com/send?phone=6288210274828&text=Chat%20Dong%20Bestiee%20Jangan%20Di%20Liat%20Doang'
)
img.save('myqr.png')
img.show()
