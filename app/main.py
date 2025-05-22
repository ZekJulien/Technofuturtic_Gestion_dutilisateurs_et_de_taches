# database
from database import Db
# ui
from ui import UserUI
# services
from services import UserService, TaskService
# tools
from tools import Tools

class App:
    """
    Main class for the application.
    
    This class initializes and manages the application's core components.
    """
    def __init__(self):
        self._user_ui : UserUI = None
        self._task_service: TaskService = None
        self._initialize_app()
        self.menu()
        #self._testing()

    def _initialize_app(self) -> None:
        """
        Initialize database connection and services
        """
        if not Db.is_connected():
            raise RuntimeError("Failed to connect to database")
        Db.create_tables()
        print("✅ Connection established")
        self._user_ui = UserUI()
        self._task_service = TaskService()




    def menu(self):
        Tools.clearConsole()
        while True:
            print("User and Task Management")
            print("""
                  ----------------
                  | 1 | 👨 Users |
                  ----------------
                  | 2 | 🔤 Tasks |
                  ----------------
                  | 3 | ❌ exit  |
                  ----------------
            """)
            match Tools.input_numeric_int("Choose 1 to 3 : ", "🛑 Error : Only 1 to 3", lambda x : x > "0" and x < "4"):
                case 1:
                    self._user_ui.menu_user()
                case 2:
                    pass
                case 3:
                    exit(1)



    def _testing(self) -> None:
        """
        Create sample users for testing
        """
        pass



def main():
    try:
        App()
    except Exception as e:
        print(f"Application failed to start: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
