from PyQt6.QtGui import QPixmap

class ImageManager:

    def __init__(self):
        
        # preload images
        self.styles = ["default", "hornet", "title"]

        self.fleurs = {}

        for style in self.styles:
            self.fleurs[style] = (QPixmap(f"src/images/fleurs/fleur_{style}_gray.png"), QPixmap(f"src/images/fleurs/fleur_{style}_white.png"))
                                        
        
        self.health_icon = (QPixmap("src/images/icons/basic_data/heart_piece.png"), QPixmap("src/images/icons/basic_data/heart_piece.png")) # 32, 32

        self.theme_icon = (QPixmap("src/images/icons/settings/sun.png"), QPixmap("src/images/icons/settings/moon.png")) 

        self.clock_icon = (QPixmap("src/images/icons/basic_data/clock_gray.png"), QPixmap("src/images/icons/basic_data/clock_white.png"))

        self.silk_icon = (QPixmap("src/images/icons/basic_data/silk.png"), QPixmap("src/images/icons/basic_data/silk.png"))

        self.rosary_icon = (QPixmap("src/images/icons/basic_data/rosary_icon.png"), QPixmap("src/images/icons/basic_data/rosary_icon.png"))

        self.ss_icon = (QPixmap("src/images/icons/basic_data/shell_shards.png"), QPixmap("src/images/icons/basic_data/shell_shards.png"))

        self.silk_hearts = {}

        for i in range(4):
            self.silk_hearts[i] = (QPixmap(f"src/images/icons/var_data/silk_heart_{i}.png"), QPixmap(f"src/images/icons/var_data/silk_heart_{i}.png"))

        self.craftmetal_icon = (QPixmap("src/images/icons/advanced_data/craftmetal.png"), QPixmap("src/images/icons/advanced_data/craftmetal.png"))

        self.mask_shard_icon = (QPixmap("src/images/icons/advanced_data/mask_shard.png"), QPixmap("src/images/icons/advanced_data/mask_shard.png"))

        self.spool_fragment_icon = (QPixmap("src/images/icons/advanced_data/spool_fragment.png"), QPixmap("src/images/icons/advanced_data/spool_fragment.png"))

        self.nail_upgrade_icons = {}

        for i in range(5):
            self.nail_upgrade_icons[i] = (QPixmap(f"src/images/icons/var_data/nail_{i}.png"), QPixmap(f"src/images/icons/var_data/nail_{i}.png"))

        self.crafting_kit_icon = (QPixmap("src/images/icons/advanced_data/crafting_kit.png"), QPixmap("src/images/icons/advanced_data/crafting_kit.png"))

        self.tool_pouch_icon = (QPixmap("src/images/icons/advanced_data/tool_pouch.png"), QPixmap("src/images/icons/advanced_data/tool_pouch.png"))

        self.silk_skills_icon = (QPixmap("src/images/icons/advanced_data/silk_skills_icon.png"), QPixmap("src/images/icons/advanced_data/silk_skills_icon.png"))

        self.abilities_icon = (QPixmap("src/images/icons/advanced_data/abilities_icon.png"), QPixmap("src/images/icons/advanced_data/abilities_icon.png"))

        self.crests_icon = (QPixmap("src/images/icons/advanced_data/crests_icon.png"), QPixmap("src/images/icons/advanced_data/crests_icon.png"))

        self.simple_key_icon = (QPixmap("src/images/icons/advanced_data/simple_key.png"), QPixmap("src/images/icons/advanced_data/simple_key.png"))

        self.cylinder_icon = (QPixmap("src/images/icons/advanced_data/cylinder.png"), QPixmap("src/images/icons/advanced_data/cylinder.png"))

        self.memory_locket_icon = (QPixmap("src/images/icons/advanced_data/mem_locket.png"), QPixmap("src/images/icons/advanced_data/mem_locket.png"))

        self.flea_icon = (QPixmap("src/images/icons/advanced_data/flea_icon.png"), QPixmap("src/images/icons/advanced_data/flea_icon.png"))

        self.tool_icon = (QPixmap("src/images/icons/advanced_data/toolmaster.png"), QPixmap("src/images/icons/advanced_data/toolmaster.png"))

        self.steam_icon = (QPixmap("src/images/icons/links/steam_icon_dark.png"), QPixmap("src/images/icons/links/steam_icon_light.png"))

        self.github_icon = (QPixmap("src/images/icons/links/github_icon_dark.png"), QPixmap("src/images/icons/links/github_icon_light.png"))

        self.cherry_icon = (QPixmap("src/images/icons/links/cherry_icon_dark.png"), QPixmap("src/images/icons/links/cherry_icon_light.png"))
        

        