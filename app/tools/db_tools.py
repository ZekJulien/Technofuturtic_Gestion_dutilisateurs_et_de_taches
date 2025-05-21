from sqlalchemy.orm import Session

class DbTools:
    def __init__(self, session: Session) -> None:
        self.session: Session = session
    
    def commit(self) -> bool:
        """
        Validates the transaction. If an error occurs, performs a rollback and raises the exception for handling or display.
        Returns:
            bool: True if commit successful
        """
        try:
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            raise e