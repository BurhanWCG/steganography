from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

def encode_message():
    input_image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG Files", "*.png")])
    if not input_image_path:
        return

    message = text_message.get("1.0", END).strip()
    if not message:
        messagebox.showwarning("Warning", "Please enter a secret message.")
        return

    img = Image.open(input_image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    binary_message = ''.join([format(ord(i), '08b') for i in message]) + '1111111111111110'

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = img.getpixel((col, row))
                r, g, b = pixel[:3]

                r = (r & ~1) | int(binary_message[index])
                index += 1
                if index < len(binary_message):
                    g = (g & ~1) | int(binary_message[index])
                    index += 1
                if index < len(binary_message):
                    b = (b & ~1) | int(binary_message[index])
                    index += 1

                if len(pixel) == 4:
                    encoded.putpixel((col, row), (r, g, b, pixel[3]))  # Keep alpha channel
                else:
                    encoded.putpixel((col, row), (r, g, b))

    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if output_path:
        encoded.save(output_path)
        messagebox.showinfo("Success", f"Message encoded and saved to {output_path}")

def decode_message():
    input_image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG Files", "*.png")])
    if not input_image_path:
        return

    img = Image.open(input_image_path)
    binary_data = ""

    for pixel in img.getdata():
        for value in pixel[:3]:
            binary_data += str(value & 1)

   
    bytes_list = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for byte in bytes_list:
        if byte == '11111110':  
            break
        message += chr(int(byte, 2))

    text_message.delete("1.0", END)
    text_message.insert(END, message)

root = Tk()
root.title("Image Steganography")
root.geometry("500x400")
root.resizable(False, False)

Label(root, text="Enter your secret message:", font=("Arial", 12)).pack(pady=10)
text_message = Text(root, height=10, width=60)
text_message.pack()

frame = Frame(root)
frame.pack(pady=20)

Button(frame, text="Encode", command=encode_message, width=20, bg='green', fg='white').grid(row=0, column=0, padx=10)
Button(frame, text="Decode", command=decode_message, width=20, bg='blue', fg='white').grid(row=0, column=1, padx=10)

root.mainloop()
