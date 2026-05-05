# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# ============================================
# Shop Prices Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QScrollArea, QFrame, QGroupBox, QPushButton, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, CardWidget, ScrollArea

# Import resource manager for images
from utils.resource_manager import ResourceManager
# Import shop price event functions for MP4
try:
    from events.marioParty6_items import itemsEvent_mp6DX, itemsEvent_mp6
except ImportError:
    pass


class ItemsMP6Tab(QWidget):
    def __init__(self, game_id, game_type="mp6"):
        super().__init__()
        self.game_id = game_id
        self.game_type = game_type  # "mp6" or "mp6dx"
        # Consistent column sizing for alignment
        self.icon_width = 32
        self.name_col_width = 140
        self.input_width = 60

        # Use dictionary to store widget references instead of dynamic attributes
        self.price_entries = {}

        self.setup_ui()

    def setup_ui(self):
        """Set up the shop prices tab UI"""
        self.setObjectName(f"{self.game_id}ItemsMP6Tab")
        
        # Set transparent background
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget#marioParty4ItemsMP6Tab { background: transparent; }")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Item Modifications")
        title.setAlignment(Qt.AlignCenter)
        self.apply_label_theme(title, "")
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Modify prices and weights for items at different game stages:")
        desc.setAlignment(Qt.AlignCenter)
        self.apply_label_theme(desc, "")
        layout.addWidget(desc)

        # Create scroll area for the shop interface
        scroll_area = ScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("ScrollArea { background: transparent; border: none; }")

        # Container widget for scroll area content
        container = QWidget()
        container.setStyleSheet("QWidget { background: transparent; }")
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(20, 16, 20, 16)
        container_layout.setSpacing(16)

        # Create shop modifications card
        shop_card = CardWidget()
        shop_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }")
        shop_card_layout = QVBoxLayout(shop_card)
        shop_card_layout.setContentsMargins(20, 16, 20, 16)
        shop_card_layout.setSpacing(16)

        # Add title to the card
        card_title = SubtitleLabel("Item Shop Prices")
        self.apply_label_theme(card_title, "font-size: 16px; margin-bottom: 8px;")
        shop_card_layout.addWidget(card_title)

        # Game version selection
        version_layout = QHBoxLayout()
        version_label = BodyLabel("Game Version:")
        self.apply_label_theme(version_label, "")
        version_layout.addWidget(version_label)

        # Create radio button group
        self.version_button_group = QButtonGroup()

        self.mp4_radio = QRadioButton("Mario Party 6")
        self.mp4dx_radio = QRadioButton("Mario Party 6 Deluxe")

        self.version_button_group.addButton(self.mp4_radio)
        self.version_button_group.addButton(self.mp4dx_radio)

        self.mp4_radio.setChecked(self.game_type == "mp6")
        self.mp4dx_radio.setChecked(self.game_type == "mp6dx")

        self.mp4_radio.clicked.connect(lambda: self.set_game_version("mp6"))
        self.mp4dx_radio.clicked.connect(lambda: self.set_game_version("mp6dx"))

        version_layout.addWidget(self.mp4_radio)
        version_layout.addWidget(self.mp4dx_radio)
        version_layout.addStretch()
        shop_card_layout.addLayout(version_layout)

        # Apply initial radio button styling
        self.update_radio_button_theme()

        # Create grid layout for item cards
        items_grid = QVBoxLayout()
        items_grid.setSpacing(12)

        # Create items based on game version
        dynamic_container = self.create_dynamic_content_container()
        items_grid.addWidget(dynamic_container)
        
        # Store reference to the items grid for later updates
        self.items_grid = items_grid

        shop_card_layout.addLayout(items_grid)
        container_layout.addWidget(shop_card)
        scroll_area.setWidget(container)
        layout.addWidget(scroll_area)

        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

        self.setLayout(layout)

    def set_game_version(self, version):
        """Set the game version (mp6 or mp6dx)"""
        self.game_type = version
        if version == "mp6":
            self.mp4_radio.setChecked(True)
            self.mp4dx_radio.setChecked(False)
        else:
            self.mp4_radio.setChecked(False)
            self.mp4dx_radio.setChecked(True)

        # Reapply theme styling to prevent palette glitches in dark mode
        self.update_radio_button_theme()
        
        # Update the items UI to reflect the new game version
        if hasattr(self, 'items_grid'):
            self.update_items_ui(self.items_grid)

    def clear_item_rows(self, scroll_layout):
        """Clear all items by replacing the dynamic content container"""
        # Find and remove the dynamic content container
        for i in range(scroll_layout.count()):
            item = scroll_layout.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                # Look for our dynamic content container (QWidget with object name)
                if hasattr(widget, 'objectName') and widget.objectName() == 'dynamic_content_container':
                    scroll_layout.removeWidget(widget)
                    widget.deleteLater()
                    break

        # Clear the price entries dictionary to prevent accumulation
        self.price_entries.clear()

    def create_dynamic_content_container(self):
        """Create a container widget for dynamic content"""
        container = QWidget()
        container.setObjectName('dynamic_content_container')
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(8)

        # Add the items
        self.create_version_items(container_layout)

        return container

    def update_min_coins_ui(self):
        """Update the min_coins UI based on current game version"""
        # Note: UI updates disabled for stability
        print(f"Min coins UI update requested for game type: {self.game_type}")

    def update_items_ui(self, scroll_layout):
        """Update the items UI based on current game version"""
        # Clear existing dynamic content
        self.clear_item_rows(scroll_layout)

        # Create new dynamic content container
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

    def create_column_header(self, parent_layout):
        """Create column header with clear labels"""
        header_layout = QHBoxLayout()
        header_layout.setSpacing(12)
        header_layout.setContentsMargins(10, 5, 10, 5)

        # Empty space for icon
        icon_placeholder = QLabel("")
        icon_placeholder.setFixedWidth(self.icon_width)
        header_layout.addWidget(icon_placeholder)

        # Price columns for different stages and player counts
        stages = ["Early Game", "Mid Game", "Late Game"]
        player_counts = ["1 Player", "2 Players", "3-4 Players"]

        for stage in stages:
            for player_count in player_counts:
                col_label = BodyLabel(f"{stage}\n{player_count}")
                col_label.setAlignment(Qt.AlignCenter)
                header_layout.addWidget(col_label)

        header_layout.addStretch()
        parent_layout.addLayout(header_layout)

        # Add a separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: palette(mid);")
        parent_layout.addWidget(separator)

    def create_item_row(self, parent_layout, item_name, item_icon):
        """Create a single card for an item"""
        # Create individual card for each item
        item_card = CardWidget()
        item_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); }")
        item_card_layout = QVBoxLayout(item_card)
        item_card_layout.setContentsMargins(16, 12, 16, 12)
        item_card_layout.setSpacing(8)

        # Item title
        title = BodyLabel(item_name)
        self.apply_label_theme(title, "font-size: 14px; margin-bottom: 4px;")
        item_card_layout.addWidget(title)

        # Parameters layout
        params_layout = QHBoxLayout()
        params_layout.setSpacing(16)

        # Add item icon
        icon = self.create_image_label(item_icon, 32, 32)
        params_layout.addWidget(icon)

        # Price inputs for different stages
        stages = ["Early", "Mid", "Late"]
        item_key = (
            item_name.lower()
            .replace(" ", "_")
            .replace("-", "_")
            .replace(".", "")
        )
        self.create_price_inputs_card(params_layout, item_key, stages)

        item_card_layout.addLayout(params_layout)
        parent_layout.addWidget(item_card)

    def create_price_inputs_card(self, layout, item_key, stages):
        """Create price input fields organized by category (Prices, Shop Odds, Space Odds)"""
        # Prices section - only player counts (1P, 2P, 34P) - skip for mushroom
        if item_key != "mushroom":
            prices_layout = QVBoxLayout()
            prices_layout.setSpacing(4)
            prices_label = BodyLabel("Prices:")
            self.apply_label_theme(prices_label, "font-size: 12px; font-weight: 600;")
            prices_layout.addWidget(prices_label)
            
            for player_count in ["1", "2", "34"]:
                entry = LineEdit()
                entry.setPlaceholderText(f"{player_count}P")
                entry.setFixedWidth(60)
                entry.setFixedHeight(30)
                entry.setObjectName(f"{item_key}_price_{player_count}")
                prices_layout.addWidget(entry)
                self.price_entries[f"{item_key}_price_{player_count}"] = entry
            
            layout.addLayout(prices_layout)
        
        # Shop Odds section - Early and Late
        shop_odds_layout = QVBoxLayout()
        shop_odds_layout.setSpacing(4)
        shop_odds_label = BodyLabel("Shop Odds:")
        self.apply_label_theme(shop_odds_label, "font-size: 12px; font-weight: 600;")
        shop_odds_layout.addWidget(shop_odds_label)
        
        for stage in ["Early", "Late"]:
            entry = LineEdit()
            entry.setPlaceholderText(stage)
            entry.setFixedWidth(60)
            entry.setFixedHeight(30)
            entry.setObjectName(f"{item_key}_shopodds_{stage.lower()}")
            shop_odds_layout.addWidget(entry)
            self.price_entries[f"{item_key}_shopodds_{stage.lower()}"] = entry
        
        layout.addLayout(shop_odds_layout)
        
        # Space Odds section - only player counts (1P, 2P, 34P)
        space_odds_layout = QVBoxLayout()
        space_odds_layout.setSpacing(4)
        space_odds_label = BodyLabel("Space Odds:")
        self.apply_label_theme(space_odds_label, "font-size: 12px; font-weight: 600;")
        space_odds_layout.addWidget(space_odds_label)
        
        for player_count in ["1", "2", "34"]:
            entry = LineEdit()
            entry.setPlaceholderText(f"{player_count}P")
            entry.setFixedWidth(60)
            entry.setFixedHeight(30)
            entry.setObjectName(f"{item_key}_spacedds_{player_count}")
            space_odds_layout.addWidget(entry)
            self.price_entries[f"{item_key}_spacedds_{player_count}"] = entry
        
        layout.addLayout(space_odds_layout)

    def create_price_inputs(self, layout, item_key, stages):
        """Create price input fields for different game stages (legacy method)"""
        for stage in stages:
            # Create inputs for player counts (1, 2, 3-4 players)
            for player_count in ["1", "2", "34"]:
                entry = LineEdit()

                # Leave fields blank - users can fill in custom values
                entry.setFixedWidth(self.input_width)
                entry.setObjectName(f"{item_key}_{stage.lower()}_{player_count}")
                # Let QFluentWidgets handle theme-aware styling automatically
                layout.addWidget(entry)

                # Store reference for later access using dictionary
                self.price_entries[f"{item_key}_{stage.lower()}_{player_count}"] = entry

    def create_image_label(self, image_path, width=32, height=32):
        """Create a QLabel with an image from the assets folder"""
        try:
            # Get the image path from resource manager
            image_path = ResourceManager.get_resource_path(image_path)

            # Create QLabel and set image
            image_label = QLabel()
            pixmap = QPixmap(str(image_path))

            if not pixmap.isNull():
                # Scale the image to the specified dimensions
                scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label.setPixmap(scaled_pixmap)
                image_label.setFixedSize(width, height)
                image_label.setAlignment(Qt.AlignCenter)
            else:
                # Fallback text if image fails to load
                image_label.setText("?")
                image_label.setFixedSize(width, height)
                image_label.setAlignment(Qt.AlignCenter)
                image_label.setStyleSheet("border: 1px solid gray; background: lightgray;")

            return image_label

        except Exception as e:
            # Fallback if image creation fails
            fallback_label = QLabel("?")
            fallback_label.setFixedSize(width, height)
            fallback_label.setAlignment(Qt.AlignCenter)
            fallback_label.setStyleSheet("border: 1px solid gray; background: lightgray;")
            return fallback_label

    def generate_codes(self):
        """Generate codes for the current game version"""
        try:
            # Note: min_coins functionality is not currently implemented in the backend
            # min_coins = self.min_coins_entry.text()

            # Collect all item prices
            item_prices = self.collect_item_prices()

            if self.game_type == "mp6dx":
                if 'itemsEvent_mp6DX' in globals():
                    # Call MP6DX function with collected parameters
                    itemsEvent_mp6DX(**item_prices)
                else:
                    self.show_error("Mario Party 6 Deluxe shop price modification not available")
            else:
                if 'itemsEvent_mp6' in globals():
                    # Call MP6 function with collected parameters
                    itemsEvent_mp6(**item_prices)
                else:
                    self.show_error("Mario Party 6 shop price modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def collect_item_prices(self):
        """Collect all item prices from the form"""
        prices = {}

        # Define separate mappings for MP6 and MP6DX
        mp6_item_mapping = {
            "mushroom": "mushroomCapsule",
            "golden_mushroom": "goldenMushroomCapsule",
            "slow_mushroom": "slowMushroomCapsule",
            "metal_mushroom": "metalMushroomCapsule",
            "bullet_bill": "cannonCapsule",
            "flutter": "flutterCapsule",
            "cursed_mushroom": "cursedMushroom",
            "spiny": "spinyCapsule",
            "goomba": "goombaCapsule",
            "piranha_plant": "piranhaPlantCapsule",
            "klepto": "kleptoCapsule",
            "toady": "toadyCapsule",
            "kamek": "kamekCapsule",
            "mr_blizzard": "mrBlizzardCapsule",
            "podoboo": "podobooCapsule",
            "zap": "banditCapsule",
            "tweester": "tweesterCapsule",
            "thwomp": "thwompCapsule",
            "warp_pipe": "bombCapsule",
            "bob_omb": "fireballCapsule",
            "paratroopa": "paraTroopaCapsule",
            "snack": "snackCapsule",
            "boo_away": "gaddLightCapsule"
        }

        mp6dx_item_mapping = {
            "mushroom": "mushroomCapsule",
            "golden_mushroom": "goldenMushroomCapsule",
            "slow_mushroom": "slowMushroomCapsule",
            "metal_mushroom": "metalMushroomCapsule",
            "bullet_bill": "cannonCapsule",
            "flutter": "flutterCapsule",
            "cursed_mushroom": "cursedMushroom",
            "spiny": "spinyCapsule",
            "goomba": "goombaCapsule",
            "piranha_plant": "piranhaPlantCapsule",
            "klepto": "kleptoCapsule",
            "toady": "toadyCapsule",
            "kamek": "kamekCapsule",
            "mr_blizzard": "mrBlizzardCapsule",
            "podoboo": "podobooCapsule",
            "zap": "banditCapsule",
            "tweester": "tweesterCapsule",
            "thwomp": "thwompCapsule",
            "warp_pipe": "bombCapsule",
            "bob_omb": "fireballCapsule",
            "paratroopa": "paraTroopaCapsule",
            "snack": "eggCapsule",
            "boo_away": "vacuumCapsule",
            # MP6DX exclusive items with "DxCapsule" prefix
            "duel": "DxCapsuleDuel",
            "chance_time": "DxCapsuleChance",
            "bowser": "DxCapsuleBowser",
            "donkey_kong": "DxCapsuleDonkeyKong",
            "pink_boo": "DxCapsulePinkBoo",
            "soluna": "DxCapsuleSoluna",
            "chain_chomp": "DxCapsuleChainChomp",
            "wacky_watch": "DxCapsuleWackyWatch"
        }

        # Get the appropriate item mapping based on game type
        if self.game_type == "mp6":
            item_list = list(mp6_item_mapping.keys())
            item_mapping = mp6_item_mapping
        else:  # MP6DX
            item_list = list(mp6dx_item_mapping.keys())
            item_mapping = mp6dx_item_mapping

        for item_key in item_list:
            if item_key in item_mapping:
                capsule_name = item_mapping[item_key]
                
                # Skip price collection for mushroom (no prices)
                if item_key != "mushroom":
                    # Collect price fields (1P, 2P, 34P)
                    for player_count in ["1", "2", "34"]:
                        entry_key = f"{item_key}_price_{player_count}"
                        if entry_key in self.price_entries:
                            entry = self.price_entries[entry_key]
                            value = entry.text().strip()
                            if value:  # Only add non-empty values
                                param_name = f"{capsule_name}Price{player_count}"
                                prices[param_name] = value
                
                # Collect shop odds fields (both MP6 and MP6DX use "12" and "34")
                for stage_key, stage_suffix in [("early", "12"), ("late", "34")]:
                    entry_key = f"{item_key}_shopodds_{stage_key}"
                    if entry_key in self.price_entries:
                        entry = self.price_entries[entry_key]
                        value = entry.text().strip()
                        if value:  # Only add non-empty values
                            param_name = f"{capsule_name}ShopOdds{stage_suffix}"
                            prices[param_name] = value
                
                # Collect space odds fields (1P, 2P, 34P)
                for player_count in ["1", "2", "34"]:
                    entry_key = f"{item_key}_spacedds_{player_count}"
                    if entry_key in self.price_entries:
                        entry = self.price_entries[entry_key]
                        value = entry.text().strip()
                        if value:  # Only add non-empty values
                            param_name = f"{capsule_name}SpaceOdds{player_count}"
                            prices[param_name] = value

        return prices

    def apply_label_theme(self, label, base_style=""):
        """Apply theme-aware styling to labels with explicit white text for dark mode"""
        from qfluentwidgets import isDarkTheme
        
        if isDarkTheme():
            # Dark theme - explicit white text
            color_style = "color: #ffffff;"
        else:
            # Light theme - dark text
            color_style = "color: #333333;"
        
        # Combine base style with color
        full_style = f"{base_style} {color_style}".strip()
        label.setStyleSheet(full_style)

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)

    def create_version_items(self, parent_layout):
        """Create items for the current game version"""
        if self.game_type == "mp6":
            # MP6 items only
            all_items = [
                ("Mushroom", "assets/items/mushroomCapsule.png"),
                ("Golden Mushroom", "assets/items/goldenMushroomCapsule.png"),
                ("Slow Mushroom", "assets/items/slowMushroomCapsule.png"),
                ("Metal Mushroom", "assets/items/metalMushroomCapsule.png"),
                ("Bullet Bill", "assets/items/bulletBillCapsule.png"),
                ("Flutter", "assets/items/wigglerCapsule.png"),
                ("Cursed Mushroom", "assets/items/cursedMushroomCapsule.png"),
                ("Spiny", "assets/items/spinyCapsule.png"),
                ("Goomba", "assets/items/goombaCapsule.png"),
                ("Piranha Plant", "assets/items/plantCapsule.png"),
                ("Klepto", "assets/items/kleptoCapsule.png"),
                ("Toady", "assets/items/toadyCapsule.png"),
                ("Kamek", "assets/items/kamekCapsule.png"),
                ("Mr. Blizzard", "assets/items/blizzardCapsule.png"),
                ("Podoboo", "assets/items/podobooCapsule.png"),
                ("Zap", "assets/items/zapCapsule.png"),
                ("Tweester", "assets/items/tweesterCapsule.png"),
                ("Thwomp", "assets/items/thwompCapsule.png"),
                ("Warp Pipe", "assets/items/warpCapsule.png"),
                ("Bob-omb", "assets/items/bombCapsule.png"),
                ("Paratroopa", "assets/items/paraTroopaCapsule.png"),
                ("Snack", "assets/items/snackCapsule.png"),
                ("Boo-away", "assets/items/gaddLightCapsule.png"),
            ]
        else:
            # MP4DX items (includes all MP4 items plus additional ones)
            all_items = [
                ("Mushroom", "assets/items/mushroomCapsule.png"),
                ("Golden Mushroom", "assets/items/goldenMushroomCapsule.png"),
                ("Slow Mushroom", "assets/items/slowMushroomCapsule.png"),
                ("Metal Mushroom", "assets/items/metalMushroomCapsule.png"),
                ("Bullet Bill", "assets/items/bulletBillCapsule.png"),
                ("Flutter", "assets/items/wigglerCapsule.png"),
                ("Cursed Mushroom", "assets/items/cursedMushroomCapsule.png"),
                ("Spiny", "assets/items/spinyCapsule.png"),
                ("Goomba", "assets/items/goombaCapsule.png"),
                ("Piranha Plant", "assets/items/plantCapsule.png"),
                ("Klepto", "assets/items/kleptoCapsule.png"),
                ("Toady", "assets/items/toadyCapsule.png"),
                ("Kamek", "assets/items/kamekCapsule.png"),
                ("Mr. Blizzard", "assets/items/blizzardCapsule.png"),
                ("Podoboo", "assets/items/podobooCapsule.png"),
                ("Zap", "assets/items/zapCapsule.png"),
                ("Tweester", "assets/items/tweesterCapsule.png"),
                ("Thwomp", "assets/items/thwompCapsule.png"),
                ("Warp Pipe", "assets/items/warpCapsule.png"),
                ("Bob-omb", "assets/items/bombCapsule.png"),
                ("Paratroopa", "assets/items/paraTroopaCapsule.png"),
                ("Snack", "assets/items/snackCapsule.png"),
                ("Boo-away", "assets/items/gaddLightCapsule.png"),
                ("Duel", "assets/items/duelCapsule.png"),
                ("Chance Time", "assets/items/chanceCapsule.png"),
                ("Bowser", "assets/items/bowserCapsule.png"),
                ("Donkey Kong", "assets/items/dkCapsule.png"),
                ("Pink Boo", "assets/items/pinkBooCapsule.png"),
                ("Soluna", "assets/items/solunaOrb.png"),
                ("Chain Chomp", "assets/items/chainChompCapsule.png"),
                ("Wacky Watch", "assets/items/wackyWatchOrb.png")
            ]

        # Create items using card-based layout
        for i, (item_name, item_icon) in enumerate(all_items):
            self.create_item_row(parent_layout, item_name, item_icon)

    def create_minimal_item(self, scroll_layout):
        """Create initial items based on the current game version"""
        # Create dynamic content container
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

    def themeChanged(self):
        """Called when theme changes - update all styling"""
        self.update_radio_button_theme()
        # Update CardWidget title theming
        if hasattr(self, 'scroll_area'):
            self.apply_scrollbar_theme(self.scroll_area)
        # QFluentWidgets LineEdit handles theme changes automatically
        # No manual styling needed

    def update_radio_button_theme(self):
        """Update radio button styling based on current theme"""
        from qfluentwidgets import isDarkTheme

        if isDarkTheme():
            # Dark theme styling for radio buttons
            radio_style = """
                QRadioButton {
                    background: transparent;
                    color: #ffffff;
                    font-size: 14px;
                    spacing: 8px;
                    padding: 4px;
                }
                QRadioButton::indicator {
                    width: 16px;
                    height: 16px;
                    border: 2px solid #666666;
                    border-radius: 8px;
                    background: #3c3c3c;
                }
                QRadioButton::indicator:checked {
                    background: #0078d4;
                    border: 2px solid #0078d4;
                }
                QRadioButton::indicator:hover {
                    border: 2px solid #999999;
                }
                QRadioButton::indicator:checked:hover {
                    background: #106ebe;
                    border: 2px solid #106ebe;
                }
            """
        else:
            # Light theme styling for radio buttons
            radio_style = """
                QRadioButton {
                    background: transparent;
                    color: #333333;
                    font-size: 14px;
                    font-weight: 500;
                    spacing: 8px;
                    padding: 4px;
                }
                QRadioButton::indicator {
                    width: 16px;
                    height: 16px;
                    border: 2px solid #cccccc;
                    border-radius: 8px;
                    background: #ffffff;
                }
                QRadioButton::indicator:checked {
                    background: #0078d4;
                    border: 2px solid #0078d4;
                }
                QRadioButton::indicator:hover {
                    border: 2px solid #999999;
                }
                QRadioButton::indicator:checked:hover {
                    background: #106ebe;
                    border: 2px solid #106ebe;
                }
            """

        # Apply the styling to radio buttons
        self.mp4_radio.setStyleSheet(radio_style)
        self.mp4dx_radio.setStyleSheet(radio_style)

    def apply_scrollbar_theme(self, scroll_area):
        """Apply themed styling to QScrollArea scrollbars (light/dark)"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            bar_style = """
                QScrollBar:vertical {
                    background: transparent;
                    width: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:vertical {
                    background: #5a5a5a;
                    min-height: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #7a7a7a;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar:horizontal {
                    background: transparent;
                    height: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:horizontal {
                    background: #5a5a5a;
                    min-width: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #7a7a7a;
                }
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }
            """
        else:
            bar_style = """
                QScrollBar:vertical {
                    background: transparent;
                    width: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:vertical {
                    background: #c4c4c4;
                    min-height: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #a0a0a0;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar:horizontal {
                    background: transparent;
                    height: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:horizontal {
                    background: #c4c4c4;
                    min-width: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #a0a0a0;
                }
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }
            """

        # Apply the style to both scrollbars
        try:
            scroll_area.verticalScrollBar().setStyleSheet(bar_style)
            scroll_area.horizontalScrollBar().setStyleSheet(bar_style)
        except Exception:
            pass
