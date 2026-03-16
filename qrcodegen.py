import qrcode
import qrcode.constants
from PIL import Image



def generate_fancy_qr_code(link, qr_filename):
    NAVY_BLUE = (0, 0, 0)
    CREAM_WHITE = (255, 255, 255)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color=CREAM_WHITE, back_color=NAVY_BLUE).convert("RGBA")

    logo = Image.open("optima_.png")
    logo_size = (qr_image.width // 4, qr_image.height // 4)
    logo = logo.resize(logo_size, Image.Resampling.LANCZOS)
    logo_position = (
        (qr_image.width - logo_size[0]) // 2,
        (qr_image.height - logo_size[1]) // 2
    )

    qr_image.paste(logo, logo_position, logo)
    qr_image.save(qr_filename)


if __name__ == "__main__":
    url = "https://wa.me/50588679238?text=Hola%20Optima%2C%20me%20gustaria%20cotizar%20un%20envio."
    filename = "optima-6.png"
    generate_fancy_qr_code(url, filename)
