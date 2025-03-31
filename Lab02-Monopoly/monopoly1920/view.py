import tkinter as tk
import os
from tkinter import ttk
import controller


def get_board_square_images():
    """return a List of all the file paths for the board square images"""
    square_images = []
    for i in range(40):
        path = os.path.join("resources", "images", "properties", f"{i}.png")
        square_images.append(path)
    return square_images

class View:
    """Class to create the GUI for the Monopoly game"""
    width = 1280
    height = 720

    def __init__(self, root, controller):
        # Set-up a simple window
        self.images = []
        root.title("Monopoly 1920")

        #tight coupling with the controller
        #not ideal, but we will refactor later
        self.controller = controller

        root.geometry(f'{self.width}x{self.height}')
        root.resizable(False, False)

        self.main_frame = ttk.Frame(root, padding=10, relief='groove')

        #create the frames
        logo_frame = self._create_logo_frame()
        middle_frame = self._create_middle_frame()
        msg_frame = self._create_msg_frame()

        #pack the frames
        logo_frame.pack(fill=tk.BOTH, expand=True)
        middle_frame.pack(fill=tk.BOTH, expand=False)
        msg_frame.pack(fill=tk.BOTH, expand=True)

        self.main_frame.pack(fill=tk.BOTH, expand=True)

        #self.setup_game()

    def _create_middle_frame(self):
        """Create the middle frame of the GUI"""
        middle_frame = ttk.Frame(self.main_frame, padding=10)
        board_image = tk.PhotoImage(file=r"resources/images/monopoly.png")
        board = ttk.Label(middle_frame, image=board_image)
        board.pack(side='left', anchor='n', padx=75)
        board.image = board_image

        # preload all the images for the board squares
        self._preload_images()

        card_image = self.images[0]
        self.card = ttk.Label(middle_frame, image=card_image)

        button_frame = ttk.Frame(middle_frame, padding=10)

        #create buttons
        self.roll_button = ttk.Button(button_frame, text="Roll Dice", command=lambda: self._action_taken("roll") )
        self.roll_button.pack(side='top', anchor='center', pady=(10, 10))

        self.purchase_button = ttk.Button(button_frame, text="Purchase", command=lambda: self._action_taken("purchase"))
        self.purchase_button.pack(side='top', anchor='center', pady=(10, 10))
        self.purchase_button.state(['disabled'])

        self.bankrupt_button = ttk.Button(button_frame, text="Go Bankrupt", command=lambda: self._action_taken("bankrupt"))
        self.bankrupt_button.pack(side='top', anchor='center', pady=(10, 10))
        self.bankrupt_button.state(['disabled'])
        self.end_turn_button = ttk.Button(button_frame, text="End Turn", command=lambda: self._action_taken("end_turn"))
        self.end_turn_button.pack(side='top', anchor='center', pady=(10, 10))
        self.end_turn_button.state(['disabled'])

        button_frame.pack(side='left', anchor='center', pady=(0, 0), padx=50)

        self.card.pack(side='left', anchor='n', padx=100, pady=(100, 0))
        self.card.image = card_image

        return middle_frame

    def _create_msg_frame(self):
        """Create the frame at the bottom of the screen to display messages"""
        msg_frame = ttk.Frame(self.main_frame, padding=10, relief='raised', borderwidth=3)

        self.state_box = tk.Text(msg_frame, width=60, height=10, background='black', foreground='white')
        self.state_box.pack(side='left', padx=(150,0))
        self.state_box.insert(tk.END, "All Players at Go!\n")
        self.state_box.insert(tk.END, "Player 1's Turn")

        self.text_box = tk.Text(msg_frame, width=60, height=10, background='black', foreground='white')
        self.text_box.pack(side='left', padx=200)
        self.text_box.insert(tk.END, "Roll the dice!")

        return msg_frame

    def _create_logo_frame(self):
        """Create the frame at the top of the screen to display the logo"""
        logo_frame = ttk.Frame(self.main_frame, padding=10)
        # load a logo resource
        logo_image = tk.PhotoImage(file=r"resources/images/monopoly_logo.png")
        logo = ttk.Label(logo_frame, image=logo_image)
        logo.pack(side='top', anchor='n')
        logo.image = logo_image

        return logo_frame

    def _action_taken(self, action):
        #disable the roll button
        #self.roll_button['state'] = 'disabled'
        #self.text_box.delete(1.0, tk.END)

        #tell the controller roll was clicked
        self._disable_all()

        #tight coupling means we need to pass the action to the controller
        updates = self.controller.button_clicked(action)

    def update_state(self, state, text):
        """Function to update the state of the game"""
        if state == "roll":
            self._await_roll()
        elif state == "purchase":
            self._await_purchase()
        elif state == "moves":
            self._await_moves()
        elif state == "moves_or_bankrupt":
            self._await_moves_or_bankrupt()
        elif state == "disable_all":
            self._disable_all()

        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, text)

    def _disable_all(self):
        self.roll_button['state'] = 'disabled'
        self.purchase_button['state'] = 'disabled'
        self.end_turn_button['state'] = 'disabled'
        self.bankrupt_button['state'] = 'disabled'

    def _await_roll(self):
        self.roll_button['state'] = 'active'

    def _await_purchase(self):
        self.purchase_button['state'] = 'active'

    def _await_moves(self):
        self.end_turn_button['state'] = 'active'

    def _await_moves_or_bankrupt(self):
        self.end_turn_button['state'] = 'active'
        self.bankrupt_button['state'] = 'active'

    def update_state_box(self, text=""):
        self.state_box.delete(1.0, tk.END)
        self.state_box.insert(tk.END, text)

    def _preload_images(self):
        '''Function to preload all the images for the board squares'''
        square_images = get_board_square_images()
        for image in square_images:
            img = tk.PhotoImage(file=image)
            self.images.append(img)

'''launch the GUI'''
if __name__ == '__main__':

    free_parking_payout = 0
    players_in_jail_collect = True
    property_auctions = False
    root = tk.Tk()

    controller = controller.Controller(root)

    root.mainloop()

