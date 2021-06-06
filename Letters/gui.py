#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSlider, \
    QLineEdit, QComboBox, QTextEdit, QCheckBox, QRadioButton, QButtonGroup, QDialog
from PyQt5.QtCore import Qt
import json

ws_point1 = (-15, 12)
ws_point2 = (15, 28)

font_width = 3
font_len_wid_ratio = 1.667 #5/3
database_start_coords = (0, 20, 8)

start_right = 3
start_up = 5

gap = 1


class GUI(QMainWindow):
    def __init__(self):
        """
        """
        """
        Initial Setup
        Create Window
        Set Title
        """
        super(GUI, self).__init__()
        self.setWindowTitle('Set Values')


        """
        Central Widget
        layouts
        Add Widget
        # shape and size
        # sub windows   
        """
        widget = QWidget()
        self.setCentralWidget(widget)

        outside_layout = QVBoxLayout()
        widget.setLayout(outside_layout)

        layout = QVBoxLayout()
        outside_layout.addLayout(layout)

        # workspace
        ws_layout = QVBoxLayout()
        ws_heading = QVBoxLayout()
        ws_options = QVBoxLayout()

        ws_layout.addLayout(ws_heading)
        ws_layout.addLayout(ws_options)
        layout.addLayout(ws_layout)

        # Font layout
        font_layout = QVBoxLayout()
        font_heading = QVBoxLayout()
        font_options = QVBoxLayout()

        font_layout.addLayout(font_heading)
        font_layout.addLayout(font_options)
        layout.addLayout(font_layout)

        # Start space
        starting_layout = QVBoxLayout()
        starting_heading = QVBoxLayout()
        starting_options = QVBoxLayout()
        #
        starting_layout.addLayout(starting_heading)
        starting_layout.addLayout(starting_options)
        layout.addLayout(starting_layout)

        # Gap between letters space
        gap_layout = QVBoxLayout()
        gap_heading = QVBoxLayout()
        gap_options = QVBoxLayout()

        gap_layout.addLayout(gap_heading)
        gap_layout.addLayout(gap_options)
        layout.addLayout(gap_layout)

        # Radio Button Groups
        ws_group = QButtonGroup(widget)
        font_group = QButtonGroup(widget)
        starting_group = QButtonGroup(widget)
        gap_group = QButtonGroup(widget)



        """
        Vertical separations of all options
        """
        self.ws_label = QLabel('Select workspace size:')
        ws_heading.addWidget(self.ws_label)

        self.font_label = QLabel('Select font size:')
        font_heading.addWidget(self.font_label)

        self.starting_label = QLabel('Select start spacing:')
        starting_heading.addWidget(self.starting_label)

        self.gap_label = QLabel('Select spacing between letters:')
        gap_heading.addWidget(self.gap_label)

        """
        WorkSpace layout
        """
        self.ws_user_input = QRadioButton('Input in cms:')
        ws_group.addButton(self.ws_user_input)
        ws_options.addWidget(self.ws_user_input)

        self.ws_user_input_text = QLineEdit("")
        ws_options.addWidget(self.ws_user_input_text)

        self.ws_or_label = QLabel("OR")
        ws_options.addWidget(self.ws_or_label)

        self.ws_default = QRadioButton('Default:')
        ws_group.addButton(self.ws_default)
        ws_options.addWidget(self.ws_default)

        self.ws_default_text = QLineEdit("Corner 1: {} Corner 2: {}".format(ws_point1, ws_point2))
        self.ws_default_text.setReadOnly(True)
        ws_options.addWidget(self.ws_default_text)

        """
        Font layout
        """
        self.font_user_input = QRadioButton('Input in cms: Width, Ratio of length/width')
        font_group.addButton(self.font_user_input)
        font_options.addWidget(self.font_user_input)

        self.font_user_input_text = QLineEdit("")
        font_options.addWidget(self.font_user_input_text)

        self.font_or_label = QLabel("OR")
        font_options.addWidget(self.font_or_label)

        self.font_default = QRadioButton('Default:')
        font_group.addButton(self.font_default)
        font_options.addWidget(self.font_default)

        self.font_default_text = QLineEdit("Width: {} Ratio: {}".format(font_width, font_len_wid_ratio))
        self.font_default_text.setReadOnly(True)
        font_options.addWidget(self.font_default_text)

        """
        Start layout
        """
        self.starting_user_input = QRadioButton('Input in cms: Distance from Right boundary, Upper boundary')
        starting_group.addButton(self.starting_user_input)
        starting_options.addWidget(self.starting_user_input)

        self.starting_user_input_text = QLineEdit("")
        starting_options.addWidget(self.starting_user_input_text)

        self.starting_or_label = QLabel("OR")
        starting_options.addWidget(self.starting_or_label)

        self.starting_default = QRadioButton('Default:')
        starting_group.addButton(self.starting_default)
        starting_options.addWidget(self.starting_default)

        self.starting_default_text = QLineEdit("Distance from Right boundary: {} Upper boundary: {}".format(start_right, start_up))
        self.starting_default_text.setReadOnly(True)
        starting_options.addWidget(self.starting_default_text)

        """
        Gap layout
        """
        self.gap_user_input = QRadioButton('Input in cms: Gap')
        gap_group.addButton(self.gap_user_input)
        gap_options.addWidget(self.gap_user_input)

        self.gap_user_input_text = QLineEdit("")
        gap_options.addWidget(self.gap_user_input_text)

        self.gap_or_label = QLabel("OR")
        gap_options.addWidget(self.gap_or_label)

        self.gap_default = QRadioButton('Default:')
        gap_group.addButton(self.gap_default)
        gap_options.addWidget(self.gap_default)

        self.gap_default_text = QLineEdit("{}".format(gap))
        self.gap_default_text.setReadOnly(True)
        gap_options.addWidget(self.gap_default_text)

        """
        Done Button
        """
        self.done_button = QPushButton('OK')
        outside_layout.addWidget(self.done_button)
        self.done_button.clicked.connect(self.update_json_file)

    def convert_to_dict(self, text_to_add):
        new_dict = {}
        print("FULL TEXT:", text_to_add)
        for text in text_to_add:
            new_text = text.split(":")
            print("NEW TEXT:", new_text)
            new_text[1] = new_text[1].replace('[','')
            new_text[1] = new_text[1].replace(']', '')
            float_vals = new_text[1].split(",")
            print("FLOAT VALS:", float_vals)
            for vals in range(0, len(float_vals)):
                float_vals[vals] = float(float_vals[vals])
            new_dict.update({new_text[0]: float_vals})
        # print("Text to add: {} \nKey value split: {} \nfloats: {}\n".format(text_to_add, new_text, float_vals))
        return new_dict

if __name__ == '__main__':
    app = QApplication([])

    interface = GUI()

    interface.show()

    app.exec_()