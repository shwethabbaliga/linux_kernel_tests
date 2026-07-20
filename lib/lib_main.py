import subprocess
from abc import ABC , abstractmethod 

class main_class:
    def run_command(self,command):
        status = subprocess.run(command,shell=True,capture_output=True,text=True)
        print (command)
        if not status.returncode: 
            print (f"command execution is perfect o/p is following {status.stdout}")
            return status.stdout
        else :
            return status.stderr
    
            

