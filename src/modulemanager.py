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
                    for module in self.module_list:
                        self.installer(module)

                    return True
        
    def installer(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])