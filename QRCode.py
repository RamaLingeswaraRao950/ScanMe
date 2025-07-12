import qrcode

# Generating QR Code for links
qr = qrcode.make("Please reach out to me")
data = "https://portfolio-ten-omega-75.vercel.app/"
qr = qrcode.make(data)
qr.save("Me.png")
qr.show()


# Generating QR Code for bio-data
qr = qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name = input("Enter your name:")
age = int(input("Enter yor age:"))
email = input("Enter your email:")
mobile = int(input("Enter your your mobile number:"))
data = {"Name": name, "Age": age, "Email": email, "Mobile": mobile}
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save("mydetails_in_qr.png")
img.show()
