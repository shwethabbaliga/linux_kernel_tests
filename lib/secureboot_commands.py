from lib_main import main_class

class SB_basic_commands(main_class):
    def __init__(self):
        self.run_command("mokutil --sb")
        return 
        print ("secureboot is enabled or not")