from tools import Tools, UiTools
from services import UserService

class UserUI:
    def __init__(self):
        self._user_service : UserService = UserService()

    def view_add(self):
        Tools.clearConsole()
        UiTools.header("➕ Add a new user")
        self._user_service.add(
            username=input("Username : "),
            email=input("Email : "),
            password=input("Password : "),
        )
        Tools.sleep(3)
        return
    
    def view_get_all(self):
        Tools.clearConsole()
        UiTools.header("🟰  Show all users")
        users = self._user_service.get_all()
        if not users:
            Tools.sleep(3)
            return
        for user in users:
            print(user)
            UiTools.separator()
        input("Enter to return to the user management menu...")
        return
    
    def view_get_by_email(self):
        Tools.clearConsole()
        UiTools.header("🔎 Find a user")
        user = self._user_service.get_by_email(input("Enter a email to find user : "))
        if not user:
            Tools.sleep(3)
            return
        print(user)
        input("Enter to return to the user management menu...")

    def view_update_user(self):
        Tools.clearConsole()
        UiTools.header("➗ Update a user")
        user = self._user_service.get_by_email(input("Enter a email to find user : "))
        if not user:
            Tools.sleep(3)
            return
        self._user_service.update(
            id=user.id,
            username=Tools.input_ui_str(f"Enter to save {user.username} or new username : "),
            email=Tools.input_ui_str(f"Enter to save {user.email} or new email : "),
            password=Tools.input_ui_str(f"Enter to save your actual password or new password : "),
            is_active= True if Tools.input_numeric_int(f"Enter to save {user.is_active} or 1 to activate | 2 to disable : ", "Error : Only 1 or 2", lambda x : x > "0" and x < "3") == 1 else False,
        )
        Tools.sleep(3)
        return
    
    def view_delete_user(self):
        Tools.clearConsole()
        UiTools.header("➖ Delete a user")
        user = self._user_service.get_by_email(input("Enter a email to find user : "))
        if not user:
            Tools.sleep(3)
            return
        if Tools.input_numeric_int(f"Are you sure to delete this {user.username} ? 1 to cancel | 2 to delete :", "Error : Only 1 or 2", lambda x : x > "0" and x < "3") == 2:
            self._user_service.delete(user.id)
            Tools.sleep(3)
            return
        
    def menu_user(self):
        while True:
            Tools.clearConsole()
            print("🧑User management")
            print("""
                  1 - 🟰  Show all users
                  2 - ➕ Add a new user
                  3 - 🔎 Find a user
                  4 - ➗ Update a user
                  5 - ➖ Delete a user
                  6 - Back to the main menu
            """)
            match Tools.input_numeric_int("Choose (1 to 6) : ", "🛑 Error : Only 1 to 6", lambda x : x > "0" and x < "7"):
                case 1:
                    self.view_get_all()
                case 2:
                    self.view_add()
                case 3:
                    self.view_get_by_email()
                case 4:
                    self.view_update_user()
                case 5:
                    self.view_delete_user()
                case 6:
                    return
