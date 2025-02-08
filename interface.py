import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QHBoxLayout, QLineEdit, QLabel, QFrame, QSizePolicy)
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor


class CustomButton(QPushButton):
    def __init__(self, text, icon_name=None):
        super().__init__(text)
        self.setFixedHeight(40)
        self.setFont(QFont('Arial', 10))
        if icon_name:
            self.setIcon(QIcon(f'icons/{icon_name}.png'))
        self.setStyleSheet("""
            QPushButton {
                background-color: #2962ff;
                color: white;
                border-radius: 5px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
            QPushButton:pressed {
                background-color: #0d47a1;
            }
        """)


class CustomSearchBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(35)
        self.setFont(QFont('Arial', 10))
        self.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QLineEdit:focus {
                border: 2px solid #2962ff;
            }
        """)


class FolderManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Configuration de la fenêtre principale
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
            }
        """)

        # Layout principal avec marges
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Conteneur du haut
        top_container = QFrame()
        top_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        top_layout = QHBoxLayout(top_container)

        # Barre de recherche améliorée
        self.search_bar = CustomSearchBar()
        self.search_bar.setPlaceholderText("🔍 Rechercher un dossier...")

        # Horloge avec style
        self.clock_label = QLabel()
        self.clock_label.setFont(QFont('Arial', 12, QFont.Weight.Bold))
        self.clock_label.setStyleSheet("color: #2962ff;")
        self.update_time()

        top_layout.addWidget(self.search_bar, stretch=4)
        top_layout.addWidget(self.clock_label, stretch=1, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(top_container)

        # Conteneur des boutons
        btn_container = QFrame()
        btn_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 15px;
            }
        """)
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.setSpacing(10)

        # Création des boutons personnalisés
        self.new_btn = CustomButton("Nouveau dossier", "new")
        self.edit_btn = CustomButton("Modifier dossier", "edit")
        self.delete_btn = CustomButton("Supprimer dossier", "delete")
        self.settings_btn = CustomButton("Réglages", "settings")

        # Ajout des boutons avec espacement égal
        for btn in [self.new_btn, self.edit_btn, self.delete_btn, self.settings_btn]:
            btn_layout.addWidget(btn)

        layout.addWidget(btn_container)

        # Timer pour l'horloge
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Configuration finale de la fenêtre
        self.setLayout(layout)
        self.setWindowTitle("Gestionnaire de Dossiers")
        self.setMinimumSize(600, 250)
        self.resize(800, 300)

    def update_time(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.clock_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Application du style global
    app.setStyle('Fusion')

    # Création et affichage de la fenêtre
    window = FolderManagerUI()
    window.show()

    sys.exit(app.exec())