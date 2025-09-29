from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QFileDialog, QSizePolicy, QScrollArea
import json
from functools import partial
from .themes import Themes
from .image_manager import ImageManager
from .decoder import decrypt_file
from .save_manager import SaveManager
from PyQt6.QtCore import Qt, QSize, QUrl
from PyQt6.QtGui import QFont, QCursor, QIcon, QDesktopServices

class Application:

    def __init__(self):

        self.app_data = self.init_app_data()

        self.app = QApplication([])
        self.window = QMainWindow()
        self.window.setWindowTitle(f"Silksong Completion Analyzer v{self.app_data['UserData']['version']}")
        self.app.setWindowIcon(QIcon("src/images/icons/ico/hornet_icon.ico"))
        self.window.resize(1400, 900)

        self.fullscreen = False

        self.font = QFont("Gill Sans MT", 10, QFont.Weight.Normal, italic=False)
        self.font_bold = QFont("Gill Sans MT", 10, QFont.Weight.Bold, italic=False)

        self.themes = Themes()

        self.IM = ImageManager()

        self.manager = None

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.main_widget = QWidget() 

        self.header_layout = QVBoxLayout()

        self.scroll_area.setWidget(self.main_widget)

        self.main_widget.setLayout(self.header_layout)

        self.window.setCentralWidget(self.scroll_area)

        self.window.keyPressEvent = self.toggle_fullscreen

        self.mode = self.app_data['UserData']['theme']
        self.switch_scrollbar()
        self.main_widget.setStyleSheet(self.themes.dark_theme if self.mode == 1 else self.themes.light_theme)

    def toggle_fullscreen(self, event):
            if event.key() == Qt.Key.Key_F11:
                if self.fullscreen:
                    self.window.showNormal()  
                    self.fullscreen = False
                else:
                    self.window.showFullScreen()  
                    self.fullscreen = True
            else:
                QMainWindow.keyPressEvent(self.window, event)


    def init_app_data(self):
        with open("src/app_data.json", "r") as config_file:
            return json.load(config_file)

    
    def run(self):

        self.display_title()

        self.display_file_path_helper()

        self.display_save_file_button()

        self.info_page()

        self.toggle_theme_button()

        self.window.show()

        self.app.exec()

    def display_basic_data(self):

        self.manager.display_fleur("hornet")

        self.manager.return_completion()

        self.manager.return_playtime()
        
        self.manager.display_fleur()

        self.manager.return_health()

        self.manager.return_silk()

        self.manager.return_rosaries()

        self.manager.return_shell_shards()

        self.manager.display_fleur()

        self.display_advanced_data()



    def display_advanced_data(self):

        self.manager.return_silk_hearts()

        self.manager.return_craftmetal()

        self.manager.return_mask_shards()

        self.manager.return_spool_fragments()

        self.manager.return_crafting_kit_upgrades()

        self.manager.return_tool_pouch_upgrades()

        self.manager.return_nail_upgrades()

        self.manager.return_silk_skills()

        self.manager.return_abilities()

        self.manager.return_crests()

        self.manager.return_simple_keys()

        self.manager.return_cylinders()

        self.manager.return_memory_lockets()

        self.manager.return_fleas()

        self.manager.return_tools()

        self.manager.display_fleur()

    def display_title(self):

        self.title_fleur = QLabel("", self.main_widget)
        self.title_fleur.setProperty("class", "header1")
        self.title_fleur.setPixmap(self.IM.fleurs['title'][self.mode].scaled(684, 243, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.title_fleur.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)


        h3 = QLabel("Your save file can be found at:")
        h3.setProperty("class", "header3")
        h3.setFont(self.font)
        h3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)


        self.header_layout.addWidget(self.title_fleur, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.header_layout.addWidget(h3, alignment=Qt.AlignmentFlag.AlignHCenter)

    def display_file_path_helper(self):

        helper_text = "%USERPROFILE%\\AppData\\LocalLow\\Team Cherry\\Hollow Knight Silksong\\"

        hover_text = "Click to copy to Clipboard..."

        h4 = QLabel(helper_text)

        h4.setProperty("class", "header4")
        
        h4.setFont(self.font)
        h4.setMinimumWidth(800)
        h4.setFixedHeight(50)

        # hover helper functions

        def on_enter(event):
            h4.setText(hover_text)
            h4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            
            
        
        def on_leave(event):
            h4.setText(helper_text)
            h4.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            
        
        def on_click(event):
            if event.button() == Qt.MouseButton.LeftButton:
                clipboard = QApplication.clipboard()
                clipboard.setText(helper_text)
                h4.setText("Copied!")
            
        h4.enterEvent = on_enter

        h4.leaveEvent = on_leave

        h4.mousePressEvent = on_click
        
        h4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_layout.addWidget(h4, alignment=Qt.AlignmentFlag.AlignHCenter)

    def display_save_file_button(self):
        self.save_button = QPushButton("Select Save File...")
        self.save_button.setProperty("class", "Main_Button")
        self.save_button.clicked.connect(self.file_picker)

        self.save_button.setFont(self.font)
        self.header_layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignHCenter)


    def file_picker(self):
        save_filepath = QFileDialog.getOpenFileName(self.main_widget, "Select a File...", "", "Binary data files (*.dat)")
       
        if save_filepath[0]:

            if self.manager is not None:
                self.manager.clear_layout(self.manager.data_layout)
                self.manager.fleurs.clear()
            
            self.manager = SaveManager(self, decrypt_file(save_filepath[0]))

            self.display_basic_data()


    def toggle_theme_button(self):

        self.settings_layout = QHBoxLayout()

        self.header_layout.addLayout(self.settings_layout)
        

        self.theme_button = QPushButton("")
        self.theme_button.setProperty("class", "Setting_Button")

        self.theme_button.setIcon(QIcon(self.IM.theme_icon[self.mode]))
        self.theme_button.setIconSize(QSize(36, 36))

        self.theme_button.setFont(self.font)
        self.theme_button.clicked.connect(self.toggle_theme)

        self.settings_layout.addWidget(self.theme_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)

    def info_page(self):

        self.info_layout = QVBoxLayout()
        self.info_layout.setSpacing(0)  
        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        self.info_layout.addStretch()

        self.header_layout.addLayout(self.info_layout)
        
        v_label = QLabel(f"Version {self.app_data['UserData']['version']}.  Work-in-Progress.")
        v_label.setProperty("class", "header3")
        v_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        v_label.setFont(self.font)

        self.info_layout.addWidget(v_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.github_layout = QHBoxLayout()
        self.github_layout.setSpacing(0)  
        self.github_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        self.info_layout.addLayout(self.github_layout)

        c_label = QLabel(f"Programmed and created by ")
        c_label.setProperty("class", "header3")
        c_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        c_label.setFont(self.font)

        self.github_layout.addWidget(c_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.git_icon = QLabel(f"")
        self.git_icon.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.git_icon.setPixmap(self.IM.github_icon[self.mode].scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        self.github_layout.addWidget(self.git_icon, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        git_label = QLabel(f"Jevv")
        git_label.setProperty("class", "Link_Label")
        git_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        git_label.setFont(self.font)

        self.github_layout.addWidget(git_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        date_label = QLabel(f"© 2025")
        date_label.setProperty("class", "header3")
        date_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        date_label.setFont(self.font)

        self.github_layout.addWidget(date_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.cherry_layout = QHBoxLayout()
        self.cherry_layout.setSpacing(0)  
        self.cherry_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        self.info_layout.addLayout(self.cherry_layout)

        self.steam_icon = QLabel(f"")
        self.steam_icon.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.steam_icon.setPixmap(self.IM.steam_icon[self.mode].scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        self.cherry_layout.addWidget(self.steam_icon, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        ss_label = QLabel(f"Hollow Knight:  Silksong")
        ss_label.setProperty("class", "Link_Label")
        ss_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        ss_label.setFont(self.font)

        self.cherry_layout.addWidget(ss_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)


        cc_label = QLabel(f"by ")
        cc_label.setProperty("class", "header3")
        cc_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        cc_label.setFont(self.font)

        self.cherry_layout.addWidget(cc_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.cherry_icon = QLabel(f"")
        self.cherry_icon.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.cherry_icon.setPixmap(self.IM.cherry_icon[self.mode].scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        self.cherry_layout.addWidget(self.cherry_icon, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)


        steam_label = QLabel(f"Team Cherry")
        steam_label.setProperty("class", "Link_Label")
        steam_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        steam_label.setFont(self.font)

        self.cherry_layout.addWidget(steam_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        date_2_label = QLabel(f"© 2017 - 2025")
        date_2_label.setProperty("class", "header3")
        date_2_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        date_2_label.setFont(self.font)

        self.cherry_layout.addWidget(date_2_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        def on_enter(label: QLabel, event):
            label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            
            
        def on_leave(label: QLabel, event):
            label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            
        
        def on_click(url, event):
            QDesktopServices.openUrl(QUrl(url))
            
        git_label.enterEvent = partial(on_enter, git_label)
        git_label.leaveEvent = partial(on_leave, git_label)
        git_label.mousePressEvent = partial(on_click, "https://github.com/langstonstewart/silksong-completion-analyzer")

        ss_label.enterEvent = partial(on_enter, ss_label)
        ss_label.leaveEvent = partial(on_leave, ss_label)
        ss_label.mousePressEvent = partial(on_click, "https://store.steampowered.com/app/1030300/Hollow_Knight_Silksong")

        steam_label.enterEvent = partial(on_enter, steam_label)
        steam_label.leaveEvent = partial(on_leave, steam_label)
        steam_label.mousePressEvent = partial(on_click, "https://www.teamcherry.com.au")
        
    def toggle_theme(self):
        if self.mode == 1:
            self.mode = 0
            self.app_data['UserData']['theme'] = 0

            self.main_widget.setStyleSheet(self.themes.light_theme)
            self.switch_scrollbar()
            
        elif self.mode == 0:
            self.mode = 1
            self.app_data['UserData']['theme'] = 1

            self.main_widget.setStyleSheet(self.themes.dark_theme)
            self.switch_scrollbar()

        with open("src/app_data.json", "w") as config_file:
                json.dump(self.app_data, config_file, indent=4)

        self.reload_images()

        if self.manager is not None:
            self.manager.reload_images()

    def reload_images(self):

        self.title_fleur.setPixmap(self.IM.fleurs['title'][self.mode].scaled(684, 243, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.git_icon.setPixmap(self.IM.github_icon[self.mode].scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.theme_button.setIcon(QIcon(self.IM.theme_icon[self.mode]))
        self.steam_icon.setPixmap(self.IM.steam_icon[self.mode].scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.cherry_icon.setPixmap(self.IM.cherry_icon[self.mode].scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def switch_scrollbar(self):
        if self.mode == 1:
            self.scroll_area.verticalScrollBar().setStyleSheet("QScrollBar"
                                "{"
                                "background : #1a1a1a;"
                                "}"
                                "QScrollBar::handle"
                                "{"
                                "background : #8d8d8d;"
                                "border-radius: 5px;"
                                "}"
                                "QScrollBar::handle::pressed"
                                "{"
                                "background : #aeaeae;"
                                "}"
                                
                                )
        elif self.mode == 0:
            self.scroll_area.verticalScrollBar().setStyleSheet("QScrollBar"
                                "{"
                                "background : #8d8d8d;"
                                "}"
                                "QScrollBar::handle"
                                "{"
                                "background : #aeaeae;"
                                "border-radius: 5px;"
                                "}"
                                "QScrollBar::handle::pressed"
                                "{"
                                "background : #b6b6b6;"
                                "}"
                                
                                )
            

        
    


        
              

        

        