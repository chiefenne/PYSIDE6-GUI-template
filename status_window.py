from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PySide6.QtCore import Qt

class StatusWindow(QWidget):
    def __init__(self, max_lines=100):
        super().__init__()
        self.max_lines = max_lines

        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # Make text not editable
        self.text_edit.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def append_message(self, message):
        # Append the new message
        self.text_edit.append(message)

        # Limit the number of lines
        text = self.text_edit.toPlainText()
        lines = text.split('\n')

        if len(lines) > self.max_lines:
            # Keep only the last 'max_lines' lines
            lines = lines[-self.max_lines:]
            self.text_edit.setPlainText('\n'.join(lines))

        # Move cursor to the end
        self.text_edit.moveCursor(self.text_edit.textCursor().End)
