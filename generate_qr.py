import qrcode
print(qrcode.__file__)

x = qrcode.QRCode()

msg = "hello world!"

x.add_data(msg)
x.make(fit=True)
res = x.make_image(fill_color="black",back_color="white")
res.save("haha.png")
print("done!!")