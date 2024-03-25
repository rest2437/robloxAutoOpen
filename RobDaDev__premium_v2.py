import customtkinter as ctk
from PIL import Image
import os
import autoit
import time
import pywinauto
import threading
import pyautogui
import subprocess
from licensing.models import *
from licensing.methods import Key, Helpers
import saved_data
import random


# real time data (no storage)
startAFK = bool
stopAFK = bool
start = bool
stop = bool
hcOnOrOff = int
robloxApp = pywinauto.Application(backend='uia')
icon = r"C:\Users\noctu\OneDrive\Desktop\pythonCompletedexeFiles\InProgress\RobDaDev_premium_v.2.0.0\favicon.ico"


# saved data from user (storage)
# mouse_entry_1_x = 0
# mouse_entry_1_y = 0 
# mouse_entry_2_x = 0 
# mouse_entry_2_y = 0 
# mouse_click_1_speed = int
# mouse_click_2_speed = int
# check_process_speed = int
# total_time_to_check = int
# executor_inject_speed = int
# profile_name = 'RobDaDev'
# rb_open_method = 1
# mouse_amount_var = 1
# product_key = str

class MyImage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        IMAGE_WIDTH = 240
        IMAGE_HEIGHT = 240
        IMAGE_PATH = r'C:\Users\noctu\OneDrive\Desktop\pythonCompletedexeFiles\InProgress\RobDaDev_premium_v.2.0.0\profile.psd'
        logo = ctk.CTkImage(light_image=Image.open(
            os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH, IMAGE_HEIGHT))
        label = ctk.CTkLabel(self, image=logo, text='')
        label.grid(pady=5, padx=10, column=0, row=0, sticky="nsew")
        dcinfo = ctk.CTkLabel(self, text=saved_data.profile_name,
                              font=ctk.CTkFont(size=20, weight='bold'))
        dcinfo.grid(pady=(5,10), padx=0, column=0, row=1, sticky="nsew")

class ProjectTitleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # title label
        self.label2 = ctk.CTkLabel(
            self, text="Roblox Auto Launch", font=ctk.CTkFont(size=20, weight='bold'))
        self.label2.pack(padx=10, pady=(20, 1))
        # version
        self.label3 = ctk.CTkLabel(
            self, text="Version 2.0.0 - Premium", text_color="#545f63", font=ctk.CTkFont(size=15, weight='bold'))
        self.label3.pack(pady=(1, 20))

