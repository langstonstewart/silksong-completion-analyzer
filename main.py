from src import modulemanager

if modulemanager.ModuleManager().module_check():

    from src import app
    
    analyzer = app.Application()
    analyzer.run()
    




