import subprocess
from abc import ABC , abstractmethod 

class main_class:
    def run_command(self,command):
        status = subprocess.run(command,shell=True,capture_output=True,Text=True)
        print (command)
        if status.returncode: 
            pass

