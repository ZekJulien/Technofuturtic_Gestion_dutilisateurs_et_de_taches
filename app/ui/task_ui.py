from tools import Tools, UiTools
from services import TaskService, UserService

class TaskUi:
    def __init__(self):
        self._task_service : TaskService = TaskService()
        self._user_service : UserService = UserService()

    def find_user(self, input_message : str):
        bool_user : bool = True
        while bool_user:
            user = self._user_service.get_by_email(input(input_message))
            if user:
                bool_user = False
                return user
            else:
                Tools.sleep(3)
                if Tools.input_numeric_int("Do you want to find another user ? 1 to YES | 2 back to the menu : ", "Error : Only 1 to YES | 2 back to the menu", lambda x : x > "0" and x < "3") == 2:
                    return True

    def view_add(self):
        Tools.clearConsole()
        UiTools.header("➕ Add a new task")
        user = self.find_user("Who should be added to this task? \nEnter email : ")
        if user == False:
            return
        Tools.clearConsole()
        self._task_service.add(
            description=input(f"Task description for {user.email} : "),
            user = user
        )
        Tools.sleep(3)
        return
    
    def view_get_all(self):
        Tools.clearConsole()
        UiTools.header("🟰  Show all tasks")
        tasks = self._task_service.get_all()
        if not tasks:
            Tools.sleep(3)
            return
        for user in tasks:
            print(user)
            UiTools.separator()
        input("Enter to return to the task management menu...")
        return
    
    def view_get_by_user(self):
        Tools.clearConsole()
        UiTools.header("🔎 Find user tasks")
        user = self.find_user("Enter a email to find task(s) user : ")
        if user == False:
            return
        tasks = self._task_service.get_by_user(user.id)
        Tools.clearConsole()
        if not tasks:
            Tools.sleep(3)
            return
        for task in tasks:
            print(task)
            UiTools.separator()
        input("Enter to return to the user management menu...")

    def view_update_task(self):
        Tools.clearConsole()
        UiTools.header("➗ Update a task")
        user = self.find_user("Enter a email to find task(s) user : ")
        Tools.clearConsole()
        if user == False:
            Tools.sleep(3)
            return
        tasks = self._task_service.get_by_user(user.id)
        if not tasks:
            Tools.sleep(3)
            return
        for task in tasks:
            print(f"""
                  Task ID : {task.id}
                  """)
            print(task)
            UiTools.separator()
        selecion = Tools.input_numeric_int(f"Which task would you like to update ? 1 to {len(tasks)} | 0 to back menu : ", f"Error : Only 1 to {len(tasks)} | 0 to back menu", lambda x : x >= "0" and x <= f"{len(tasks)}")
        Tools.clearConsole()
        if selecion == 0:
            return
        self._task_service.update(
            id_task=tasks[selecion-1].id,
            description=Tools.input_ui_str(f"Enter to save {tasks[selecion-1].description} or new description : "),
        )
        Tools.sleep(3)
        return
    
    def view_delete_task(self):
        Tools.clearConsole()
        UiTools.header("➖ Delete a task")
        user = self.find_user("Enter a email to find task(s) user : ")
        if user == False:
            Tools.sleep(3)
            return
        tasks = self._task_service.get_by_user(user.id)
        Tools.clearConsole()
        if not tasks:
            Tools.sleep(3)
            return
        for task in tasks:
            print(f"""
                  Task ID : {task.id}
                  """)
            print(task)
            UiTools.separator()
        selecion = Tools.input_numeric_int(f"Which task would you like to delete ? 1 to {len(tasks)} | 0 to back menu : ", f"Error : Only 1 to {len(tasks)} | 0 to back menu", lambda x : x >= "0" and x <= f"{len(tasks)}")
        Tools.clearConsole()
        if selecion == 0:
            return
        self._task_service.delete(tasks[selecion-1].id)
        Tools.sleep(3)
        return
    
    def menu_task(self):
        while True:
            Tools.clearConsole()
            print("🔤 Task management")
            print("""
                  1 - 🟰  Show all tasks
                  2 - ➕ Add a new task
                  3 - 🔎 Find user tasks
                  4 - ➗ Update a task
                  5 - ➖ Delete a task
                  6 - Back to the main menu
            """)
            match Tools.input_numeric_int("Choose (1 to 6) : ", "🛑 Error : Only 1 to 6", lambda x : x > "0" and x < "7"):
                case 1:
                    self.view_get_all()
                case 2:
                    self.view_add()
                case 3:
                    self.view_get_by_user()
                case 4:
                    self.view_update_task()
                case 5:
                    self.view_delete_task()
                case 6:
                    return
