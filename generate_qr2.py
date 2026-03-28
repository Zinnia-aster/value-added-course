import qrcode
x= qrcode.QRCode()
upi_id = "#upi_id#"
name = "priya"
amount = "100"
link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

x.add_data(link)
x.make(fit=True)
res = x.make_image(fill_color="black",back_color="white")
res.save("ha.png")
print("done!!")
