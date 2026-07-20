from lib_main import main_class
from common_commands import common_commands

class SB_basic_commands(common_commands):
    state = 0 
    
    def __init__(self):
        secureboot_state = self.run_command("mokutil --sb")

        if "enabled" in secureboot_state:
            print ("secureboot is enabled")
            SB_basic_commands.state = 1 
        else :
            print ("secureboot is disabled")


    if state :

        def dmesg_lockdownstatus(self):
            lockdown_dmesg = self.dmesg_log("Kernel is locked down from EFI Secure Boot")
            print (lockdown_dmesg)
    

sb_object = SB_basic_commands()
sb_object.dmesg_lockdownstatus()