import lib_main

class common_commands(lib_main.main_class):
    def uname(self,option):
        command = "uname " + option
        self.run_command("uname " + option)
        pass
    
    def changelog(self,package_name):
        print("get ur changelog of the package here")

    def dmesg_log(self):
        status = self.run_command("dmesg")
        return status.stdout
    
    def dmesg_grep_log(self,grep_mesg):
        status = self.run_command(f"dmesg | grep {grep_mesg}")
        return status

    def journalctl_log(self,**kwargs):
        pass

    def hostname(self):
        print('provide hostname')

    def architecture(self):
        print("architecture")

    def release(self):
        print("cat /etc/oracle-release")


command = common_commands()

command.uname("-r")
