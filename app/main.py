from database import InitDb

class App:
    """
    Main class for the application.
    """
    if not InitDb.init():
        exit()
    

if __name__ == "__main__":
    App