class SettingsFrame(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('520x400')
        self.iconbitmap(icon)
        self.title("Settings")

        self.settings_frame = ctk.CTkScrollableFrame(self,width = 600, height=400)
        self.settings_frame.pack(ipadx = 30)
                
        # Roblox directory selection
        self.roblox_entry = ctk.CTkFrame(self.settings_frame)
        self.roblox_entry.pack(ipadx = 5, ipady = 5)
        self.roblox_entry.grid_columnconfigure(0, minsize=150)
        self.roblox_entry.grid_columnconfigure(1, minsize=150)
        self.roblox_file_label = ctk.CTkLabel(self.roblox_entry, text='For more advanced settings, please locate saved_data.py', font=ctk.CTkFont(size=12, weight='bold'))
        self.roblox_file_label.grid(column=0, row=0, padx=30, columnspan=2,
                         pady=(10, 0))

        self.roblox_file_label = ctk.CTkLabel(self.roblox_entry, text='Roblox opening method', font=ctk.CTkFont(size=15, weight='bold'))
        self.roblox_file_label.grid(column=0, row=1, padx=30, columnspan=2,
                         pady=(10, 0))
        self.rb_open_method_var = ctk.IntVar(value=1)
        self.rb_open_method_1_button = ctk.CTkRadioButton(self.roblox_entry, text="Method 1 (Default)",
                                                    command=self.rbSwitchValue, variable= self.rb_open_method_var, value=1)
        self.rb_open_method_2_button = ctk.CTkRadioButton(self.roblox_entry, text="Method 2",
                                                    command=self.rbSwitchValue, variable= self.rb_open_method_var, value=2)
        self.rb_open_method_1_button.grid(row=2, column=0)
        self.rb_open_method_2_button.grid(row=2, column=1)

        # Mouse point amount selection
        # self.mouse_amount = ctk.CTkFrame(self.settings_frame)
        # self.mouse_amount.pack(ipadx = 5, ipady = 5)
        # self.mouse_amount.grid_columnconfigure(0, minsize=150)
        # self.mouse_amount.grid_columnconfigure(1, minsize=150)
        # self.mouse_amount_label = ctk.CTkLabel(self.mouse_amount, text='How many mouse points?', font=ctk.CTkFont(size=15, weight='bold'))
        # self.mouse_amount_label.grid(column=0, row=0, padx=30, columnspan=2,
        #                  pady=(10, 0))
        # self.mouse_amount_var = ctk.IntVar(value=1)
        # self.mouse_amount_1_button = ctk.CTkRadioButton(self.mouse_amount, text="1 (Default)",
        #                                             command=self.mouseAmountSwitchValue, variable= self.mouse_amount_var, value=1)
        # self.mouse_amount_2_button = ctk.CTkRadioButton(self.mouse_amount, text="2",
        #                                             command=self.mouseAmountSwitchValue, variable= self.mouse_amount_var, value=2)
        # self.mouse_amount_1_button.grid(row=1, column=0)
        # self.mouse_amount_2_button.grid(row=1, column=1)

    # def mouseAmountSwitchValue(self):
    #     global mouse_amount_var
    #     mouse_amount_var = self.mouse_amount_var.get()
    #     if self.rb_open_method_var.get() == 1:
    #         print('Method 1 selected')
    #     elif self.rb_open_method_var.get() == 2:
    #         print('Method 2 selected')

        # SECTION 2 TITLE
        self.label3 = ctk.CTkLabel(
            self.settings_frame, text='Mouse Points', font=ctk.CTkFont(size=15, weight='bold'))
        self.label3.pack(pady=(20,0))

        # Placeholder Variables
        self.placeholderText_x1 = "X"
        self.placeholderText_x2 = "X"
        self.placeholderText_y1 = "Y"
        self.placeholderText_y2 = "Y"

        # entry 1
        self.entry_1_frame = ctk.CTkFrame(self.settings_frame)
        self.entry_1_frame.pack(ipadx = 5, ipady = 5)
        self.entry_1_frame.grid_columnconfigure(0, minsize=125)
        self.entry_1_frame.grid_columnconfigure(1, minsize=125)
        self.entry_1_frame.grid_columnconfigure(2, minsize=125)
        self.entry_1_frame.grid_columnconfigure(4, minsize=125)
        self.label1 = ctk.CTkLabel(
            self.entry_1_frame, text='Mouse point 1 - PSX game', font=ctk.CTkFont(size=12))
        self.label1.grid(column=0, row=1, padx=30, columnspan=4,
                         pady=(0, 0))
        self.entry1_x = ctk.CTkEntry(
            self.entry_1_frame, width=100, height=20, placeholder_text=self.placeholderText_x1)
        self.entry1_x.grid(column=0, row=2, padx=5,
                           pady=(0, 10))
        self.entry1_y = ctk.CTkEntry(
            self.entry_1_frame, width=100, height=20, placeholder_text=self.placeholderText_y1)
        self.entry1_y.grid(column=1, row=2, padx=5,
                           pady=(0, 10))
        self.start_mouse_location_1 = ctk.CTkButton(
            self.entry_1_frame, width=100, height=20, text='Start', command=self.startMouseLocation1)
        self.start_mouse_location_1.grid(
            column=2, row=2, padx=5, pady=(0, 10))
        self.save_mouse_location_1 = ctk.CTkButton(
            self.entry_1_frame, width=100, height=20, text='Save', command=lambda: [self.mouseEntry1_x(), self.mouseEntry1_y()])
        self.save_mouse_location_1.grid(
            column=3, row=2, padx=5, pady=(0, 10))

        # entry 2
        self.entry_2_frame = ctk.CTkFrame(self.settings_frame)
        self.entry_2_frame.pack(ipadx = 5, ipady = 5)
        self.entry_2_frame.grid_columnconfigure(0, minsize=125)
        self.entry_2_frame.grid_columnconfigure(1, minsize=125)
        self.entry_2_frame.grid_columnconfigure(2, minsize=125)
        self.entry_2_frame.grid_columnconfigure(4, minsize=125)
        self.label2 = ctk.CTkLabel(
            self.entry_2_frame, text='(Optional) Mouse point 2 - Play button after clicking PSX game', font=ctk.CTkFont(size=12))
        self.label2.grid(column=0, row=3, padx=30,columnspan=4, pady=(10, 0))
        self.entry2_x = ctk.CTkEntry(
            self.entry_2_frame, width=100, height=20, placeholder_text=self.placeholderText_x2)
        self.entry2_x.grid(column=0, row=4, padx=5,
                           pady=(0, 10))
        self.entry2_y = ctk.CTkEntry(
            self.entry_2_frame, width=100, height=20, placeholder_text=self.placeholderText_y2)
        self.entry2_y.grid(column=1, row=4, padx=5,
                           pady=(0, 10))
        self.start_mouse_location_2 = ctk.CTkButton(
            self.entry_2_frame, width=100, height=20, text='Start', command=self.startMouseLocation2)
        self.start_mouse_location_2.grid(
            column=2, row=4, padx=5, pady=(0, 10))
        self.save_mouse_location_2 = ctk.CTkButton(
            self.entry_2_frame, width=100, height=20, text='Save', command=lambda: [self.mouseEntry2_x(), self.mouseEntry2_y()])
        self.save_mouse_location_2.grid(
            column=3, row=4, padx=5, pady=(0, 10))

        # # entry 3
        # self.entry_3_frame = ctk.CTkFrame(self.settings_frame)
        # self.entry_3_frame.pack(ipadx = 5, ipady = 5)
        # self.entry_3_frame.grid_columnconfigure(0, minsize=125)
        # self.entry_3_frame.grid_columnconfigure(1, minsize=125)
        # self.entry_3_frame.grid_columnconfigure(2, minsize=125)
        # self.entry_3_frame.grid_columnconfigure(4, minsize=125)
        # self.label3 = ctk.CTkLabel(
        #     self.entry_3_frame, text='Mouse point 3 - Close window button', font=ctk.CTkFont(size=12))
        # self.label3.grid(column=0, row=3, padx=30,columnspan=4, pady=(10, 0))
        # self.entry3_x = ctk.CTkEntry(
        #     self.entry_3_frame, width=100, height=20, placeholder_text='X')
        # self.entry3_x.grid(column=0, row=4, padx=5,
        #                    pady=(0, 10))
        # self.entry3_y = ctk.CTkEntry(
        #     self.entry_3_frame, width=100, height=20, placeholder_text='Y')
        # self.entry3_y.grid(column=1, row=4, padx=5,
        #                    pady=(0, 10))
        # self.start_mouse_location_3 = ctk.CTkButton(
        #     self.entry_3_frame, width=100, height=20, text='Start', command=self.startMouseLocation3)
        # self.start_mouse_location_3.grid(
        #     column=2, row=4, padx=5, pady=(0, 10))
        # self.save_mouse_location_3 = ctk.CTkButton(
        #     self.entry_3_frame, width=100, height=20, text='Save', command=lambda: [self.mouseEntry3_x(), self.mouseEntry3_y()])
        # self.save_mouse_location_3.grid(
        #     column=3, row=4, padx=5, pady=(0, 10))

    def rbSwitchValue(self):
        global rb_open_method
        rb_open_method = self.rb_open_method_var.get()
        if self.rb_open_method_var.get() == 1:
            print('Method 1 selected')
        elif self.rb_open_method_var.get() == 2:
            print('Method 2 selected')

    # Handling mouse input variables
    # input 1
    def mouseEntry1_x(self):
        print('Mouse location 1 saved')
        # global mouse_entry_1_x
        values=pyautogui.position()
        x = values.x
        saved_data.mouse_entry_1_x = x
        # print(type(mouse_entry_1_x))
        # print(mouse_entry_1_x)

    def mouseEntry1_y(self):
        values=pyautogui.position()
        y = values.y
        saved_data.mouse_entry_1_y = y
        # print(mouse_entry_1_y)

    def startMouseLocation1(self):
        # currently set to 5 seconds...change to however many seconds you need to position the mouse.
        time.sleep(5)
        values=pyautogui.position()
        x = values.x
        y = values.y
        self.entry1_x.configure(placeholder_text = x)
        self.entry1_y.configure(placeholder_text = y)

        print('Mouse location 1', values)
        
    


    #  input 2
    def mouseEntry2_x(self):
        print('Mouse location 2 saved')
        values=pyautogui.position()
        x = values.x
        saved_data.mouse_entry_2_x = x

    def mouseEntry2_y(self):
        values=pyautogui.position()
        y = values.y
        saved_data.mouse_entry_2_y = y

    def startMouseLocation2(self):
        # currently set to 5 seconds...change to however many seconds you need to position the mouse.
        time.sleep(5)
        values=pyautogui.position()
        x = values.x
        y = values.y
        self.entry2_x.configure(placeholder_text = x)
        self.entry2_y.configure(placeholder_text = y)

    #  input 3

    def mouseEntry3_x(self):
        print('Mouse location 1 saved')
        global mouse_entry_3_x
        mouse_entry_3_x = int(self.entry3_x.get())
        # print(type(mouse_entry_1_x))
        # print(mouse_entry_3_x)

    def mouseEntry3_y(self):
        global mouse_entry_3_y
        mouse_entry_3_y = int(self.entry3_y.get())
        # print(type(mouse_entry_3_y))
        # print(mouse_entry_3_y)

    def startMouseLocation3(self):
        # currently set to 5 seconds...change to however many seconds you need to position the mouse.
        time.sleep(5)
        pyautogui.position()
        print('Mouse location 3', pyautogui.position())

class StartProgramButtonFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Start button
        self.start_button = ctk.CTkButton(
            self, text="Start Auto Launch", width=200, command=self.start_main)  # enter command
        self.start_button.pack(padx=10, pady=(20, 0))
        # AFK button
        self.afk_button = ctk.CTkButton(
            self, text="Start Anti AFK", width=200, command=self.start_AFK, fg_color="#1F6AA5", hover_color='#144870')  # enter command
        self.afk_button.pack(pady=(10, 0))
        # Stop button
        # self.stop_button = ctk.CTkButton(
        #     self, text="Stop Auto Launch or Anti AFK", width=200, command=self.stop_all)  # enter command
        # self.stop_button.pack(pady=(10, 0))
        #settings menu
        self.stop_button = ctk.CTkButton(
            self, text="Settings Menu", width=200, command=self.open_settings_menu)  # enter command
        self.stop_button.pack(pady=(10, 0))
        self.settings_window = None
        # Open Roblox
        self.stop_button = ctk.CTkButton(
            self, text="Open Roblox", width=200, command=self.open_roblox)  # enter command
        self.stop_button.pack(pady=(10, 0))
        self.settings_window = None

        # kill game
        self.stop_button = ctk.CTkButton(
            self, text="Kill Roblox", width=200, command=self.end_game)  # enter command
        self.stop_button.pack(pady=(10, 0))
        self.settings_window = None

        # Console updates

        self.consoleUpdates = ctk.CTkLabel(self, text="console updates",
                              font=ctk.CTkFont(size=12))
        self.consoleUpdates.pack(pady=(10, 20))

        # # hardcore switch
        # self.hcswitch_var = ctk.IntVar(value=0)
        # self.hardcore_switch = ctk.CTkSwitch(
        #     self, text='Hardcore mode', command=self.hcSwitchValue, variable=self.hcswitch_var, onvalue=1, offvalue=0)
        # self.hardcore_switch.pack(pady=(10, 20))

    # settings menu
    def open_settings_menu(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
              self.settings_window = SettingsFrame(self)
        else:
             self.settings_window.focus()

    # Mouse entry string to int conversions
    # def hcSwitchValue(self):
    #     global hcOnOrOff
    #     hcOnOrOff = self.hcswitch_var.get()
    #     if self.hcswitch_var.get() == 1:
    #         print('HC mode enabled')
    #     elif self.hcswitch_var.get() == 0:
    #         print('HC mode is diabled')

    # def hardCore(self):
    #     global hcOnOrOff
    #     # wait 15 seconds for game to load
    #     if hcOnOrOff == 1:
    #         time.sleep(saved_data.hc_sleep_time)
    #         print('HC teleport in progress')
    #         autoit.send("{LSHIFT}")
    #         time.sleep(1)
    #         # click tp button
    #         autoit.mouse_click("left", saved_data.hc_mouse_click_1_x, saved_data.hc_mouse_click_1_y)
    #         # scroll to diamondd mine
    #         time.sleep(1)
    #         autoit.mouse_click_drag(saved_data.hc_mouse_click_drag_1_x, saved_data.hc_mouse_click_drag_1_y, saved_data.hc_mouse_click_drag_2_x, saved_data.hc_mouse_click_drag_2_y, 'left')
    #         # click on hardcore game mode
    #         time.sleep(1)
    #         autoit.mouse_click("left", saved_data.hc_mouse_click_2_x, saved_data.hc_mouse_click_2_y)
    #         # click on hardcore
    #         time.sleep(1)
    #         autoit.mouse_click("left", saved_data.hc_mouse_click_3_x, saved_data.hc_mouse_click_3_y)

    def start_game(self):
        print('starting new game')
        self.consoleUpdates.configure(text = 'starting new game')

        if saved_data.mouse_entry_1_x == 0 or saved_data.mouse_entry_1_y == 0:
             self.consoleUpdates.configure(text = 'Please input mouse\npoints and press "save"')
             return print('Please input mouse points and press "save"')
             
        elif saved_data.mouse_entry_2_x == 0 or saved_data.mouse_entry_2_y == 0:
             self.consoleUpdates.configure(text = "Mouse Point 2 disabled\nOnly using mouse point 1")
             print("Mouse Point 2 disabled. Only using mouse point 1")
             return autoit.mouse_click("left", saved_data.mouse_entry_1_x, saved_data.mouse_entry_1_y)
        else:
            print('Executing mouse point 1')
            self.consoleUpdates.configure(text = 'Executing mouse point 1')
            autoit.mouse_click("left", saved_data.mouse_entry_1_x, saved_data.mouse_entry_1_y)
            time.sleep(saved_data.mouse_click_2_speed)
            print('Executing mouse point 2')
            self.consoleUpdates.configure(text = 'Executing mouse point 2')
            autoit.mouse_click("left", saved_data.mouse_entry_2_x, saved_data.mouse_entry_2_y)

    def end_game(self):
        self.consoleUpdates.configure(text = 'Ending game to\nprevent injection issues')
        print('ending game to prevent injection issues')
        # time.sleep(5)
        # global mouse_entry_3_x
        # global mouse_entry_3_y
        # autoit.mouse_click("left", mouse_entry_3_x, mouse_entry_3_y)
        subprocess.run('taskkill /im Windows10Universal.exe /F')

    def open_roblox(self):
        global robloxApp
        # global rb_open_method
        if saved_data.rb_open_method == 1:
            print('Opening roblox with method 1')
            self.consoleUpdates.configure(text = 'Opening roblox\nwith method 1')
            robloxApp.start('explorer.exe shell:appsFolder\ROBLOXCORPORATION.ROBLOX_55nm5eh3cm0pr!App').connect(title='Roblox', timeout=10)       
        elif saved_data.rb_open_method ==2:
            self.consoleUpdates.configure(text = 'Opening roblox\nwith method 2')
            print('Opening roblox with method 2')
            robloxApp.start(r'C:\Program Files\WindowsApps\ROBLOXCORPORATION.ROBLOX_2.578.564.0_x86__55nm5eh3cm0pr\Windows10Universal.exe',wait_for_idle=False).connect(title='Roblox', timeout=10)
           
    def run_main(self):
        global robloxApp
        if start == True and stop == False:
            robloxApp = pywinauto.Application(backend='uia')
            process_is_running = True
            try:
                robloxApp = pywinauto.Application().connect(title='Roblox')
            except pywinauto.findwindows.ElementNotFoundError:
                process_is_running = False
            if not process_is_running and (start == True and stop == False):
                if (start == False and stop == True):
                    self.consoleUpdates.configure(text = 'Program stopped')
                    return print('Program stopped')
                else:
                    self.consoleUpdates.configure(text = 'Checking for Roblox')
                    print('Checking for Roblox')
                    time.sleep(3)

                if (start == False and stop == True):
                            self.consoleUpdates.configure(text = 'Program stopped')
                            return print('Program stopped')
                else:
                    self.consoleUpdates.configure(text = 'Starting Roblox UWP')
                    print('Starting Roblox UWP')
                    self.open_roblox()
                    time.sleep(3)

                if (start == False and stop == True):
                            self.consoleUpdates.configure(text = 'Program stopped')
                            return print('Program stopped')
                else:
                    self.consoleUpdates.configure(text = 'Waiting for\nexecutor to inject')
                    print('Waiting for executor to inject')
                    time.sleep(saved_data.executor_inject_speed)
                if (start == False and stop == True):
                            self.consoleUpdates.configure(text = 'Program stopped')
                            return print('Program stopped')
                else:
                     self.start_game()

                if (start == False and stop == True):
                            self.consoleUpdates.configure(text = 'Program stopped')
                            return print('Program stopped')  
                else:  
                    self.hardCore()
                    time.sleep(6)
                if (start == False and stop == True):
                            self.consoleUpdates.configure(text = 'Program stopped')
                            return print('Program stopped')
                else:
                     self.run_main()

            elif process_is_running and (start == True and stop == False):
                    times_checked = 0
                    while times_checked <= saved_data.total_time_to_check:
                        robloxApp = pywinauto.Application(backend='uia')
                        process_is_running = True
                        try:
                            robloxApp = pywinauto.Application().connect(title='Roblox')
                        except pywinauto.findwindows.ElementNotFoundError:
                            process_is_running = False

                        if(start == False and stop == True):
                            self.consoleUpdates.configure(text = 'Program stopped')
                            return print('Program stopped')

                        elif (not process_is_running and times_checked <= saved_data.total_time_to_check):
                            self.consoleUpdates.configure(text = 'Crash detected.\nRestarting Roblox UWP')
                            print('Crash detected. Restarting Roblox UWP')
                            time.sleep(5)
                            return self.run_main()

                        elif (process_is_running and times_checked >= saved_data.total_time_to_check):
                            self.consoleUpdates.configure(text = ('Roblox UWP ran\nsuccessfully for\n',saved_data.total_time_to_check,' seconds but\nwe are restarting\nto prevent crashes'))
                            print('Roblox UWP ran successfully for ',saved_data.total_time_to_check,' seconds but we are restarting to prevent crashes')
                            self.consoleUpdates.configure(text = 'Closing Roblox UWP')
                            print('Closing Roblox UWP')
                            time.sleep(4)
                            self.end_game()
                            time.sleep(saved_data.restart_after_closing_speed)
                            return self.run_main()
                        

                        elif (process_is_running and times_checked <=saved_data.total_time_to_check ):
                            times_checked+=1
                            self.consoleUpdates.configure(text = ('Checking for errors.\nTimes checked:',times_checked,'/nout of', saved_data.total_time_to_check))
                            print('Checking for errors. Times checked:',times_checked, 'out of', saved_data.total_time_to_check)
                            self.consoleUpdates.configure(text = 'Checking again in\n5 seconds')
                            print('Checking again in 5 seconds') 
                            time.sleep(saved_data.check_process_speed)


                        
        elif (start == False and stop == True):
            print ('Program stopped') 

    def randomTimedHop(self):
        self.afkInt = random.randint(3000,10000)
        self.secondsConversion = self.afkInt / 1000
        self.consolePr = ('Hopped after', str(self.secondsConversion), 'seconds')

    def aFK(self):  
        self.randomTimedHop()
        self.consoleUpdates.configure(text = self.consolePr)
        print('Hopped after', self.secondsConversion, 'seconds')
        if startAFK == True and stopAFK == False:
            autoit.send("{space}") 
            autoit.send("{space}")
            # autoit.mouse_click("left", 2938, 366)
            app.after(self.afkInt, self.aFK)

        elif stopAFK == True and startAFK == False:
            self.consoleUpdates.configure(text = 'Program stopped')
            print('Program stopped')

    def start_AFK(self):
        global startAFK
        startAFK = True
        global stopAFK
        stopAFK = False
        self.start_afk_inbg()
        print('Anti AFK activated')
        self.consoleUpdates.configure(text = 'Anti AFK activated')
        self.consoleUpdates.configure(text = 'Anti AFK activated')
        self.afk_button.configure(text = "Stop Anti AFK", fg_color="Red",hover_color='darkred',command=self.stop_all)

    def stop_all(self):
        global startAFK
        startAFK = False
        global start
        start = False
        global stop
        stop = True
        global stopAFK
        stopAFK = True
        self.afk_button.configure(text = "Start Anti AFK", fg_color="#1F6AA5", hover_color='#144870',command=self.start_AFK)
        self.consoleUpdates.configure(text = 'Stopping Application...\nDo not close until\n"Program stopped" is displayed')
        print('Stopping Application... Please keep roblox open and')
        print('wait until "Program stopped" is displayed to close window')

    def start_main_inbg(self):
        threading.Thread(target=self.run_main).start()

    def start_afk_inbg(self):
        threading.Thread(target=self.aFK).start()

    def start_main(self):
        global start
        start = True
        global stop
        stop = False
        self.consoleUpdates.configure(text = 'Application starting...\nplease wait')
        print ('Application starting... please wait')
        app.after(5000, self.start_main_inbg)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("540x435")
        # self.minsize(590, 530)
        # self.maxsize(590, 530)
        self.resizable(False, False)
        self.iconbitmap(icon)
        self.title("RobDaDev's Roblox Auto Launch - v2.1.0")
        # authentication 
        # RSAPubKey = "<RSAKeyValue><Modulus>mJzQWvjcYseH6Lz8DdcyKmXAsIi7FgkJshcq1U0Jq6F2dTIwJS4ZZGRPdeusRmEATPlpCf8/qYXDu0/WGg6H5kGTngljfe5rl/cvvgyuVeknW9onyL3+JkgqDfwp9gv4ucmeom5d0UHiyaI+oipXn+dt08zCmkHnR5ResucbbIlqBdWT0aEFJzX6PqMCPYzaSLFAc3wwQjHTeyPuz9E5MVudTzWD++vT8zOU/+j7BupN/8tOAgE2TvShuWXLc9tvB1IHLr/5EZT7P6XjPqR1lCqne8vn2wgg2FDY+zVufruTpWQs8xJVjLD9U1KpPEWvUTPUsGXnhDPGlFT2x33rUQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
        # auth = "WyI1MTc1Njg0MSIsImZabWM3aGRkdm0ySWcrZ1ZxUm1qYis3Ny9ucDgySWVRYnp0K1d0cWUiXQ=="
        # result = Key.activate(token=auth,\
        #                             rsa_pub_key=RSAPubKey,\
        #                             product_id=20586, \
        #                             key=saved_data.product_key,\
        #                             machine_code=Helpers.GetMachineCode(v=2))
                    
        # if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        #     print("The license does not work: {0}".format(result[1]))
        #     print ("Attempting to use key:",saved_data.product_key)
        #     # an error occurred or the key is invalid or it cannot be activated
        #     # (eg. the limit of activated devices was achieved)
        #     self.key_entry_frame = ctk.CTkFrame(master=self, height=430, width=535)
        #     self.key_entry_frame.pack(pady=150, ipadx = 5, ipady = 5)
        #     self.key_entry_frame.grid_columnconfigure(0, minsize=400)
        #     self.key_entry_frame.grid_columnconfigure(1, minsize=80)
        #     self.app_key_entry_label = ctk.CTkLabel(self.key_entry_frame, text='Product key invalid. Please enter product key in saved_data.py', font=ctk.CTkFont(size=15, weight='bold'))
        #     self.app_key_entry_label.grid(column=0, row=0, padx=30, columnspan=4,
        #                                     pady=(10, 0))



        # else:
        #     # everything went fine if we are here!
        #     print("The license is valid!")
        #     license_key = result[0]
        #     print("License expires: " + str(license_key.expires))
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title_frame = ProjectTitleFrame(master=self)
        self.title_frame.grid(row=0, column=0, padx=10, pady=10,
                                        sticky="nsew", columnspan=1)
        self.my_image = MyImage(master=self)
        self.my_image.grid(row=1, column=0, padx=10,
                                        pady=(0,10), ipady=5, ipadx=5, sticky='w')
        self.button_housing = StartProgramButtonFrame(master=self)
        self.button_housing.grid(row=1, column=0, padx=10,
                                                pady=(0,10), ipady=43, ipadx=10, sticky='e')




app = App()
app.mainloop()
