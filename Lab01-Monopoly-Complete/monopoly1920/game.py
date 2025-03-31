import tkinter as tk
from tkinter import ttk
import random
import os


#TODO Task 6: Fix the bug

#TODO: TASK 3 - Implement the load_game_board function
def load_game_board():
    '''Function to load and return the game board from a file
        @:return game_board: an ordered list of the game board spaces
                             where the 0th index is "GO" and the indices
                             proceed clockwise around the board
    '''
    game_board = []
    csv_path = os.path.join("resources", "data", "board.csv")
    f = open(csv_path, "r")
    next(f)  # skip the header row of the file, we don't need it for this game
    for line in f:
        line = line.strip()
        line = line.split(",")
        game_board.append(line[0])
    f.close()

    return game_board


#TODO: Task 4 - Implement the get_board_space_name function
def get_board_space_name(game_board, index):
    """Function to return the name of the board space at the given index
        @:param game_board: an ordered list of the game board spaces
        @:param index: the index of the space on the board
        @:return space_name: the name of the space at the given index
    """
    space_name = game_board[index]
    return space_name


#TODO Task 5 - Implement the get_board_square_images function
def get_board_square_images():
    """return a List of all the file paths for the board square images
    don't forget to use os.path.join to create the file path"""
    square_images = []
    for i in range(40):
        path = os.path.join("resources", "images", "properties", f"{i}.png")
        square_images.append(path)
    return square_images


#TODO: Task 2. Implement the roll_dice function
def roll_dice():
    """Function to simulate the rolling of two dice
        @:return dice_sum: the sum of the two dice
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    return dice_sum


class View():
    '''Class to create the GUI for the Monopoly game'''

    board_size = 40
    width = 1280
    height = 720

    def __init__(self, root):
        """ Set-up a simple window
            where we will play the game """
        self.images = []
        root.title("Monopoly 1920")
        self.player_position = 0

        root.geometry(f'{self.width}x{self.height}')
        root.resizable(False, False)

        self.main_frame = ttk.Frame(root, padding=10, relief='groove')

        logo_frame = self.create_logo_frame()
        middle_frame = self.create_middle_frame()
        msg_frame = self.create_msg_frame()

        # pack the frames
        logo_frame.pack(fill=tk.BOTH, expand=True)
        middle_frame.pack(fill=tk.BOTH, expand=False)
        msg_frame.pack(fill=tk.BOTH, expand=True)

        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def create_logo_frame(self):
        """create the logo frame for the GUI"""
        logo_path = os.path.join("resources", "images", "monopoly_logo.png")

        logo_frame = ttk.Frame(self.main_frame, padding=10)
        # load a logo resource
        logo_image = tk.PhotoImage(file=logo_path)
        logo = ttk.Label(logo_frame, image=logo_image)
        logo.pack(side='top', anchor='n')
        logo.image = logo_image

        return logo_frame

    def create_msg_frame(self):
        """create the message frame for the GUI"""
        msg_frame = ttk.Frame(self.main_frame, padding=10, relief='raised', borderwidth=3)

        # a few labels to display the game rules
        ttk.Label(msg_frame, text=f'Free Parking Payout: {free_parking_payout}').pack(side='left', anchor='n',
                                                                                      pady=(50, 0), padx=5)
        ttk.Label(msg_frame, text=f'Players in Jail Collect: {players_in_jail_collect}').pack(side='left', anchor='n',
                                                                                              pady=(50, 0), padx=5)
        ttk.Label(msg_frame, text=f'Property Auctions: {property_auctions}').pack(side='left', anchor='n', pady=(50, 0),
                                                                                  padx=5)

        self.text_box = tk.Text(msg_frame, width=60, height=10, background='black', foreground='white')
        self.text_box.pack(side='left', padx=200)
        self.text_box.insert(tk.END, "Roll the dice!")

        return msg_frame

    def create_middle_frame(self):
        """Function to create the middle frame of the GUI"""

        # setup some image paths
        board_path = os.path.join("resources", "images", "monopoly.png")
        card_path = os.path.join("resources", "images", "properties", "0.png")

        middle_frame = ttk.Frame(self.main_frame, padding=10)

        board_image = tk.PhotoImage(file=board_path)
        board = ttk.Label(middle_frame, image=board_image)
        board.pack(side='left', anchor='n', padx=75)
        board.image = board_image

        # preload all the images for the board squares
        self.preload_images()

        card_image = tk.PhotoImage(file=card_path)
        self.card = ttk.Label(middle_frame, image=card_image)

        button_frame = ttk.Frame(middle_frame, padding=10)

        self.roll_button = ttk.Button(button_frame, text="Roll Dice", command=self.update_gui)
        self.roll_button.pack(side='top', anchor='center', pady=(10, 10))

        button_frame.pack(side='left', anchor='center', pady=(0, 0), padx=50)

        self.card.pack(side='left', anchor='n', padx=100, pady=(100, 0))
        self.card.image = card_image

        return middle_frame

    def update_gui(self,):
        """Wrapper function to call the roll_dice function and then update the GUI"""
        self.roll_button['state'] = 'disabled'
        dice_sum = roll_dice()

        # update the player position
        self.player_position += dice_sum

        #TASK 6 FIX The bug with the mod operator
        self.player_position %= self.board_size

        square = get_board_space_name(game_board, self.player_position)

        try:
            self.card['image'] = self.images[self.player_position]
        except:
            pass
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, f"You rolled a {dice_sum}")
        self.text_box.insert(tk.END, chars=f"\nYou landed on {square}")
        self.roll_button['state'] = 'active'


    def preload_images(self):
        """Function to preload all the images for the board squares"""
        square_images = get_board_square_images()
        for image in square_images:
            img = tk.PhotoImage(file=image)
            self.images.append(img)


'''launch the GUI'''
if __name__ == '__main__':

    #TODO: Task 1. Set some values below to complete Task 1
    free_parking_payout = 0
    players_in_jail_collect = True
    property_auctions = False
    root = tk.Tk()
    v = View(root)

    game_board = load_game_board()

    root.mainloop()

