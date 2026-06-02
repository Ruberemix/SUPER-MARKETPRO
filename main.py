import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from database.db_manager import inicializar_db
from views.main_window import MainWindow

if __name__ == "__main__":
    inicializar_db()
    app = MainWindow()
    app.mainloop()
