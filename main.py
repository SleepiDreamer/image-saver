import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App")

        # Open the image using PIL
        self.pil_image = Image.open("DSC09022.jpg")
        self.image = ImageTk.PhotoImage(self.pil_image)

        # Add the image to a label
        label = tk.Label(self.root, image=self.image)
        label.pack()

        # Add buttons for selecting different images
        button1 = tk.Button(self.root, text="Select Image 1", command=self.select_image_1)
        button1.pack()
        button2 = tk.Button(self.root, text="Select Image 2", command=self.select_image_2)
        button2.pack()

    def select_image_1(self):
        # This function will be called when button 1 is clicked
        self.pil_image = Image.open("DSC09022.jpg")
        self.image.configure(image=ImageTk.PhotoImage(self.pil_image))
        self.image.image = self.pil_image

    def select_image_2(self):
        # This function will be called when button 2 is clicked
        self.pil_image = Image.open("DSC09023.jpg")
        self.image.configure(image=ImageTk.PhotoImage(self.pil_image))
        self.image.image = self.pil_image

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()