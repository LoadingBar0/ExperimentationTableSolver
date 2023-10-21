import tkinter as tk
from pynput import mouse
from time import sleep
import pydirectinput
import screeninfo
from PIL import ImageGrab, Image
import os

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App Title")  # Set the window title
        self.root.geometry("800x600")  # Set the window size to 800x600 pixels

        # Create a frame with a white background
        self.frame = tk.Frame(self.root, bg="white", width=800, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.start_screen()

    def start_screen(self):
        self.destroy_wigets()

        # Create a header label with My App Tile text
        self.header_label = tk.Label(self.frame, text="My App Title", font=("Arial", 60), bg="white")
        self.header_label.pack(pady=10)  # Add some padding to separate the header from other content

        # Create a button widget labeled "Chronomatron"
        self.chronomatron_button = tk.Button(self.frame, text="Chronomatron", font=("Arial", 32), bg="white", command=lambda: self.chronomatron())
        self.chronomatron_button.pack(pady=10)

        # Create a button widget labeled "Ultrasequencer"
        self.ultrasequencer_button = tk.Button(self.frame, text="Ultrasequencer", font=("Arial", 32), bg="white", command=lambda: self.ultrasequencer())
        self.ultrasequencer_button.pack(pady=10)

        # Add menu bar labbeled "Experimental" with checkboxes for each experimental feature
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.experimental_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Experimental", menu=self.experimental_menu)

        self.screen_region_var = tk.BooleanVar()
        self.screen_region_var.set(False)
        self.experimental_menu.add_checkbutton(label="Screen Region", variable=self.screen_region_var, onvalue=True, offvalue=False)

        self.auto_detect_var = tk.BooleanVar()
        self.auto_detect_var.set(False)
        self.experimental_menu.add_checkbutton(label="Auto Detect", variable=self.auto_detect_var, onvalue=True, offvalue=False)

        if not os.path.isfile("file_memory.txt"):
            with open("file_memory.txt", "w+") as file:
                file.write("False\n0\n0\n0\n0\n0\n0\n")

        with open("file_memory.txt", "r") as file:
            lines = file.readlines()
            if len(lines):
                if lines[0].strip() == "True": self.screen_region_var.set(True)
                self.top_left_corner = int(lines[1].strip()), int(lines[2].strip())
                self.bottom_right_corner = int(lines[3].strip()), int(lines[4].strip())
                self.clock_pixel_location = int(lines[5].strip()), int(lines[6].strip())

        # Initialize the recording variable
        self.recording = False

        # Initialize the color_location list
        self.red_color_location = ()
        self.blue_color_location = ()
        self.lime_color_location = ()
        self.yellow_color_location = ()
        self.light_blue_color_location = ()
        self.pink_color_location = ()
        self.dark_green_color_location = ()
        self.cyan_color_location = ()
        self.orange_color_location = ()
        self.purple_color_location = ()
        self.red_pixel_location = ()
        self.blue_pixel_location = ()
        self.lime_pixel_location = ()
        self.yellow_pixel_location = ()
        self.light_blue_pixel_location = ()
        self.pink_pixel_location = ()
        self.dark_green_pixel_location = ()
        self.cyan_pixel_location = ()
        self.orange_pixel_location = ()
        self.purple_pixel_location = ()
        self.clock_pixel_location = [0, 0]

        # Initialize the screen size variables
        self.getscreensize()

        self.root.bind("<Escape>", lambda e: self.start_screen()) # This will be removed for the final version

    def getscreensize(self):
        """
        This function will return the size of the screen
        """
        self.screen_height, self.screen_width = screeninfo.get_monitors()[0].height, screeninfo.get_monitors()[0].width

    def get_pixel_color_sum(self, x, y):
        try:
            img = Image.open("screenshot.png")
            pixel = img.getpixel((x, y))
            rgb_sum = pixel[0] + pixel[1] + pixel[2]
            return rgb_sum
        except FileNotFoundError:
            return None


    def destroy_wigets(self):
        try:
            self.header_label.destroy()
        except:
            pass
        try:
            self.chronomatron_button.destroy()
        except:
            pass
        try:
            self.ultrasequencer_button.destroy()
        except:
            pass
        try:
            self.experiment_select_dropdown.destroy()
        except:
            pass
        try:    
            self.start_button.destroy()
        except:
            pass
        try:
            self.chronomatron_label.destroy()
        except:
            pass
        try:
            self.color_select_dropdown.destroy()
        except:
            pass
        try:
            self.select_location_button.destroy()
        except:
            pass
        try:
            self.chronomatron_instruction_label.destroy()
        except:
            pass
        try:
            self.order_label.destroy()
        except:
            pass
        try:
            self.start_solver_button.destroy()
        except:
            pass
        try:
            self.test_location_button.destroy()
        except:
            pass
        try:
            self.experimental_menu.destroy()
        except:
            pass
        try:
            self.menu_bar.destroy()
        except:
            pass
        try:
            self.clear_order_button.destroy()
        except:
            pass

    def chronomatron(self):
        self.destroy_wigets()

        # Create a label widget with Chronomatron text
        self.chronomatron_label = tk.Label(self.frame, text="Chronomatron", font=("Arial", 60), bg="white")
        self.chronomatron_label.pack(pady=10)

        # Create a dropdown widget labeled "experment_select"
        self.experiment_select = tk.StringVar()
        self.experiment_select.set("Select an experiment")
        self.experiment_select_dropdown = tk.OptionMenu(self.frame, self.experiment_select, "High", "Grand", "Supreme", "Transcendent", "Metaphysical")
        self.experiment_select_dropdown.config(font=("Arial", 32), bg="white", width=20)
        self.experiment_select_dropdown["menu"].config(font=("Arial", 32))
        self.experiment_select_dropdown.pack(pady=10)

        # Create a button widget labeled "Start"
        self.start_button = tk.Button(self.frame, text="Start", font=("Arial", 32), bg="white", command=lambda: self.start_experiment_solver(self.experiment_select.get()))
        self.start_button.pack(pady=10)

    def start_experiment_solver(self, experiment_level="High"):
        self.destroy_wigets()
        
        # Create a label widget with Chronomatron (High) Solver text
        self.chronomatron_label = tk.Label(self.frame, text="Chronomatron (" + experiment_level + ") solver", font=("Arial", 30), bg="white")
        self.chronomatron_label.pack(pady=10)

        if self.screen_region_var.get():
            with open("file_memory.txt", "r") as file:
                lines = file.readlines()
                if len(lines):
                    if lines[0].strip() != "True": lines[0] = "True\n"
                    self.determin_color_location(experiment_level)
            
            with open ("file_memory.txt", "w+") as file:
                file.writelines(lines)
            
            ## create a button widget labeled "select location"
            self.select_location_button = tk.Button(self.frame, text="Select location", font=("Arial", 20), bg="white", command=lambda: self.select_screen_region_popup(experiment_level))
            self.select_location_button.pack(pady=10)
        else:
            # create a label widget with text "select location of each color"
            self.chronomatron_instruction_label = tk.Label(self.frame, text="Select location of each color", font=("Arial", 20), bg="white")
            self.chronomatron_instruction_label.pack(pady=10)

            with open("file_memory.txt", "w+") as file:
                lines = file.readlines()
                if len(lines):
                    if lines[0].strip() != "False": lines[0] = "False\n"
                    file.writelines(lines)

            if experiment_level == "High":
                self.experiment_high()
            elif experiment_level == "Grand":
                self.experiment_grand()
            elif experiment_level == "Supreme":
                self.experiment_supreme()
            elif experiment_level == "Transcendent":
                self.experiment_transcendent()
            elif experiment_level == "Metaphysical":
                self.experiment_metaphysical()

            # create a button widget labeled "select location"
            self.select_location_button = tk.Button(self.frame, text="Select location", font=("Arial", 20), bg="white", command=lambda: self.start_recording(self.color_select.get()))
            self.select_location_button.pack(pady=10)

            # Create a buttpm widget called order with text "Test Location"
            self.test_location_button = tk.Button(self.frame, text="Test Location", font=("Arial", 20), bg="white", command=lambda: self.test_color_location(self.color_select.get()))
            self.test_location_button.pack(pady=10)

        # Create a label widget called order with text "Order: "
        self.order_label = tk.Label(self.frame, text="Current Order: ", font=("Arial", 20), bg="white")
        self. order_label.pack(pady=10)

        # Create a btton widget called input order with text "Start Solver"
        self.start_solver_button = tk.Button(self.frame, text="Start Solver", font=("Arial", 15), bg="white", command=lambda: self.start_solver_popup(experiment_level))
        self.start_solver_button.pack(pady=10)

        # Create a button widget called "Clear Order"
        self.clear_order_button = tk.Button(self.frame, text="Clear Order", font=("Arial", 15), bg="white", command=lambda: self.order_label.config(text="Current Order: "))
        self.clear_order_button.pack(pady=10)

    def MouseMoveTo(self, x, y):
        x = 1 + int(x * 65536./float(self.screen_width))
        y = 1 + int(y * 65536./float(self.screen_height))
        extra = pydirectinput.ctypes.c_ulong(0)
        ii_ = pydirectinput.Input_I()
        ii_.mi =  pydirectinput.MouseInput(x,y,0, (0x0001 | 0x8000), 0, pydirectinput.ctypes.pointer(extra) )
        x = pydirectinput.Input(pydirectinput.ctypes.c_ulong(0), ii_ )
        pydirectinput.SendInput(1, pydirectinput.ctypes.pointer(x), pydirectinput.ctypes.sizeof(x))

    def test_color_location(self, color=None):
        if color == None:
            return
        try:
            if color == "Red":
                x, y = self.red_color_location
            elif color == "Blue":
                x, y = self.blue_color_location
            elif color == "Lime":
                x, y = self.lime_color_location
            elif color == "Yellow":
                x, y = self.yellow_color_location
            elif color == "Light Blue":
                x, y = self.light_blue_color_location
            elif color == "Pink":
                x, y = self.pink_color_location
            elif color == "Dark Green":
                x, y = self.dark_green_color_location
            elif color == "Cyan":
                x, y = self.cyan_color_location
            elif color == "Orange":
                x, y = self.orange_color_location
            elif color == "Purple":
                x, y = self.purple_color_location
            else:
                print("Error: invalid color")
                return
        except ValueError:
            print('Error: ' + '"' + color + '"' + ' location not found')
            return
        self.MouseMoveTo(x, y)
    
    def experiment_high(self):
        # Create a dropdown widget labeled "color_select"
        self.color_select = tk.StringVar()
        self.color_select.set("Select a color")
        self.color_select_dropdown = tk.OptionMenu(self.frame, self.color_select, "Red", "Blue", "Lime")
        self.color_select_dropdown.config(font=("Arial", 20), bg="white", width=20)
        self.color_select_dropdown["menu"].config(font=("Arial", 20))
        self.color_select_dropdown.pack(pady=10)
    
    def experiment_grand(self):
        # Create a dropdown widget labeled "color_select"
        self.color_select = tk.StringVar()
        self.color_select.set("Select a color")
        self.color_select_dropdown = tk.OptionMenu(self.frame, self.color_select, "Red", "Blue", "Lime", "Yellow", "Light Blue")
        self.color_select_dropdown.config(font=("Arial", 20), bg="white", width=20)
        self.color_select_dropdown["menu"].config(font=("Arial", 20))
        self.color_select_dropdown.pack(pady=10)
        
    
    def experiment_supreme(self):
        # Create a dropdown widget labeled "color_select"
        self.color_select = tk.StringVar()
        self.color_select.set("Select a color")
        self.color_select_dropdown = tk.OptionMenu(self.frame, self.color_select, "Red", "Blue", "Lime", "Yellow", "Light Blue", "pink", "Dark Green")
        self.color_select_dropdown.config(font=("Arial", 20), bg="white", width=20)
        self.color_select_dropdown["menu"].config(font=("Arial", 20))
        self.color_select_dropdown.pack(pady=10)
        
    
    def experiment_transcendent(self):
        # Create a dropdown widget labeled "color_select"
        self.color_select = tk.StringVar()
        self.color_select.set("Select a color")
        self.color_select_dropdown = tk.OptionMenu(self.frame, self.color_select, "Red", "Blue", "Lime", "Yellow", "Light Blue", "Pink", "Dark Green", "Cyan")
        self.color_select_dropdown.config(font=("Arial", 20), bg="white", width=20)
        self.color_select_dropdown["menu"].config(font=("Arial", 20))
        self.color_select_dropdown.pack(pady=10)
        
    
    def experiment_metaphysical(self):
        # Create a dropdown widget labeled "color_select"
        self.color_select = tk.StringVar()
        self.color_select.set("Select a color")
        self.color_select_dropdown = tk.OptionMenu(self.frame, self.color_select, "Red", "Blue", "Lime", "Yellow", "Light Blue", "Pink", "Dark Green", "Cyan", "Orange", "Purple")
        self.color_select_dropdown.config(font=("Arial", 20), bg="white", width=20)
        self.color_select_dropdown["menu"].config(font=("Arial", 20))
        self.color_select_dropdown.pack(pady=10)

    def start_recording(self, color=None):
        if color == None:
            return
        self.recording = True
        self.mouse_listener = mouse.Listener(on_click=self.select_location)
        self.mouse_listener.start()

    def select_location(self, x, y, button, pressed):
        if self.recording and button == mouse.Button.left and pressed:
            self.update_color_location(self.color_select.get(), x, y)
            self.recording = False 

    def determin_color_location(self, experiment_level):
        if experiment_level == "High":
            x_distance_between_colors = (self.bottom_right_corner[0] - self.top_left_corner[0]) / 3
            y_distance_between_colors = (self.bottom_right_corner[1] - self.top_left_corner[1]) / 3
            experiment_level_number = 1
        elif experiment_level == "Grand":
            x_distance_between_colors = (self.bottom_right_corner[0] - self.top_left_corner[0]) / 5
            y_distance_between_colors = (self.bottom_right_corner[1] - self.top_left_corner[1]) / 3
            experiment_level_number = 2
        elif experiment_level == "Supreme":
            x_distance_between_colors = (self.bottom_right_corner[0] - self.top_left_corner[0]) / 7
            y_distance_between_colors = (self.bottom_right_corner[1] - self.top_left_corner[1]) / 3
            experiment_level_number = 3
        elif experiment_level == "Transcendent":
            x_distance_between_colors = (self.bottom_right_corner[0] - self.top_left_corner[0]) / 5
            y_distance_between_colors = (self.bottom_right_corner[1] - self.top_left_corner[1]) / 4
            experiment_level_number = 4
        elif experiment_level == "Metaphysical":
            x_distance_between_colors = (self.bottom_right_corner[0] - self.top_left_corner[0]) / 5
            y_distance_between_colors = (self.bottom_right_corner[1] - self.top_left_corner[1]) / 4
            experiment_level_number = 5
        else:
            print("Error: invalid experiment level")
            return
        
        if experiment_level_number >= 1:
            self.red_color_location = self.top_left_corner[0] + x_distance_between_colors / 2, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.red_pixel_location = x_distance_between_colors / 2, y_distance_between_colors * 1.5
            self.blue_color_location = self.top_left_corner[0] + x_distance_between_colors * 1.5, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.blue_pixel_location = x_distance_between_colors * 1.5, y_distance_between_colors * 1.5
            self.lime_color_location = self.top_left_corner[0] + x_distance_between_colors * 2.5, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.lime_pixel_location = x_distance_between_colors * 2.5, y_distance_between_colors * 1.5
        if experiment_level_number >= 2:
            self.yellow_color_location = self.top_left_corner[0] + x_distance_between_colors * 3.5, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.yellow_pixel_location = x_distance_between_colors * 3.5, y_distance_between_colors * 1.5
            self.light_blue_color_location = self.top_left_corner[0] + x_distance_between_colors * 4.5, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.light_blue_pixel_location = x_distance_between_colors * 4.5, y_distance_between_colors * 1.5
        if experiment_level_number >= 3:
            self.pink_color_location = self.top_left_corner[0] + x_distance_between_colors * 5.5, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.pink_pixel_location = x_distance_between_colors * 5.5, y_distance_between_colors * 1.5
            self.dark_green_color_location = self.top_left_corner[0] + x_distance_between_colors * 6.5, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.dark_green_pixel_location = x_distance_between_colors * 6.5, y_distance_between_colors * 1.5
        if experiment_level_number >= 4:
            self.light_blue_color_location = self.top_left_corner[0] + x_distance_between_colors * 1.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.light_blue_pixel_location = x_distance_between_colors * 1.5, y_distance_between_colors * 2.5
            self.pink_color_location = self.top_left_corner[0] + x_distance_between_colors * 2.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.pink_pixel_location = x_distance_between_colors * 2.5, y_distance_between_colors * 2.5
            self.dark_green_color_location = self.top_left_corner[0] + x_distance_between_colors * 3.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.dark_green_pixel_location = x_distance_between_colors * 3.5, y_distance_between_colors * 2.5
            self.cyan_color_location = self.top_left_corner[0] + x_distance_between_colors * 4.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.cyan_pixel_location = x_distance_between_colors * 4.5, y_distance_between_colors * 2.5
        if experiment_level_number >= 5:
            self.light_blue_color_location = self.top_left_corner[0] + x_distance_between_colors * 4.5, self.top_left_corner[1] + y_distance_between_colors * 1.5
            self.light_blue_pixel_location = x_distance_between_colors * 4.5, y_distance_between_colors * 1.5
            self.pink_color_location = self.top_left_corner[0] + x_distance_between_colors / 2, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.pink_pixel_location = x_distance_between_colors / 2, y_distance_between_colors * 2.5
            self.dark_green_color_location = self.top_left_corner[0] + x_distance_between_colors * 1.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.dark_green_pixel_location = x_distance_between_colors * 1.5, y_distance_between_colors * 2.5
            self.cyan_color_location = self.top_left_corner[0] + x_distance_between_colors * 2.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.cyan_pixel_location = x_distance_between_colors * 2.5, y_distance_between_colors * 2.5
            self.orange_color_location = self.top_left_corner[0] + x_distance_between_colors * 3.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.orange_pixel_location = x_distance_between_colors * 3.5, y_distance_between_colors * 2.5
            self.purple_color_location = self.top_left_corner[0] + x_distance_between_colors * 4.5, self.top_left_corner[1] + y_distance_between_colors * 2.5
            self.purple_pixel_location = x_distance_between_colors * 4.5, y_distance_between_colors * 2.5

        with open("file_memory.txt", "r") as file:
            lines = file.readlines()
            self.clock_pixel_location[0] = int(lines[5].strip())
            self.clock_pixel_location[1] = int(lines[6].strip()) 

    def update_color_location(self, color=None, x=None, y=None):
        if color == None or x == None or y == None:
            return
        if color == "Red":
            self.red_color_location = (x, y)
        elif color == "Blue":
            self.blue_color_location = (x, y)
        elif color == "Lime":
            self.lime_color_location = (x, y)
        elif color == "Yellow":
            self.yellow_color_location = (x, y)
        elif color == "Light Blue":
            self.light_blue_color_location = (x, y)
        elif color == "Pink":
            self.pink_color_location = (x, y)
        elif color == "Dark Green":
            self.dark_green_color_location = (x, y)
        elif color == "Cyan":
            self.cyan_color_location = (x, y)
        elif color == "Orange":
            self.orange_color_location = (x, y)
        elif color == "Purple":
            self.purple_color_location = (x, y)
        elif color == "Clock":
            self.clock_pixel_location = (x, y)
        else:
            print("Error: invalid color")
            return
        
    def update_corner_location(self, corner, x, y):
        if corner == "top left":
            self.top_left_corner = (x, y)
            with open("file_memory.txt", "r") as file:
                lines = file.readlines()
                lines[1] = str(x) + "\n"
                lines[2] = str(y) + "\n"
            with open("file_memory.txt", "w+") as file:
                file.writelines(lines)  
        elif corner == "bottom right":
            self.bottom_right_corner = (x, y)
            with open("file_memory.txt", "r") as file:
                lines = file.readlines()
                lines[3] = str(x) + "\n"
                lines[4] = str(y) + "\n"
            with open("file_memory.txt", "w+") as file:
                file.writelines(lines)  
        else:
            print("Error: invalid corner")
            return
                
    def select_location_screen(self, x, y, button, pressed):
        if self.recording and button == mouse.Button.left and pressed:
            self.update_corner_location(self.corner, x, y)
            self.recording = False

    def select_screen_region(self, corner=None):
        if corner == None:
            return
        self.corner = corner
        self.recording = True
        self.mouse_listener = mouse.Listener(on_click=self.select_location_screen)
        self.mouse_listener.start()
        
    def select_screen_region_popup(self, experiment_level="High"):
        '''
        This function will allow the user to select a region of the screen
        '''
        # Creates a popup window that tells you to click on the top left corner of the screen region
        select_screen_popup = tk.Toplevel(self.root)
        select_screen_popup.title("Select Screen Region")
        select_screen_popup.geometry("650x350")
        label = tk.Label(select_screen_popup, text="Click on the top left corner of the screen region", font=("Arial", 16))
        label.pack(pady=20)

        # Creates a button that will allow the user to select the top left corner of the screen region
        top_left_button = tk.Button(select_screen_popup, text="Top Left", font=("Arial", 15), bg="white", fg="black", command=lambda: self.select_screen_region("top left"))
        top_left_button.pack(pady=4)

        # Creates a button that tells you to click on the bottom right corner of the screen region
        bottom_right_button = tk.Button(select_screen_popup, text="Bottom Right", font=("Arial", 14), bg="white", fg="black", command=lambda: self.select_screen_region("bottom right"))
        bottom_right_button.pack(pady=10)

        # Creates a button that will allow you to confirm the screen region
        confirm_button = tk.Button(select_screen_popup, text="Confirm", font=("Arial", 14), bg="white", fg="green", command=lambda: self.determin_color_location(experiment_level))
        confirm_button.pack(pady=10)

        # Creates a button that will allow you to close the popup window
        close_button = tk.Button(select_screen_popup, text="Close", font=("Arial", 14), command=select_screen_popup.destroy)
        close_button.pack(pady=10)

        # Allows the user to close the popup window by pressing the escape key
        select_screen_popup.bind("<Escape>", lambda e: select_screen_popup.destroy())

    def start_solver_popup(self, experiment_level="High"):
        popup = tk.Toplevel(self.root)
        popup.title(experiment_level + " Experiment Solver")

        if self.auto_detect_var.get():
            popup.geometry("250x350")

            label = tk.Label(popup, text="Hit the start button (built in 1 sec delay)", font=("Arial", 16))
            label.pack(pady=20)

            clock_location_button = tk.Button(popup, text="Clock Location", font=("Arial", 15), bg="white", fg="black", command=lambda: self.update_clock_location())
            clock_location_button.pack(pady=4)

            start_button = tk.Button(popup, text="Start", font=("Arial", 15), bg="white", fg="black", command=lambda: self.run_auto_solver())
            start_button.pack(pady=4)
        else:

            if experiment_level == "High": # Set the size of the popup window based on the experiment level
                popup.geometry("250x350")  
            elif experiment_level == "Grand":
                popup.geometry("250x370")
            elif experiment_level == "Supreme":
                popup.geometry("250x460")
            elif experiment_level == "Transcendent":
                popup.geometry("250x520")
            elif experiment_level == "Metaphysical":
                popup.geometry("250x610")

            label = tk.Label(popup, text="Add Next Color", font=("Arial", 16))
            label.pack(pady=20)

            if experiment_level == "High":
                experiment_level_number = 1
            elif experiment_level == "Grand":
                experiment_level_number = 2
            elif experiment_level == "Supreme":
                experiment_level_number = 3
            elif experiment_level == "Transcendent":
                experiment_level_number = 4
            elif experiment_level == "Metaphysical":
                experiment_level_number = 5

            if experiment_level_number >= 1:
                red_button = tk.Button(popup, text="red", font=("Arial", 15), bg="white", fg="red", command=lambda: self.update_order_list("Red"))
                red_button.pack(pady=4)
                blue_button = tk.Button(popup, text="blue", font=("Arial", 15), bg="white", fg="blue", command=lambda: self.update_order_list("Blue"))
                blue_button.pack(pady=4)
                lime_button = tk.Button(popup, text="lime", font=("Arial", 15), bg="white", fg="lime", command=lambda: self.update_order_list("Lime"))
                lime_button.pack(pady=4)
            if experiment_level_number >= 2:
                yellow_button = tk.Button(popup, text="yellow", font=("Arial", 15), bg="white", fg="yellow", command=lambda: self.update_order_list("Yellow"))
                yellow_button.pack(pady=4)
                light_blue_button = tk.Button(popup, text="Light Blue", font=("Arial", 15), bg="white", fg="light blue", command=lambda: self.update_order_list("Light_Blue"))
                light_blue_button.pack(pady=4)
            if experiment_level_number >= 3:
                pink_button = tk.Button(popup, text="pink", font=("Arial", 15), bg="white", fg="pink", command=lambda: self.update_order_list("Pink"))
                pink_button.pack(pady=4)
                dark_green_button = tk.Button(popup, text="dark green", font=("Arial", 15), bg="white", fg="dark green", command=lambda: self.update_order_list("Dark_Green"))
                dark_green_button.pack(pady=4)
            if experiment_level_number >= 4:
                cyan_button = tk.Button(popup, text="cyan", font=("Arial", 15), bg="white", fg="cyan", command=lambda: self.update_order_list("Cyan"))
                cyan_button.pack(pady=4)
            if experiment_level_number >= 5:
                orange_button = tk.Button(popup, text="orange", font=("Arial", 15), bg="white", fg="orange", command=lambda: self.update_order_list("Orange"))
                orange_button.pack(pady=4)
                purple_button = tk.Button(popup, text="purple", font=("Arial", 15), bg="white", fg="purple", command=lambda: self.update_order_list("Purple"))
                purple_button.pack(pady=4)

        close_button = tk.Button(popup, text="Close", font=("Arial", 14), command=popup.destroy)
        close_button.pack(pady=10)

        popup.bind("<Escape>", lambda e: popup.destroy())
    
    def update_clock_location(self):
        self.recording = True
        self.mouse_listener = mouse.Listener(on_click=self.select_clock_location)
        self.mouse_listener.start()

    def select_clock_location(self, x, y, button, pressed):
        if self.recording and button == mouse.Button.left and pressed:
            self.update_color_location("Clock", x, y)
            self.recording = False
        with open("file_memory.txt", "r") as file:
            lines = file.readlines()
            lines[5] = str(x) + "\n"
            lines[6] = str(y) + "\n"
        with open("file_memory.txt", "w+") as file:
            file.writelines(lines)
    
    def run_solver(self, given_order=None):
        if given_order == None:
            order = self.order_label.cget("text")[15:]
            order = order.split(" ")[:-1]
        else:
            order = given_order

        for i in order:
            sleep(0.5)
            try:
                if i == "Red":
                    x, y = self.red_color_location
                elif i == "Blue":
                    x, y = self.blue_color_location
                elif i == "Lime":
                    x, y = self.lime_color_location
                elif i == "Yellow":
                    x, y = self.yellow_color_location
                elif i == "Light Blue":
                    x, y = self.light_blue_color_location
                elif i == "Pink":
                    x, y = self.pink_color_location
                elif i == "Dark Green":
                    x, y = self.dark_green_color_location
                elif i == "Cyan":
                    x, y = self.cyan_color_location
                elif i == "Orange":
                    x, y = self.orange_color_location
                elif i == "Purple":
                    x, y = self.purple_color_location
                else:
                    print("Error: invalid color")
            except ValueError:
                print('Error: color ' +'"' + i + '"' + ' has no location')
                return
            self.MouseMoveTo(x, y)
            pydirectinput.click()
            self.MouseMoveTo(100, 100)
        
    def run_auto_solver(self):
        for i in range(3):
            order = []
            while True:

                # Define the coordinates of the top left and bottom right corners of the section to capture
                left = self.top_left_corner[0]
                top = self.top_left_corner[1]
                right = self.bottom_right_corner[0]
                bottom = self.bottom_right_corner[1]

                # Capture the section of the screen and save it as "screenshot.png"
                ImageGrab.grab(bbox=(left, top, right, bottom)).save("screenshot.png")


                # uses red_pixel_location and checks hex value of pixel
                try:
                    if self.get_pixel_color_sum(self.red_pixel_location[0], self.red_pixel_location[1]) <= 120 :
                        order.append("Red")
                        sleep(0.5)
                except:
                    pass
                # checks blue_pixel_location
                try:
                    if self.get_pixel_color_sum(self.blue_pixel_location[0], self.blue_pixel_location[1]) <= 120:
                        order.append("Blue")
                        sleep(0.5)
                except:
                    pass
                # checks lime_pixel_location
                try:
                    if self.get_pixel_color_sum(self.lime_pixel_location[0], self.lime_pixel_location[1]) <= 120:
                        order.append("Lime")
                        sleep(0.5)
                except:
                    pass
                # checks yellow_pixel_location
                try:
                    if self.get_pixel_color_sum(self.yellow_pixel_location[0], self.yellow_pixel_location[1]) <= 120:
                        order.append("Yellow")
                        sleep(0.5)
                except:
                    pass
                # checks light_blue_pixel_location
                try:
                    if self.get_pixel_color_sum(self.light_blue_pixel_location[0], self.light_blue_pixel_location[1]) <= 120:
                        order.append("Light Blue")
                        sleep(0.5)
                except:
                    pass
                # checks pink_pixel_location
                try:
                    if self.get_pixel_color_sum(self.pink_pixel_location[0], self.pink_pixel_location[1]) <= 120:
                        order.append("Pink")
                        sleep(0.5)
                except:
                    pass
                # checks dark_green_pixel_location
                try:
                    if self.get_pixel_color_sum(self.dark_green_pixel_location[0], self.dark_green_pixel_location[1]) <= 120:
                        order.append("Dark Green")
                        sleep(0.5)
                except:
                    pass
                # checks cyan_pixel_location
                try:
                    if self.get_pixel_color_sum(self.cyan_pixel_location[0], self.cyan_pixel_location[1]) <= 120:
                        order.append("Cyan")
                        sleep(0.5)
                except:
                    pass
                # checks orange_pixel_location
                try:
                    if self.get_pixel_color_sum(self.orange_pixel_location[0], self.orange_pixel_location[1]) <= 120:
                        order.append("Orange")
                        sleep(0.5)
                except:
                    pass
                # checks purple_pixel_location
                try:
                    if self.get_pixel_color_sum(self.purple_pixel_location[0], self.purple_pixel_location[1]) <= 120:
                        order.append("Purple")
                except:
                    pass
                # if no color is found, then it waits 100 miliseconds and tries again

                if len(order) == i + 1:
                    break

            # Run solver after delay
            print(order)
            self.wait_till_clock()
            self.run_solver(order)
        print("Done")

    def wait_till_clock(self):
        while True:
            # Define the coordinates of the top left and bottom right corners of the section to capture
            left = self.clock_pixel_location[0] - 1
            top = self.clock_pixel_location[1] - 1
            right = self.clock_pixel_location[0] + 1
            bottom = self.clock_pixel_location[1] + 1

            # Capture the section of the screen and save it as "screenshot.png"
            ImageGrab.grab(bbox=(left, top, right, bottom)).save("screenshot.png")

            # uses clock_pixel_location and checks hex value of pixel
            if self.get_pixel_color_sum(1, 1) <= 120:
                break
            sleep(0.1)

    def update_order_list(self, color=None):
        if color == None:
            return
        self.order_label.config(text=self.order_label.cget("text") + color + " ")
        sleep(0.5)
        self.run_solver()

    def ultrasequencer(self):
        print("ultrasequencer currently does nothing :(")
        # self.destroy_wigets()


if __name__ == '__main__':
    root = tk.Tk()
    my_app = MyApp(root)
    root.mainloop()
