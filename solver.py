import tkinter as tk
from pynput import mouse
from time import sleep
import pydirectinput
import screeninfo

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

        # Initialize the recording variable
        self.recording = False

        # Initialize the color_location list
        self.red_color_location = ()
        self.blue_color_location = ()
        self.lime_color_location = ()

        # Initialize the screen size variables
        self.getscreensize()

        self.root.bind("<Escape>", lambda e: self.start_screen()) # This will be removed for the final version

    def getscreensize(self):
        """
        This function will return the size of the screen
        """
        self.screen_height, self.screen_width = screeninfo.get_monitors()[0].height, screeninfo.get_monitors()[0].width

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
        self.chronomatron_label = tk.Label(self.frame, text="Chronomatron (High) solver", font=("Arial", 30), bg="white")
        self.chronomatron_label.pack(pady=10)
        
        # create a label widget with text "select location of each color"
        self.chronomatron_instruction_label = tk.Label(self.frame, text="Select location of each color", font=("Arial", 20), bg="white")
        self.chronomatron_instruction_label.pack(pady=10)

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
        "Red", "Blue", "Lime", "Yellow", "Light Blue", "Pink", "Dark Green", "Cyan", "Orange", "Purple"
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
        print(x, y)
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
        self.color_select_dropdown = tk.OptionMenu(self.frame, self.color_select, "Red", "Blue", "Lime", "Yellow", "Cyan")
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
        else:
            print("Error: invalid color")
            return

    def start_solver_popup(self, experiment_level="High"):
        popup = tk.Toplevel(self.root)
        popup.title(experiment_level + " Experiment Solver")
        if experiment_level == "High": # Set the size of the popup window based on the experiment level (for now they are all the same size)
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
            light_blue_button = tk.Button(popup, text="cyan", font=("Arial", 15), bg="white", fg="light blue", command=lambda: self.update_order_list("Light Blue"))
            light_blue_button.pack(pady=4)
        if experiment_level_number >= 3:
            cyan_button = tk.Button(popup, text="light blue", font=("Arial", 15), bg="white", fg="cyan", command=lambda: self.update_order_list("Cyan"))
            cyan_button.pack(pady=4)
            pink_button = tk.Button(popup, text="pink", font=("Arial", 15), bg="white", fg="pink", command=lambda: self.update_order_list("Pink"))
            pink_button.pack(pady=4)
        if experiment_level_number >= 4:
            dark_green_button = tk.Button(popup, text="dark green", font=("Arial", 15), bg="white", fg="dark green", command=lambda: self.update_order_list("Dark Green"))
            dark_green_button.pack(pady=4)
        if experiment_level_number >= 5:
            orange_button = tk.Button(popup, text="orange", font=("Arial", 15), bg="white", fg="orange", command=lambda: self.update_order_list("Orange"))
            orange_button.pack(pady=4)
            purple_button = tk.Button(popup, text="purple", font=("Arial", 15), bg="white", fg="purple", command=lambda: self.update_order_list("Purple"))
            purple_button.pack(pady=4)

        close_button = tk.Button(popup, text="Close", font=("Arial", 14), command=popup.destroy)
        close_button.pack(pady=10)

        popup.bind("<Escape>", lambda e: popup.destroy())
    
    def run_solver(self):
        order = self.order_label.cget("text")[15:]
        order = order.split(" ")[:-1]
        for i in order:
            sleep(0.5)
            try:
                if i == "Red":
                    x, y = self.red_color_location
                elif i == "Blue":
                    x, y = self.blue_color_location
                elif i == "Lime":
                    x, y = self.lime_color_location
                else:
                    print("Error: invalid color")
            except ValueError:
                print('Error: color ' +'"' + i + '"' + ' has no location')
                return
            self.MouseMoveTo(x, y)
            pydirectinput.click()
        


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
