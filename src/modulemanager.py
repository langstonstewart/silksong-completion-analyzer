import subprocess, sys
from .banner import banner

class ModuleManager:
    def __init__(self):
        self.module_list = ["PyQt6", "pycryptodome", "pandas"]

    def module_check(self):
        from importlib import import_module
        try:
            banner()
            # check if user has modules, install prompt if not
            print("Checking for modules, please wait...")

            for module in self.module_list:
                import_module(module)
                self.module_list.remove(module)

            banner()

            print("Modules imported.")
    
            return True

        except ModuleNotFoundError:
            banner()
            print("Silksong Completion Analyzer requires the following dependencies to run functionally:")

            for module in self.module_list:
                print(f"- {module.title()}")
            banner()

            while True:
                prompt = input("Would you like to install these modules now? (Y/N) > ")
                banner()
                if prompt.lower() in ["yes", "y"]:
                    
                    for module in self.module_list:
                        self.installer(module)

                    return True
                
                elif prompt.lower() in ["no", "n"]:
                    return False   

    def installer(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])