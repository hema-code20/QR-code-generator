import qrcode 
features = qrcode.QRCode(version=1, box_size=10, border=2)
features.add_data('https://github.com/hema-code20')
features.make(fit=True)
generate_image = features.make_image(fill_color="teal", back_color="white")
generate_image.save('qrcode.png')