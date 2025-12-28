
import copy
from .banner import banner
from typing import Any


class Dataframe_Manager:
    def __init__(self, save_data):

        self.save_data = save_data
        self.df_skeleton = {"Collected": [],
                            "Name": [],
                            "Act": [],
                            "Prerequisites": [],
                            "Location": []}
                            
        
        self.symbol_collected = "\u2705"

        self.symbol_missing = "\u274c"


    def silk_heart_df(self):
        dataframe = copy.deepcopy(self.df_skeleton)

        data_list = {"Scenes": ["Memory_Silk_Heart_BellBeast", "Memory_Silk_Heart_WardBoss", "Memory_Silk_Heart_LaceTower"],
                     "Acts": [1, 2, 2],
                     "Prerequisites": ["None", "None", "None"],
                     "Locations": ['477881', '479082', '479089']}

        sh_id = "glow_rim_Remasker"

        dataframe["Name"].extend(f"Silk Heart {i}" for i in range(1, 4))


        dataframe["Act"].extend(data_list["Acts"])

        dataframe["Prerequisites"].extend(data_list['Prerequisites'])

        dataframe["Location"].extend(data_list['Locations'])

        for scene in data_list["Scenes"]:  # check if flag exists
            
            if scene in self.save_data['playerData']['scenesVisited']: # flag exists, check if collected:

                for flag in self.save_data['sceneData']['persistentBools']['serializedList']:
                    if flag['SceneName'] == scene and flag['ID'] == sh_id: # flag found

                        dataframe["Collected"].append(self.symbol_collected if flag["Value"] else self.symbol_missing)
                            
            else:
                dataframe["Collected"].append(self.symbol_missing)

        return dataframe
    
    def craftmetal_df(self):
        
        cm_data_list = {"Scenes": ["PurchasedBonebottomToolMetal", "Bone_07", "Dock_03", "Coral_32",
                                "Under_19b", "MerchantEnclaveToolMetal", "Wisp_05", "Aqueduct_05"],

                        "SceneType": ["Generic", "Pickup", "Pickup", "Pickup", "Pickup", "Generic", "Pickup", "Pickup"],

                     "ID": ["None", "Collectable Item Pickup - Tool Metal", "Collectable Item Pickup", "Collectable Item Pickup - Tool Metal",
                            "Collectable Item Pickup - Tool Metal", "None", "Collectable Item Pickup - Tool Metal", "Collectable Item Pickup - Tool Metal"],
                     "Acts": [1, 1, 2, 2, 2, 2, 2, 2],
                     "Prerequisites": ["None", "None", "None", "Cling Grip", 
                                       "None", "None", "None", "Faydown Cloak"],
                     "Locations":['477838', '477894', '477937', '478541', '478711', '479250', '479157', '479139']
                     }
        
        return self.search_flags(cm_data_list, "Craftmetal")
    
    def mask_shard_df(self):

        ms_data_list = {"Scenes": ["PurchasedBonebottomHeartPiece", "Crawl_02", "Bone_East_20", "Shellwood_14", "Dock_08",
                                   "Weave_05b", "Beastfly Hunt", "Song_09", "Library_05", "Shadow_13",
                                   "Bone_East_LavaChallenge", "Slab_17", "Peak_04c", "Wisp_07", "MerchantEnclaveShellFragment",
                                   "Coral_19b", "Sprintmaster Race", "Ant Trapper", "Destroy Thread Cores", "Peak_06"],

                        "SceneType": ["Generic", "Pickup", "Pickup", "Pickup", "Pickup", 
                                      "Pickup", "Quest", "Pickup", "Pickup", "Pickup",
                                      "Pickup", "Pickup", "Pickup", "Pickup", "Generic",
                                      "Pickup", "Quest", "Quest", "Quest", "Pickup"],

                        "ID": ["None", "Heart Piece", "Heart Piece", "Heart Piece", "Heart Piece", 
                               "Heart Piece", "None", "Heart Piece", "Heart Piece", "Heart Piece",
                               "Heart Piece (1)", "Heart Piece", "Heart Piece", "Heart Piece", "None",
                               "Heart Piece", "None", "None", "None", "Heart Piece"],

                        "Acts": [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3],

                        "Prerequisites": ["None", "None", "Drifter's Cloak", "None", "Cling Grip", "Needolin", "None", "None", "None", "Clawline",
                                          "Clawline", "Key of Apostate", " Faydown Cloak", " Faydown Cloak", "None", "Faydown Cloak", "None", "None", "None", "Silk Soar"],

                        "Locations": ['477840', '478091', '477975', '478177', '477901', 
                                      '478233', '478800', '478615', '478671', '478849', 
                                      '478841', '479001', '479038', '479151', '478879', 
                                      '478498', '479194', '479447', '479449', '479460']}

        return self.search_flags(ms_data_list, "Mask Shard")
    
    def spool_fragments_df(self):

        sf_data_list = {"Scenes": ["Bone_11b", "Bone_East_13", "Greymoor_02", "Peak_01", "Weave_11",
                                   "PurchasedBelltownSpoolSegment", "MetCaravanTroupeLeaderGreymoor", "Cog_07", "Library_11b", "Song_19_entrance",
                                   "Under_10", "Ward_01", "Save Sherma", "Dock_03c", "Hang_03_top",
                                   "Arborium_09", "purchasedGrindleSpoolPiece", "MerchantEnclaveSpoolPiece"],

                        "SceneType": ["Pickup", "Pickup", "Pickup", "Pickup", "Pickup",
                                      "Generic", "Generic", "Pickup", "Pickup", "Pickup",
                                      "Pickup", "Pickup", "Quest", "Pickup", "Pickup",
                                      "Pickup", "Generic", "Generic"],

                        "ID": ["Silk Spool", "Silk Spool", "Silk Spool", "Silk Spool", "Silk Spool",
                               "None", "None", "Silk Spool", "Silk Spool", "Silk Spool",
                               "Silk Spool", "Silk Spool", "None", "Silk Spool", "Silk Spool",
                               "Silk Spool", "None", "None"],

                        "Acts": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 

                        "Prerequisites": ["None", "None", "Cling Grip", "Cling Grip", "Needolin",
                                          "Save Tipp", "14 Fleas Saved", "None", "None", "None",
                                          "None", "None", "Save Sherma", "None", "Clawline",
                                          "Faydown Cloak", "Faydown Cloak", "Faydown Cloak"],

                        "Locations": ['478080', '477926', '478263', '478475', '478230', 
                                      '478347', '478820', '478618', '478704', '478586', 
                                      '478931', '479317', '479180', '478825', '478909', 
                                      '479117', '478527', '479249']}


        return self.search_flags(sf_data_list, "Spool Fragment")
    

    def crafting_kit_upgrades_df(self):

        ck_data_list = {"Scenes": ["PurchasedForgeToolKit", "Crow Feathers", "purchasedGrindleToolKit", "PurchasedArchitectToolKit"],
                        "SceneType": ["Generic", "Quest", "Generic", "Generic"],
                        "ID": ["None", "None", "None", "None"],
                        "Acts": [1, 2, 2, 2],
                        "Prerequisites": ["None", "None", "Faydown Cloak", "Clawline"],
                        "Locations": ['477919', '478348', '478533', '478728']}


        return self.search_flags(ck_data_list, "Crafting Kit Upgrade")
    
    def tool_pouch_upgrades_df(self):

        tp_data_list = {"Scenes": ["PurchasedPilgrimsRestToolPouch", "pinGalleriesCompleted", "Journal", "CaravanTroupeLocation"],
                        "SceneType": ["Generic", "Generic", "Quest", "Generic"],
                        "ID": ["None", "None", "None", "None"],
                        "Acts": [1, 1, 1, 2],
                        "Prerequisites": ["None", "None", "None", "None"],
                        "Locations": ['477950', '478252', '479167', '479436']}


        return self.search_flags(tp_data_list, "Tool Pouch Upgrade")
    
    def nail_upgrades_df(self):

        nu_data_list = {"Scenes": ["PinsmithMetBelltown", "Library_03", "Great Gourmand", "Flea Games"],
                        
                        "SceneType": ["Generic", "Pickup", "Quest", "Quest"],

                        "ID": ["None", "Collectable Item Pickup", "None", "None"],

                        "Acts": [2, 2, 2, 3],

                        "Prerequisites": ["None", "None", "None", "None"],
                        
                        "Locations": ['478210', '478668', '479233', '479582']}


        return self.search_flags(nu_data_list, "Nail Upgrade")
    
    def silk_skills_df(self):
        
        ss_data_list = {"Scenes": ["Silk Spear", "Thread Sphere", "Parry", 
                                   "Silk Charge", "Silk Bomb", "Silk Boss Needle"],
                        "Names": ["Silkspear", "Thread Storm", "Cross Stitch",
                                  "Sharpdart", "Rune Rage", "Pale Nails"],
                        "Acts": [1, 1, 1, 2, 2, 3],
                        "Prerequisites": ["None", "None", "None", "None", "Clawline", "Silk Soar"],
                        "Locations": ['477871', '478061', '478371', '479079', '479025', '479606']}


        return self.search_tool_flags(ss_data_list, "Silk Skills")
    
    def abilities_df(self):

        a_data_list = {"Scenes": ["hasDash", "hasBrolly", "hasWalljump", "HasSeenNeedolin", "hasChargeSlash",
                                  "hasHarpoonDash", "hasDoubleJump", "hasSuperJump", "UnlockedFastTravelTeleport", "hasNeedolinMemoryPowerup",
                                  "HasBoundCrestUpgrader"],

                       "SceneType": ["Generic", "Generic", "Generic", "Generic", "Generic",
                                     "Generic", "Generic", "Generic", "Generic", "Generic",
                                     "Generic"],

                       "Names": ["Swift Step", "Drifter's Cloak", "Cling Grip", "Needolin", "Needle Strike",
                                 "Clawline", "Faydown Cloak", "Silk Soar", "Beastling Call", "Elegy of the Deep",
                                 "Sylphsong"],

                       "Acts": [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3],

                       "Prerequisites": ["None", "None", "None", "Cling Grip", "None",
                                         "Cling Grip", "Clawline", "None", "None", "None",
                                         "Bind Eva"],

                       "Locations": ['477915', '477971', '478189', '478199', '478510', 
                                     '478714', '479103', '479288', '479265', '479386', 
                                     '479654']}
        
        return self.search_flags(a_data_list, "Ability")
    

    def crests_df(self):
        
        c_data_list = {"Scenes": ["Hunter", "Warrior", "Reaper", "Wanderer",
                                  "Toolmaster", "Witch", "Spell"],
                       "Names": ["Hunter Crest", "Beast Crest", "Reaper Crest", "Wanderer Crest",
                                 "Architect Crest", "Witch Crest", "Shaman Crest"],
                       "Acts": [1, 1, 1, 1, 2, 2, 3],
                       "Prerequisites": ["None", "Drifter's Cloak", "None", "Simple Key", "Architect's Key", "Clawline", "Silk Soar"],
                       "Locations": ['000000', '478020', '478156', '478240', '478745', '478815', '479384']}
        
        return self.search_crest_flags(c_data_list, "Crest")
    

    def simple_keys_df(self):

        sk_data_list = {"Scenes": ["PurchasedBonebottomFaithToken", "CollectedDustCageKey",
                                   "MerchantEnclaveSimpleKey", "Bellshrine_Coral"],
                        "SceneType": ["Generic", "Generic", "Generic", "Pickup"],
                        "ID": ["None", "None", "None", "Collectable Item Pickup"],
                        "Acts": [1, 1, 2, 2],
                        "Prerequisites": ["None", "Cling Grip", "None", "Clawline"],
                        "Locations": ['477839', '478280', '478880', '479215']}

        return self.search_flags(sk_data_list, "Simple Key")
    

    def cylinder_df(self):

        pc_data_list = {"Scenes": ["Librarian Melody Cylinder", "Psalm Cylinder Librarian", "Psalm Cylinder Library Roof",
                                   "Psalm Cylinder Grindle", "Psalm Cylinder Ward", "Psalm Cylinder Hang"],
                        "Acts": [2, 2, 2, 2, 2, 2],
                        "Prerequisites": ["None", "Cling Grip", "Drifter's Cloak", "Faydown Cloak", "None", "None"],
                        "Locations": ['479717', '478650', '478774', '478530', '478929', '478908']}
        
        return self.search_relic_flags(pc_data_list, "Psalm Cylinder")
    
    def memory_locket_df(self):

        ml_data_list = {'Scenes': ['Rock Rollers', 'Bone_18', 'Crawl_09', 'Dock_13', 'PurchasedPilgrimsRestMemoryLocket', 
                                   'Ant_20', 'Greymoor_16', 'Halfway_01', 'PurchasedBelltownMemoryLocket', 'Coral_02', 
                                   'Slab_Cell_Quiet', 'Shadow_20', 'Shadow_27', 'Coral_23', 'Under_08', 
                                   'Bellway_City', 'Library_08', 'Arborium_05', 'Bone_East_25', 'Belltown'], 

                        'SceneType': ['Quest', 'Pickup', 'Pickup', 'Pickup', 'Generic', 
                                      'Pickup', 'Pickup', 'Pickup', 'Generic', 'Pickup', 
                                      'Pickup', 'Pickup', 'Pickup', 'Pickup', 'Pickup', 
                                      'Pickup', 'Pickup', 'Pickup', 'Pickup', 'Pickup'], 

                        'ID': ['None', 'Collectable Item Pickup', 'Collectable Item Pickup', 'Collectable Item Pickup', 'None', 
                               'Collectable Item Pickup', 'Collectable Item Pickup', 'Collectable Item Pickup', 'None', 'Collectable Item Pickup (1)', 
                               'Collectable Item Pickup', 'Collectable Item Pickup', 'Sack Corpse Pickup', 'Collectable Item Pickup', 'Collectable Item Pickup', 
                               'Collectable Item Pickup', 'Collectable Item Pickup', 'Collectable Item Pickup', 'Collectable Item Pickup', 'Collectable Item Pickup'], 

                        'Acts': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3], 
                        
                        'Prerequisites': ['None', 'Cling Grip', 'None', 'Simple Key', 'None', 
                                          'None', 'None', 'Faydown Cloak', 'None', 'None', 
                                          'None', 'None', 'None', 'Clawline', 'None', 
                                          'None', 'None', 'Faydown Cloak', 'None', 'Silk Soar'], 

                        'Locations': ['478222', '478246', '478493', '478836', '477953', 
                                      '478017', '478035', '478039', '478204', '478502', 
                                      '479017', '478787', '478851', '479204', '478571', 
                                      '478372', '478676', '479110', '479196', '478212']}
        
        return self.search_flags(ml_data_list, "Memory Locket")
    

    def fleas_df(self):
        
        flea_data_list = {"Scenes": ["SavedFlea_Bone_06", "SavedFlea_Dock_16", "SavedFlea_Bone_East_05", "SavedFlea_Bone_East_17b", "SavedFlea_Ant_03",
                                     "SavedFlea_Greymoor_15b", "SavedFlea_Greymoor_06", "SavedFlea_Shellwood_03", "SavedFlea_Bone_East_10_Church", "SavedFlea_Coral_35",
                                     "SavedFlea_Dust_12", "SavedFlea_Dust_09", "SavedFlea_Belltown_04", "SavedFlea_Crawl_06", "SavedFlea_Slab_Cell",
                                     "SavedFlea_Shadow_28", "SavedFlea_Dock_03d", "SavedFlea_Under_23", "SavedFlea_Shadow_10", "SavedFlea_Song_14",
                                     "SavedFlea_Coral_24", "SavedFlea_Peak_05c", "CaravanLechSaved", "SavedFlea_Library_09", "SavedFlea_Song_11", "SavedFlea_Library_01",
                                     "SavedFlea_Under_21", "SavedFlea_Slab_06", "tamedGiantFlea", "MetTroupeHunterWild"],
                          
                          "SceneType": ["Generic", "Generic", "Generic", "Generic", "Generic",
                                        "Generic", "Generic", "Generic", "Generic", "Generic",
                                        "Generic", "Generic", "Generic", "Generic", "Generic",
                                        "Generic", "Generic", "Generic", "Generic", "Generic",
                                        "Generic", "Generic", "Generic", "Generic", "Generic",
                                        "Generic", "Generic", "Generic", "Generic", "Generic"],

                          "Names": ["Lost Flea 1", "Lost Flea 2", "Lost Flea 3", "Lost Flea 4", "Lost Flea 5",
                                        "Lost Flea 6", "Lost Flea 7", "Lost Flea 8", "Lost Flea 9", "Lost Flea 10",
                                        "Lost Flea 11", "Lost Flea 12", "Lost Flea 13", "Lost Flea 14", "Lost Flea 15",
                                        "Lost Flea 16", "Lost Flea 17", "Lost Flea 18", "Lost Flea 19", "Lost Flea 20",
                                        "Lost Flea 21", "Lost Flea 22",  "Lost Flea 23 (Kratt)", "Lost Flea 24", "Lost Flea 25", "Lost Flea 26",
                                        "Lost Flea 27", "Lost Flea 28", "Lost Flea 29 (Giant Flea)", "Lost Flea 30 (Vog)"],
                            
                          "Acts": [1, 1, 1, 1, 1,
                                   1, 1, 1, 1, 1,
                                   1, 1, 1, 1, 1,
                                   1, 1, 1, 1, 2,
                                   1, 1, 2, 2, 2, 
                                   2, 2, 2, 2, 2],

                          "Prerequisites": ["None", "None", "Swift Step", "None", "None",
                                            "None", "None", "None", "Cling Grip", "None",
                                            "None", "None", "Cling Grip", "None", "Key of Indolent",
                                            "None", "Clawline", "None", "None", "None",
                                            "Cling Grip", "Cling Grip", "None", "Clawline", "None", "Clawline",
                                            "None", "Faydown Cloak", "None", "None"],

                          "Locations": ['477890', '477907', '477916', '477940', '477999', 
                                        '478145', '478287', '478176', '478219', '478385', 
                                        '478360', '478378', '478193', '478450', '478393', 
                                        '478443', '478437', '478419', '478408', '478398', 
                                        '478386', '478380', '478271', '478404', '478416', 
                                        '478402', '478420', '478392', '478413', '479138']}
        
        return self.search_flags(flea_data_list, "Flea")
    
    def tools_df(self):

        tools_data_list = {

        'Scenes': ['Bone Necklace', 'Compass', ('Mosscreep Tool 1', 'Mosscreep Tool 2'), 'Straight Pin', 'Bell Bind', 
                    'Tri Pin', 'Harpoon', ('Dead Mans Purse', 'Shell Satchel'), 'Rosary Magnet', 'Lava Charm', 
                    'Flea Brew', 'Barbed Wire', 'Tack', 'Pimpilo', 'White Ring', 
                    'Flintstone', 'Sprintmaster', 'Screw Attack', 'Poison Pouch', 'Lifeblood Syringe', 
                    'Thief Charm', 'Weighted Anklet', 'Fractured Mask', 'Sting Shard', ('Curve Claws', 'Curve Claws Upgraded'), 
                    'Multibind', 'Thief Claw', 'Magnetite Dice', 'Quickbind', 'Wallcling', 
                    'Revenge Crystal', 'Conch Drill', 'Quick Sling', 'Wisp Lantern', 'Cogwork Flier', 
                    'Rosary Cannon', 'Maggot Charm', 'Reserve Bind', 'Longneedle', 'Shakra Ring', 
                    'Scuttlebrace', 'Zap Imbuement', ('WebShot Forge', 'WebShot Architect', 'WebShot Weaver'), 'Musician Charm', 'Spool Extender', 
                    'Cogwork Saw', 'Brolly Spike', ('Dazzle Bind', 'Dazzle Bind Upgraded'), 'Lightning Rod', 'Flea Charm', 
                    'Pinstress Tool'],

        'Names': ['Shard Pendant', 'Compass', "Druid's Eye(s)", 'Straight Pin', 'Warding Bell', 
                  'Threefold Pin', 'Longpin', "DBP/Shell Satchel", 'Magnetite Brooch', 'Magma Bell', 
                  'Flea Brew', 'Barbed Bracelet', 'Tacks', 'Pimpilo', 'Weavelight', 
                  'Flintslate', 'Silkspeed Anklets', "Delver's Drill", 'Pollip Pouch', 'Plasmium Phial', 
                  "Thief's Mark", 'Weighted Belt', 'Fractured Mask', 'Sting Shard', 'Curveclaw/Curvesickle', 
                  'Multibinder', 'Snitch Pick', 'Magnetite Dice', 'Injector Band', "Ascendant's Grip", 
                  'Memory Crystal', 'Conchcutter', 'Quick Sling', 'Wispfire Lantern', 'Cogfly', 
                  'Rosary Cannon', 'Wreath of Purity', 'Reserve Bind', 'Longclaw', 'Throwing Ring', 
                  'Scuttlebrace', 'Volt Filament', 'Silkshot', 'Spider Strings', 'Spool Extender', 
                  'Cogwork Wheel', 'Sawtooth Circlet', 'Claw Mirror(s)', 'Voltvessels', 'Egg of Flealia', 
                  'Pin Badge'], 

        'Acts': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], 

        'Prerequisites': ['None', 'None', '3 Mossberries', 'Release Grindle', 'None', 
                          'None', 'None', 'None', 'None', 'None', 
                          'None', 'None', 'None', 'Cling Grip', 'None', 
                          'None', 'Needolin', 'None', 'None', 'None', 
                          'None', 'None', 'None', 'None', 'None', 
                          'None', 'None', 'None', 'None', 'None', 
                          'None', 'None', 'None', 'None', 'Craftmetal', 
                          'Simple Key', 'None', 'None', 'None', 'None', 
                          'None', 'None', 'Craftmetal', 'None', 'None', 
                          'None', 'None', 'None', 'None', 'Save All Fleas', 
                          'None'], 
                          
        'Locations': ['477848', '477851', '478255', '477899', '477935', 
                      '478058', '478158', '479081', '477841', '477918', 
                      '478025', '478341', '478365', '478964', '479070', 
                      '477986', '478216', '478577', '478294', '478496', 
                      '478525', '477947', '478607', '477917', '478604', 
                      '478345', '479201', '479309', '479182', '478878', 
                      '478947', '479230', '478848', '479156', '478903', 
                      '478937', '479133', '479254', '479240', '479242', 
                      '478727', '479224', '479497', '479248', '478881', 
                      '478725', '478726', '478691', '479121', '479439', 
                      '479466']}

       
        
        return self.search_tool_flags(tools_data_list, "Tool")
    
    def bosses_df(self):

        bosses_data_list = {"Scenes": ['defeatedMossMother', 'defeatedBellBeast', 'defeatedLace1', 'defeatedSongGolem', 'defeatedBoneFlyerGiant', 
                                       'defeatedSplinterQueen', 'skullKingDefeated', 'skullKingKilled', 'defeatedVampireGnatBoss', 'Roof Crab', 
                                       'visitedBellhartSaved', 'Moss Mother', 'defeatedBoneFlyerGiantGolemScene', 'defeatedCoralDrillers', 'defeatedLastJudge', 
                                       'defeatedPhantom', 'defeatedCogworkDancers', 'defeatedTrobbio', 'Garmond_Zaza', 'Dock Guard Thrower', 
                                       'wardBossDefeated', 'defeatedRoachkeeperChef', 'defeatedWispPyreEffigy', 'DefeatedSwampShaman', 'defeatedZapCoreEnemy', 
                                       'defeatedCoralDrillerSolo', 'defeatedFirstWeaver', 'defeatedBroodMother', 'defeatedSongChevalierBoss', 'Shakra', 
                                       'defeatedLaceTower', 'Silk Boss', 'Giant Centipede', 'Moss Mother', 'garmondBlackThreadDefeated', 
                                       'Crawfather', 'BlueScientistDead', 'Coral Warrior Grey', 'defeatedWhiteCloverstag', 'defeatedCloverDancers', 
                                       'defeatedAntTrapper', 'defeatedTormentedTrobbio', 'PinstressPeakBattleAccepted', 'defeatedSeth', 'defeatedFlowerQueen', 
                                       'defeatedAntQueen', 'defeatedCoralKing', 'Lost Lace', 'Abyss Mass']
,
                            "SceneType": ['Generic', 'Generic', 'Generic', 'Generic', 'Generic', 
                                          'Generic', 'Generic', 'Generic', 'Generic', 'Journal', 
                                          'Generic', 'Journal', 'Generic', 'Generic', 'Generic', 
                                          'Generic', 'Generic', 'Generic', 'Journal', 'Journal', 
                                          'Generic', 'Generic', 'Generic', 'Generic', 'Generic', 
                                          'Generic', 'Generic', 'Generic', 'Generic', 'Journal', 
                                          'Generic', 'Journal', 'Journal', 'Journal', 'Generic', 
                                          'Journal', 'Generic', 'Journal', 'Generic', 'Generic', 
                                          'Generic', 'Generic', 'Generic', 'Generic', 'Generic', 
                                          'Generic', 'Generic', 'Journal', 'Journal'],

                            "Names": ['Moss Mother (1/3)', 'Bell Beast', 'Lace (1/2)', 'Fourth Chorus', 'Savage Beastfly (1/2)', 
                                      'Sister Splinter', 'Skull Tyrant (1/2)', 'Skull Tyrant (2/2)', 'Moorwing', 'Craggler', 
                                      'Widow', 'Moss Mother (2/3)', 'Savage Beastfly (2/2)', 'Great Conchflies', 'Last Judge', 
                                      'Phantom', 'Cogwork Dancers', 'Trobbio', 'Garmond and Zaza', 'Signis and Gron', 
                                      'The Unravelled', 'Disgraced Chef Lugoli', 'Father Of The Flame', 'Groal the Great', 'Voltvyrm', 
                                      'Raging Conchfly', 'First Sinner', 'Broodmother', 'Second Sentinel', 'Shakra', 
                                      'Lace (2/2)', 'Grand Mother Silk', 'Bell Eater', 'Moss Mother (3/3)', 'Lost Garmond', 
                                      'Crawfather', 'Plasmified Zango', 'Watcher At the Edge', 'Palestag', 'Clover Dancers', 
                                      'Gurr The Outcast', 'Tormented Trobbio', 'Pinstress', 'Shrine Guardian Seth', 'Nyleth', 
                                      'Skarrsinger Karmelita', 'Crust King Khann', 'Lost Lace', 'Summoned Saviour'],

                            "Acts": ['1', '1', '1', '1', '1', 
                                     '1', '1', '2', '1', '2', 
                                     '1', '1', '2', '1', '1', 
                                     '1', '2', '2', '2', '2', 
                                     '2', '2', '2', '2', '3', 
                                     '2', '2', '2', '2', '2', 
                                     '2', '2', '3', '3', '3', 
                                     '3', '3', '3', '3', '3', 
                                     '3', '3', '3', '3', '3', 
                                     '3', '3', '3', '3'],

                            "Prerequisites": ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 
                                              'N/A', 'N/A', 'N/A', 'N/A'],

                            "Locations": ['476904', '477879', '476915', '477978', '478844', 
                                          '478137', '478136', '479655', '478453', '478088', 
                                          '478138', '478440', '478019', '478506', '478545', 
                                          '478370', '478606', '478690', '479361', '478831', 
                                          '480354', '478992', '479155', '478861', '479223', 
                                          '479227', '479023', '479255', '479253', '479822', 
                                          '479088', '479099', '479264', '481810', '479452', 
                                          '479578', '479273', '480326', '479408', '479427', 
                                          '479467', '479377', '479464', '479401', '479404', 
                                          '479198', '479392', '479471', '479740']}
        
        return self.search_flags(bosses_data_list, "Boss")


    def search_flags(self, data_list: dict[str, Any], name):

        dataframe = copy.deepcopy(self.df_skeleton)

        dataframe["Act"].extend(data_list["Acts"])

        dataframe["Prerequisites"].extend(data_list['Prerequisites'])

        dataframe["Location"].extend(data_list['Locations'])

        for i in range(len(data_list["Scenes"])):  # check if flag exists
            flag_found = False
            dataframe["Name"].append(f"{name} {i + 1}" if "Names" not in data_list.keys() else data_list["Names"][i])
            
            if data_list["Scenes"][i] in self.save_data['playerData']['scenesVisited']:

                for flag in self.save_data['sceneData']['persistentBools']['serializedList']:
                    if flag['SceneName'] == data_list["Scenes"][i] and flag['ID'] == data_list["ID"][i]: # flag found

                        dataframe["Collected"].append(self.symbol_collected if flag["Value"] else self.symbol_missing)
                        flag_found = True
                        break
                if not flag_found:
                    dataframe["Collected"].append(self.symbol_missing)
                            
            else:
                if data_list["SceneType"][i] == "Generic" and data_list["Scenes"][i] == "CaravanTroupeLocation":
                    dataframe["Collected"].append(self.symbol_collected if self.save_data['playerData'][data_list["Scenes"][i]] == 3 else self.symbol_missing)

                elif data_list["SceneType"][i] == "Generic":
                    if self.save_data['playerData'][data_list["Scenes"][i]]:
                        
                        dataframe["Collected"].append(self.symbol_collected)
                    else:
                        dataframe["Collected"].append(self.symbol_missing)

                elif data_list["SceneType"][i] == "Quest":
                    for quest in self.save_data['playerData']['QuestCompletionData']['savedData']:
                        if quest['Name'] == data_list["Scenes"][i]:
                            if quest['Data']['IsCompleted']:
                    
                                dataframe["Collected"].append(self.symbol_collected)
                                flag_found = True
                                break

                elif data_list["SceneType"][i] == "Journal":
                    for entry in self.save_data['playerData']['EnemyJournalKillData']['list']:
                        if entry['Name'] == data_list["Scenes"][i]:
                            dataframe["Collected"].append(self.symbol_collected)
                            flag_found = True
                            break
                        
                    if not flag_found:
                            dataframe["Collected"].append(self.symbol_missing)
                                
                else:
                    
                    dataframe["Collected"].append(self.symbol_missing)

            
            

        item_count = self.return_item_count(dataframe)

  


        return (item_count, dataframe)
    
    
    def search_tool_flags(self, data_list: dict[str, Any], name):

        dataframe = copy.deepcopy(self.df_skeleton)

        dataframe["Act"].extend(data_list["Acts"])

        dataframe["Prerequisites"].extend(data_list['Prerequisites'])

        dataframe["Location"].extend(data_list['Locations'])

     

        for i in range(len(data_list["Scenes"])):
            flag_found = False
            dataframe["Name"].append(f"{name} {i + 1}" if "Names" not in data_list.keys() else data_list["Names"][i])

            for flag in self.save_data['playerData']['Tools']['savedData']:

                if isinstance(data_list["Scenes"][i], tuple): # upgradable tool
                    
                    for tool_name in data_list["Scenes"][i]:

                        if flag['Name'] == tool_name:

                            dataframe["Collected"].append(self.symbol_collected if flag['Data']['IsUnlocked'] else self.symbol_missing)
                            flag_found = True
                            break
                if flag_found:
                    break

                elif flag['Name'] == data_list["Scenes"][i]:

                    dataframe["Collected"].append(self.symbol_collected if flag['Data']['IsUnlocked'] else self.symbol_missing)
                    flag_found = True
                    break

            if not flag_found:
                dataframe["Collected"].append(self.symbol_missing)

           

        item_count = self.return_item_count(dataframe)

   

        return (item_count, dataframe)
    

    def search_crest_flags(self, data_list: dict[str, Any], name):

        dataframe = copy.deepcopy(self.df_skeleton)

        dataframe["Act"].extend(data_list["Acts"])

        dataframe["Prerequisites"].extend(data_list['Prerequisites'])

        dataframe["Location"].extend(data_list['Locations'])


        for i in range(len(data_list["Scenes"])):
            flag_found = False
            dataframe["Name"].append(f"{name} {i + 1}" if "Names" not in data_list.keys() else data_list["Names"][i])
            for flag in self.save_data['playerData']['ToolEquips']['savedData']:

                if flag['Name'] == data_list["Scenes"][i]:

                    dataframe["Collected"].append(self.symbol_collected if flag['Data']['IsUnlocked'] else self.symbol_missing)
                    flag_found = True
                    break
            if not flag_found:
                dataframe["Collected"].append(self.symbol_missing)

        item_count = self.return_item_count(dataframe)

   

        return (item_count, dataframe)
    

    def search_relic_flags(self, data_list: dict[str, Any], name):

        dataframe = copy.deepcopy(self.df_skeleton)

        dataframe["Act"].extend(data_list["Acts"])

        dataframe["Prerequisites"].extend(data_list['Prerequisites'])

        dataframe["Location"].extend(data_list['Locations'])

      

        for i in range(len(data_list["Scenes"])):
            flag_found = False
            dataframe["Name"].append(f"{name} {i + 1}" if "Names" not in data_list.keys() else data_list["Names"][i])
            for flag in self.save_data['playerData']['Relics']['savedData']:

                if flag['Name'] == data_list["Scenes"][i]:

                    dataframe["Collected"].append(self.symbol_collected if flag['Data']['IsCollected'] else self.symbol_missing)
                    flag_found = True
                    break
            if not flag_found:
                dataframe["Collected"].append(self.symbol_missing)

         

        item_count = self.return_item_count(dataframe)

        return (item_count, dataframe)
    
    
    def return_item_count(self, dataframe):
        return f"{len([i for i in dataframe["Collected"] if i == self.symbol_collected])}/{len(dataframe["Collected"])}" 
    

        
