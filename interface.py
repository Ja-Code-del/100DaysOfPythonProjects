import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import QTimer, QTime


class FolderManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout principal
        layout = QVBoxLayout()

        # Ligne du haut avec recherche et horloge
        top_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Rechercher un dossier...")
        self.clock_label = QLabel()
        self.update_time()
        top_layout.addWidget(self.search_bar)
        top_layout.addWidget(self.clock_label)
        layout.addLayout(top_layout)

        # Boutons
        btn_layout = QHBoxLayout()
        self.new_btn = QPushButton("Nouveau dossier")
        self.edit_btn = QPushButton("Modifier dossier")
        self.delete_btn = QPushButton("Supprimer dossier")
        self.settings_btn = QPushButton("Réglages")

        btn_layout.addWidget(self.new_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.settings_btn)

        layout.addLayout(btn_layout)

        # Timer pour mettre à jour l'heure
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.setLayout(layout)
        self.setWindowTitle("Gestionnaire de Dossiers")
        self.resize(400, 200)

    def update_time(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.clock_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderManagerUI()
    window.show()
    sys.exit(app.exec())
