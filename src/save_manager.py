from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QTableView, QStyledItemDelegate, QStyle
import pandas
from .themes import Themes
from .image_manager import ImageManager
from .dataframe_manager import Dataframe_Manager
from PyQt6.QtCore import Qt, QAbstractTableModel, QUrl
from PyQt6.QtGui import QFont, QCursor, QDesktopServices, QColor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.app import Application

class SaveManager:
    def __init__(self, app: "Application", save_file):

        self.app = app

        self.save_data = save_file

        self.themes = Themes()

        self.IM = ImageManager()

        self.DM = Dataframe_Manager(self.save_data)

        self.chart_list = []

        self.fleurs = []

        self.data_layout = QVBoxLayout()

        self.data_layout.setSpacing(10)

        self.index = self.app.header_layout.indexOf(self.app.info_layout)

        self.app.header_layout.insertLayout(self.index, self.data_layout)

    def clear_layout(self, layout: QVBoxLayout):
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()
            elif item.layout() is not None:
                self.clear_layout(item.layout())


    
    def display_fleur(self, style="default"):

        fleur = QLabel("", self.app.main_widget)
        fleur.setProperty("class", "header1")
        fleur.setPixmap(self.IM.fleurs[style][self.app.mode])

        fleur.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.data_layout.addWidget(fleur, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.fleurs.append((fleur, style))

    def return_completion(self):

        self.completion = QLabel(f"Game Completion: {int(self.save_data['playerData']['completionPercentage'])}%", self.app.main_widget)
        self.completion.setProperty("class", "Completion_Label")

        self.completion.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.completion.setFont(self.app.font_bold)

        self.data_layout.addWidget(self.completion, alignment=Qt.AlignmentFlag.AlignHCenter)


    def return_playtime(self):

        playtime_var = f"{int(self.save_data['playerData']['playTime'] // 3600)} Hours, {int(self.save_data['playerData']['playTime'] % 3600 // 60)} Minutes"

        self.playtime_text = QLabel(f"Time Played: {playtime_var}", self.app.main_widget)
        self.playtime_image = QLabel("", self.app.main_widget)
        self.playtime_text.setProperty("class", "header2")

        self.playtime_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.playtime_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.playtime_text.setFont(self.app.font)
        self.playtime_image.setPixmap(self.IM.clock_icon[self.app.mode].scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        

        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.playtime_image)  
        h_layout.addWidget(self.playtime_text) 

    
        self.data_layout.addLayout(h_layout)

    def return_health(self):

        heart_count = self.save_data["playerData"]["maxHealth"]
        
        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.health_text = QLabel("Health:", self.app.main_widget)
        self.health_text.setProperty("class", "header2")
        self.health_text.setFont(self.app.font)
        self.health_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.health_count = QLabel(f"({heart_count})", self.app.main_widget)
        self.health_count.setProperty("class", "header2")
        self.health_count.setFont(self.app.font)
        self.health_count.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        h_layout.addWidget(self.health_text)

        for _ in range(heart_count):
            health_icon = QLabel("", self.app.main_widget)
            health_icon.setPixmap(self.IM.health_icon[self.app.mode].scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            health_icon.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
            h_layout.addWidget(health_icon)

        h_layout.addWidget(self.health_count)

        self.data_layout.addLayout(h_layout)


    def return_silk(self):

        silk_amount = self.save_data["playerData"]['silkMax']
        
        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.silk_text = QLabel("Silk:", self.app.main_widget)
        self.silk_text.setProperty("class", "header2")
        self.silk_text.setFont(self.app.font)
        self.silk_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.silk_count = QLabel(f"({silk_amount})", self.app.main_widget)
        self.silk_count.setProperty("class", "header2")
        self.silk_count.setFont(self.app.font)
        self.silk_count.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)


        h_layout.addWidget(self.silk_text)

        for _ in range(silk_amount):
            silk_icon = QLabel("", self.app.main_widget)
            silk_icon.setPixmap(self.IM.silk_icon[self.app.mode].scaled(18, 42, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            silk_icon.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
            h_layout.addWidget(silk_icon)

        h_layout.addWidget(self.silk_count)

        self.data_layout.addLayout(h_layout)

    
    def return_rosaries(self):
        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        r_count = self.save_data["playerData"]["geo"]

        self.r_image = QLabel("", self.app.main_widget)
        self.r_image.setPixmap(self.IM.rosary_icon[self.app.mode].scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.r_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.r_text = QLabel(f"{r_count}", self.app.main_widget)
        self.r_text.setProperty("class", "header2")
        self.r_text.setFont(self.app.font)
        self.r_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        h_layout.addWidget(self.r_image)
        h_layout.addWidget(self.r_text)

        self.data_layout.addLayout(h_layout)

        
        
    def return_shell_shards(self):
        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        ss_count = self.save_data["playerData"]["ShellShards"]

        self.ss_image = QLabel("", self.app.main_widget)
        self.ss_image.setPixmap(self.IM.ss_icon[self.app.mode].scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.ss_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.ss_text = QLabel(f"{ss_count}", self.app.main_widget)
        self.ss_text.setProperty("class", "header2")
        self.ss_text.setFont(self.app.font)
        self.ss_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        h_layout.addWidget(self.ss_image)
        h_layout.addWidget(self.ss_text)

        self.data_layout.addLayout(h_layout)

    def return_silk_hearts(self):

        sh_count = self.save_data['playerData']['silkRegenMax']

        self.sh_text = QLabel(f"Silk Hearts ({sh_count}/3)", self.app.main_widget)
        self.sh_text.setProperty("class", "header2")
        self.sh_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sh_text.setFont(self.app.font)

        self.sh_image = QLabel("", self.app.main_widget)
        self.sh_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sh_image.setPixmap(self.IM.silk_hearts[sh_count][self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.sh_image)  
        h_layout.addWidget(self.sh_text) 

        self.data_layout.addLayout(h_layout)

        self.sh_info = QLabel(f"Passively regenerates the user's silk. Each heart gives 1%.", self.app.main_widget)
        self.sh_info.setProperty("class", "header2")
        self.sh_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sh_info.setFont(self.app.font)

        self.data_layout.addWidget(self.sh_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(self.DM.silk_heart_df(), 128)

    def return_craftmetal(self):

        cm_data = self.DM.craftmetal_df()
        cm_count = cm_data[0]

        self.cm_text = QLabel(f"Craftmetal ({cm_count})", self.app.main_widget)
        self.cm_text.setProperty("class", "header2")
        self.cm_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.cm_text.setFont(self.app.font)

        self.cm_image = QLabel("", self.app.main_widget)
        self.cm_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.cm_image.setPixmap(self.IM.craftmetal_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.cm_image)  
        h_layout.addWidget(self.cm_text) 

        self.data_layout.addLayout(h_layout)

        self.cm_info = QLabel(f"Used to help vendors create new tools.", self.app.main_widget)
        self.cm_info.setProperty("class", "header2")
        self.cm_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.cm_info.setFont(self.app.font)

        self.data_layout.addWidget(self.cm_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(cm_data[1], 278)

    def return_mask_shards(self):
        ms_data = self.DM.mask_shard_df()
        ms_count = ms_data[0]

        self.ms_text = QLabel(f"Mask Shards ({ms_count})", self.app.main_widget)
        self.ms_text.setProperty("class", "header2")
        self.ms_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ms_text.setFont(self.app.font)

        self.ms_image = QLabel("", self.app.main_widget)
        self.ms_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ms_image.setPixmap(self.IM.mask_shard_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.ms_image)  
        h_layout.addWidget(self.ms_text) 

        self.data_layout.addLayout(h_layout)

        self.ms_info = QLabel(f"Strengthens the user's mask, increasing max health every 4 shards (1%).", self.app.main_widget)
        self.ms_info.setProperty("class", "header2")
        self.ms_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ms_info.setFont(self.app.font)

        self.data_layout.addWidget(self.ms_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(ms_data[1], 639)

    def return_spool_fragments(self):
        sf_data = self.DM.spool_fragments_df()
        sf_count = sf_data[0]

        self.sf_text = QLabel(f"Spool Fragments ({sf_count})", self.app.main_widget)
        self.sf_text.setProperty("class", "header2")
        self.sf_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sf_text.setFont(self.app.font)

        self.sf_image = QLabel("", self.app.main_widget)
        self.sf_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sf_image.setPixmap(self.IM.spool_fragment_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.sf_image)  
        h_layout.addWidget(self.sf_text) 

        self.data_layout.addLayout(h_layout)

        self.sf_info = QLabel(f"Lengthens the user's Silk Spool, increasing max silk every 2 fragments (1%).", self.app.main_widget)
        self.sf_info.setProperty("class", "header2")
        self.sf_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sf_info.setFont(self.app.font)

        self.data_layout.addWidget(self.sf_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(sf_data[1], 578)

    def return_nail_upgrades(self):
        nu_data = self.DM.nail_upgrades_df()
        nu_count = nu_data[0]

        self.nu_text = QLabel(f"Needle Upgrades ({nu_count})", self.app.main_widget)
        self.nu_text.setContentsMargins(0, 5, 0, 0)
        self.nu_text.setProperty("class", "header2")
        self.nu_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.nu_text.setFont(self.app.font)


        self.nu_image = QLabel("", self.app.main_widget)
        self.nu_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.nu_image.setPixmap(self.IM.nail_upgrade_icons[int(nu_count.split("/")[0])][self.app.mode].scaled(450, 66, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        self.nu_info = QLabel(f"Strengthens the user's Needle. Requires Pale Oil. Each upgrade gives 1%.", self.app.main_widget)
        self.nu_info.setProperty("class", "header2")
        self.nu_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.nu_info.setFont(self.app.font)

        

        self.data_layout.addWidget(self.nu_text, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.data_layout.addWidget(self.nu_image, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.data_layout.addWidget(self.nu_info, alignment=Qt.AlignmentFlag.AlignHCenter)


        self.create_chart(nu_data[1], 159)

    
    def return_crafting_kit_upgrades(self):
        ck_data = self.DM.crafting_kit_upgrades_df()
        ck_count = ck_data[0]

        self.ck_text = QLabel(f"Crafting Kit Upgrades ({ck_count})", self.app.main_widget)
        self.ck_text.setProperty("class", "header2")
        self.ck_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ck_text.setFont(self.app.font)

        self.ck_image = QLabel("", self.app.main_widget)
        self.ck_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ck_image.setPixmap(self.IM.crafting_kit_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.ck_image)  
        h_layout.addWidget(self.ck_text) 

        self.data_layout.addLayout(h_layout)

        self.ck_info = QLabel(f"Increases the base damage dealt by tools. Each upgrade gives 1%.", self.app.main_widget)
        self.ck_info.setProperty("class", "header2")
        self.ck_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ck_info.setFont(self.app.font)

        self.data_layout.addWidget(self.ck_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(ck_data[1], 159)

    def return_tool_pouch_upgrades(self):
        tp_data = self.DM.tool_pouch_upgrades_df()
        tp_count = tp_data[0]

        self.tp_text = QLabel(f"Tool Pouch Upgrades ({tp_count})", self.app.main_widget)
        self.tp_text.setProperty("class", "header2")
        self.tp_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.tp_text.setFont(self.app.font)

        self.tp_image = QLabel("", self.app.main_widget)
        self.tp_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.tp_image.setPixmap(self.IM.tool_pouch_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.tp_image)  
        h_layout.addWidget(self.tp_text) 

        self.data_layout.addLayout(h_layout)

        self.tp_info = QLabel(f"Increases tool capacity, along with Shell Shard capacity. Each upgrade gives 1%.", self.app.main_widget)
        self.tp_info.setProperty("class", "header2")
        self.tp_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.tp_info.setFont(self.app.font)

        self.data_layout.addWidget(self.tp_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(tp_data[1], 159)


    def return_silk_skills(self):
        ss_data = self.DM.silk_skills_df()
        ss_count = ss_data[0]

        self.ss_text = QLabel(f"Silk Skills ({ss_count})", self.app.main_widget)
        self.ss_text.setProperty("class", "header2")
        self.ss_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ss_text.setFont(self.app.font)

        self.ss_image = QLabel("", self.app.main_widget)
        self.ss_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ss_image.setPixmap(self.IM.silk_skills_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.ss_image)  
        h_layout.addWidget(self.ss_text) 

        self.data_layout.addLayout(h_layout)

        self.ss_info = QLabel(f"Damaging skills used in combat, consuming the user's silk. Each skill gives 1%.", self.app.main_widget)
        self.ss_info.setProperty("class", "header2")
        self.ss_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ss_info.setFont(self.app.font)

        self.data_layout.addWidget(self.ss_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(ss_data[1], 218)


    def return_abilities(self):
        a_data = self.DM.abilities_df()
        a_count = a_data[0]

        self.a_text = QLabel(f"Ancestral Arts ({a_count})", self.app.main_widget)
        self.a_text.setProperty("class", "header2")
        self.a_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.a_text.setFont(self.app.font)

        self.a_image = QLabel("", self.app.main_widget)
        self.a_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.a_image.setPixmap(self.IM.abilities_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.a_image)  
        h_layout.addWidget(self.a_text) 

        self.data_layout.addLayout(h_layout)

        self.a_info = QLabel(f"Special abilities, ranging from modifying mobility to enriching exploration. Each art gives 1%.", self.app.main_widget)
        self.a_info.setProperty("class", "header2")
        self.a_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.a_info.setFont(self.app.font)

        self.data_layout.addWidget(self.a_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(a_data[1], 370)

    
    def return_crests(self):
        c_data = self.DM.crests_df()
        c_count = c_data[0]

        self.c_text = QLabel(f"Crests ({c_count})", self.app.main_widget)
        self.c_text.setProperty("class", "header2")
        self.c_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.c_text.setFont(self.app.font)

        self.c_image = QLabel("", self.app.main_widget)
        self.c_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.c_image.setPixmap(self.IM.crests_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.c_image)  
        h_layout.addWidget(self.c_text) 

        self.data_layout.addLayout(h_layout)

        self.c_info = QLabel(f"Changes the user's moveset. Each crest (excluding Hunter) gives 1%.", self.app.main_widget)
        self.c_info.setProperty("class", "header2")
        self.c_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.c_info.setFont(self.app.font)

        self.data_layout.addWidget(self.c_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(c_data[1], 250)

    def return_simple_keys(self):
        sk_data = self.DM.simple_keys_df()
        sk_count = sk_data[0]

        self.sk_text = QLabel(f"Simple Keys ({sk_count})", self.app.main_widget)
        self.sk_text.setProperty("class", "header2")
        self.sk_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sk_text.setFont(self.app.font)

        self.sk_image = QLabel("", self.app.main_widget)
        self.sk_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sk_image.setPixmap(self.IM.simple_key_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.sk_image)  
        h_layout.addWidget(self.sk_text) 

        self.data_layout.addLayout(h_layout)

        self.sk_info = QLabel(f"Used to unlock further exploration.", self.app.main_widget)
        self.sk_info.setProperty("class", "header2")
        self.sk_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.sk_info.setFont(self.app.font)

        self.data_layout.addWidget(self.sk_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(sk_data[1], 159)

    def return_cylinders(self):
        pc_data = self.DM.cylinder_df()
        pc_count = pc_data[0]

        self.pc_text = QLabel(f"Psalm Cylinders ({pc_count})", self.app.main_widget)
        self.pc_text.setProperty("class", "header2")
        self.pc_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.pc_text.setFont(self.app.font)

        self.pc_image = QLabel("", self.app.main_widget)
        self.pc_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.pc_image.setPixmap(self.IM.cylinder_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.pc_image)  
        h_layout.addWidget(self.pc_text) 

        self.data_layout.addLayout(h_layout)

        self.pc_info = QLabel(f"Musical relics of Pharloom's past. Can be listened to when given to Vaultkeeper Cardinius.", self.app.main_widget)
        self.pc_info.setProperty("class", "header2")
        self.pc_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.pc_info.setFont(self.app.font)

        self.data_layout.addWidget(self.pc_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(pc_data[1], 218)


    def return_memory_lockets(self):
        ml_data = self.DM.memory_locket_df()
        ml_count = ml_data[0]

        self.ml_text = QLabel(f"Memory Lockets ({ml_count})", self.app.main_widget)
        self.ml_text.setProperty("class", "header2")
        self.ml_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ml_text.setFont(self.app.font)

        self.ml_image = QLabel("", self.app.main_widget)
        self.ml_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ml_image.setPixmap(self.IM.memory_locket_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.ml_image)  
        h_layout.addWidget(self.ml_text) 

        self.data_layout.addLayout(h_layout)

        self.ml_info = QLabel(f"Used to unlock tool slots for Crests.", self.app.main_widget)
        self.ml_info.setProperty("class", "header2")
        self.ml_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.ml_info.setFont(self.app.font)

        self.data_layout.addWidget(self.ml_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(ml_data[1], 639)

    def return_fleas(self):
        flea_data = self.DM.fleas_df()
        flea_count = flea_data[0]

        self.flea_text = QLabel(f"Lost Fleas ({flea_count})", self.app.main_widget)
        self.flea_text.setProperty("class", "header2")
        self.flea_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.flea_text.setFont(self.app.font)

        self.flea_image = QLabel("", self.app.main_widget)
        self.flea_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.flea_image.setPixmap(self.IM.flea_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.flea_image)  
        h_layout.addWidget(self.flea_text) 

        self.data_layout.addLayout(h_layout)

        self.flea_info = QLabel(f"Hidden critters that can be found and led to the Flea Caravan.", self.app.main_widget)
        self.flea_info.setProperty("class", "header2")
        self.flea_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.flea_info.setFont(self.app.font)

        self.data_layout.addWidget(self.flea_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(flea_data[1], 939)

    def return_tools(self):
        tool_data = self.DM.tools_df()
        tool_count = tool_data[0]

        self.tool_text = QLabel(f"Tools ({tool_count})", self.app.main_widget)
        self.tool_text.setProperty("class", "header2")
        self.tool_text.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.tool_text.setFont(self.app.font)

        self.tool_image = QLabel("", self.app.main_widget)
        self.tool_image.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.tool_image.setPixmap(self.IM.tool_icon[self.app.mode].scaled(90, 98, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)  
        h_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        h_layout.addWidget(self.tool_image)  
        h_layout.addWidget(self.tool_text) 

        self.data_layout.addLayout(h_layout)

        self.tool_info = QLabel(f"Trinkets to aid the user in combat, ranging from traps, passives, weapons, etc. Each tool gives 1%.", self.app.main_widget)
        self.tool_info.setProperty("class", "header2")
        self.tool_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.tool_info.setFont(self.app.font)

        self.data_layout.addWidget(self.tool_info, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.create_chart(tool_data[1], 1570)



    def create_chart(self, dataframe, fixed_height=33): # 33
        
        df = pandas.DataFrame(dataframe)

        class PandasModel(QAbstractTableModel):
            def __init__(self, data):
                super().__init__()
                self._data = data

            def rowCount(self, parent=None):
                return self._data.shape[0]

            def columnCount(self, parent=None):
                return self._data.shape[1]

            def data(self, index, role=Qt.ItemDataRole.DisplayRole):

                if not index.isValid():
                    return None
                

                col_name = self._data.columns[index.column()]
                value = self._data.iat[index.row(), index.column()]


                if role == Qt.ItemDataRole.DisplayRole:
                    if col_name == "Location" and value != "N/A":
                        return "<map-link>"
                    return str(value)
                
                if role == Qt.ItemDataRole.ForegroundRole:
                    if col_name == "Location" and value != "N/A":
                        return QColor("#2e2e2e")
                    
                if role == Qt.ItemDataRole.FontRole:
                    if col_name == "Location" and value != "N/A":
                        font = QFont()
                        font.setUnderline(True)
                        return font
                
                if role == Qt.ItemDataRole.TextAlignmentRole:
                    return Qt.AlignmentFlag.AlignCenter
                
                return None

            def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
                if role == Qt.ItemDataRole.DisplayRole:
                    if orientation == Qt.Orientation.Horizontal:
                        return str(self._data.columns[section])
                    else:
                        return str(self._data.index[section])
                return None
            
        class NoHoverDelegate(QStyledItemDelegate):
            def paint(self, painter, option, index):
                option.state &= ~QStyle.StateFlag.State_MouseOver
                option.state &= ~QStyle.StateFlag.State_Selected
                super().paint(painter, option, index)

       
        table = QTableView()
        table.setItemDelegate(NoHoverDelegate(table))
        table.setAlternatingRowColors(True)
        table.setProperty("class", "Data_Chart")
        table.horizontalHeader().setFont(self.app.font_bold)
        table.setFont(self.app.font_bold)
   
        
        model = PandasModel(df)
        table.setModel(model)
        
        table.setMouseTracking(True)

        table.verticalHeader().setVisible(False)
        table.setShowGrid(False)
        

        table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        table.setSelectionMode(QTableView.SelectionMode.NoSelection)    

        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        table.horizontalHeader().setSectionResizeMode(table.horizontalHeader().ResizeMode.Fixed)

        # Set fixed width and height
        for col in range(model.columnCount()):
            table.horizontalHeader().resizeSection(col, 200)
        
        total_width = 200 * model.columnCount()
        table.setMinimumWidth(total_width + 10)
    
        table.setMinimumHeight(fixed_height)
        table.setMaximumHeight(fixed_height)      

        table.setFrameShape(table.frameShape().NoFrame)

        container = QWidget()
        c_layout = QHBoxLayout()
        c_layout.setContentsMargins(0, 0, 0, 0)  
        c_layout.addWidget(table)
        container.setLayout(c_layout)

        def handle_click(index):
            if index.column() == df.columns.get_loc("Location"):
                url = df.iloc[index.row(), index.column()]
                if url != "N/A":
                    QDesktopServices.openUrl(QUrl(url))

        def on_enter(index):
            if index.column() == df.columns.get_loc("Location"):
                table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            else:
                table.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        
        def on_leave(event):
            table.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            return super(QTableView, table).leaveEvent(event)

        table.entered.connect(on_enter)

        table.leaveEvent = on_leave

        table.clicked.connect(handle_click)
        
        self.data_layout.addWidget(container,  alignment=Qt.AlignmentFlag.AlignHCenter)


    def reload_images(self):
        
        for t in self.fleurs:

            t[0].setPixmap(self.IM.fleurs[t[1]][self.app.mode])

        self.playtime_image.setPixmap(self.IM.clock_icon[self.app.mode].scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

            


        
        


    
    

    


