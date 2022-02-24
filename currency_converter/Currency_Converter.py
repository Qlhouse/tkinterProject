from tkinter import *


class Currency_Converter:
    def __init__(self):
        window = Tk()  # Create application window
        window.title("Currency Converter")  # Add title to application window
        # Add background color to application window
        window.configure(bg="yellow")

        # Adding Label widgets to application window
        Label(window, font="Helvetica 12 bold", bg="yellow",
              text="Amount to convert").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="yellow",
              text="Conversion Rate").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="yellow",
              text="Converted Amount").grid(row=3, column=1, sticky=W)

        # Create objects and add entry functions
        self.amount_to_convert_var = StringVar()
        Entry(window, textvariable=self.amount_to_convert_var,
              justify=RIGHT).grid(row=1, column=2)
        self.conversion_rate_var = StringVar()
        Entry(window, textvariable=self.conversion_rate_var,
              justify=RIGHT).grid(row=2, column=2)
        self.converted_amount_var = StringVar()
        label_converted_amount_var = Label(window, font="Helvetica 12 bold", bg="yellow",
                                           textvariable=self.converted_amount_var).grid(row=3, column=2, sticky=E)

        # Create convert and clear buttons. Whe clicked they will call their respective functions
        btnConvertedAmount = Button(window, text="Convert", font="Helvetica 12 bold",
                                    bg="blue", fg="white", command=self.CovertedAmount).grid(row=4, column=2, sticky=E)
        btnDeleteAll = Button(window, text="Clear", font="Helvetica 12 bold",
                              bg="red", fg="white", command=self.DeleteAll).grid(row=4, column=6, padx=25, pady=25, sticky=E)

        window.mainloop()

    # Function to do the conversion. Stores inputs and performs conversion
    def CovertedAmount(self):
        amt = float(self.conversion_rate_var.get())
        convertedAmountVar = float(self.amount_to_convert_var.get()) * amt
        self.converted_amount_var.set(format(convertedAmountVar, '10.2f'))

    def DeleteAll(self):
        self.amount_to_convert_var.set("")
        self.conversion_rate_var.set("")
        self.converted_amount_var.set("")


Currency_Converter()
