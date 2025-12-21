# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

import os
import platform
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QApplication
from PyQt5.QtCore import Qt, QTimer, QSettings, QPoint
from PyQt5.QtGui import QIcon, QKeySequence, QKeyEvent

from qfluentwidgets import FluentWindow, setTheme, Theme

# Import dark mode detection
try:
    import darkdetect
    DARKDETECT_AVAILABLE = True
except ImportError:
    DARKDETECT_AVAILABLE = False
    print("⚠️  darkdetect not available, using default light theme")

from utils.resource_manager import ResourceManager
from utils.scale_manager import ScaleManager


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        # Store scale factor for reference
        self.scale_factor = ScaleManager.get_scale_factor()
        self.setup_window()
        self.setup_theme()
        self.setup_theme_monitoring()
        self.oldPos = None
        self.corner_lock_enabled = True  # Enable corner snapping by default

    def setup_window(self):
        """Set up the main window properties"""
        self.setWindowTitle("Mario Party Toolkit")
        self.setWindowIcon(ResourceManager.get_icon("assets/icons/diceBlock.png"))
        
        # Get the available screen geometry
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        
        # Set minimum size
        self.setMinimumSize(1200, 800)
        
        # Fit to display - use available screen size with small margins
        margin = 200  # Leave some margin from screen edges
        window_width = screen_geometry.width() - (margin * 2)
        window_height = screen_geometry.height() - (margin * 2)
        
        # Set the window size to fit the display
        self.resize(window_width, window_height)
        
        # Center the window on screen
        self.move(
            screen_geometry.x() + margin,
            screen_geometry.y() + margin
        )
        
        print(f"✓ Window fitted to display: {window_width}x{window_height}")
        
        if self.scale_factor != 1.0:
            print(f"✓ Content scaled to {int(self.scale_factor * 100)}% for optimal fit")
        
        # Enable proper window dragging and resizing
        if platform.system() in ['Linux', 'Darwin']:  # Linux or macOS
            self.setWindowFlags(Qt.Window)
        else:  # Windows
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
        
        # Set size policy for proper scaling and resizing
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Ensure window is resizable (not fixed size)
        # Window is resizable by default, but we explicitly ensure it
        
        # Enable window dragging
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.setAttribute(Qt.WA_NoSystemBackground, False)
        
        # Load corner lock preference
        settings = QSettings("Mario Party Toolkit", "Settings")
        self.corner_lock_enabled = settings.value("corner_lock_enabled", True, type=bool)
        
        print(f"✓ Window resizing enabled")
        print(f"✓ Corner snapping {'enabled' if self.corner_lock_enabled else 'disabled'} (drag window near corner to snap)")

    def load_theme_preference(self):
        """Load theme preference from registry/settings"""
        settings = QSettings("Mario Party Toolkit", "Settings")
        # Default to system theme if no preference is saved
        saved_theme = settings.value("theme", "system")
        
        if saved_theme == "dark":
            return Theme.DARK
        elif saved_theme == "light":
            return Theme.LIGHT
        else:  # system or any other value
            # Use system theme as default
            if DARKDETECT_AVAILABLE:
                try:
                    return Theme.DARK if darkdetect.isDark() else Theme.LIGHT
                except Exception:
                    return Theme.LIGHT
            else:
                return Theme.LIGHT

    def setup_theme(self):
        """Set the initial theme based on saved preference"""
        try:
            # Load saved theme preference
            theme = self.load_theme_preference()
            setTheme(theme)
            
            # Apply title bar styling after setting theme
            self.apply_title_bar_style()
            
            # Use QTimer to apply styling again after window is fully initialized
            QTimer.singleShot(100, self.apply_title_bar_style)
            
            if theme == Theme.DARK:
                print("✓ Dark theme applied (saved preference)")
            else:
                print("✓ Light theme applied (saved preference)")
                
        except Exception as e:
            print(f"⚠️  Error loading theme preference: {e}, using light theme")
            setTheme(Theme.LIGHT)
            self.apply_title_bar_style()
            QTimer.singleShot(100, self.apply_title_bar_style)

    def setup_theme_monitoring(self):
        """Setup monitoring for theme changes"""
        if DARKDETECT_AVAILABLE:
            try:
                # Create a timer to check for theme changes
                self.theme_timer = QTimer()
                self.theme_timer.timeout.connect(self.check_theme_change)
                self.theme_timer.start(1000)  # Check every second
                
                # Store current theme state
                self.current_theme_dark = darkdetect.isDark()
                print("✓ Theme monitoring enabled")
            except Exception as e:
                print(f"⚠️  Error setting up theme monitoring: {e}")

    def check_theme_change(self):
        """Check if system theme has changed and update accordingly"""
        try:
            if DARKDETECT_AVAILABLE:
                is_dark = darkdetect.isDark()
                if is_dark != self.current_theme_dark:
                    # Theme changed
                    if is_dark:
                        setTheme(Theme.DARK)
                        print("✓ Theme changed to Dark")
                    else:
                        setTheme(Theme.LIGHT)
                        print("✓ Theme changed to Light")
                    
                    # Refresh window title to ensure visibility
                    self.setWindowTitle("Mario Party Toolkit")
                    
                    # Refresh title bar styling for new theme
                    self.apply_title_bar_style()
                    
                    self.current_theme_dark = is_dark
        except Exception as e:
            # Silently handle errors to avoid spam
            pass

    def mousePressEvent(self, event):
        """Handle mouse press events for window dragging"""
        # Only handle dragging if clicking in the title bar area (top portion of window)
        # This allows normal window resizing from edges
        if event.button() == Qt.LeftButton:
            # Check if click is in the top portion (title bar area)
            # Title bar is typically around 30-40 pixels tall
            title_bar_height = 40
            if event.pos().y() < title_bar_height:
                self.oldPos = event.globalPos()
            else:
                # Let the default handler deal with it (for resizing, etc.)
                super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """Handle mouse move events for window dragging"""
        if self.oldPos:
            delta = event.globalPos() - self.oldPos
            new_pos = self.pos() + delta
            self.move(new_pos)
            self.oldPos = event.globalPos()
            
            # Check for corner snapping if enabled
            if self.corner_lock_enabled:
                self.check_corner_snap()
        else:
            # Let default handler deal with resizing cursors, etc.
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """Handle mouse release events for window dragging"""
        if event.button() == Qt.LeftButton:
            if self.oldPos:
                self.oldPos = None
                # Snap to corner on release if enabled
                if self.corner_lock_enabled:
                    self.check_corner_snap()
            else:
                super().mouseReleaseEvent(event)
        else:
            super().mouseReleaseEvent(event)
    
    def toggle_corner_lock(self):
        """Toggle corner locking on/off"""
        self.corner_lock_enabled = not self.corner_lock_enabled
        settings = QSettings("Mario Party Toolkit", "Settings")
        settings.setValue("corner_lock_enabled", self.corner_lock_enabled)
        print(f"✓ Corner snapping {'enabled' if self.corner_lock_enabled else 'disabled'}")
        return self.corner_lock_enabled
    
    def keyPressEvent(self, event):
        """Handle keyboard shortcuts"""
        # Ctrl+L to toggle corner locking
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_L:
            self.toggle_corner_lock()
        else:
            super().keyPressEvent(event)
    
    def check_corner_snap(self):
        """Check if window should snap to a corner and snap it"""
        try:
            screen = QApplication.primaryScreen()
            if not screen:
                return
            
            screen_geometry = screen.availableGeometry()
            window_geometry = self.geometry()
            
            # Get window position and size
            window_x = window_geometry.x()
            window_y = window_geometry.y()
            window_width = window_geometry.width()
            window_height = window_geometry.height()
            
            # Screen boundaries
            screen_left = screen_geometry.x()
            screen_top = screen_geometry.y()
            screen_right = screen_geometry.x() + screen_geometry.width()
            screen_bottom = screen_geometry.y() + screen_geometry.height()
            
            new_x = window_x
            new_y = window_y
            
            # Check top-left corner
            if abs(window_x - screen_left) < self.snap_threshold and abs(window_y - screen_top) < self.snap_threshold:
                new_x = screen_left
                new_y = screen_top
            
            # Check top-right corner
            elif abs((window_x + window_width) - screen_right) < self.snap_threshold and abs(window_y - screen_top) < self.snap_threshold:
                new_x = screen_right - window_width
                new_y = screen_top
            
            # Check bottom-left corner
            elif abs(window_x - screen_left) < self.snap_threshold and abs((window_y + window_height) - screen_bottom) < self.snap_threshold:
                new_x = screen_left
                new_y = screen_bottom - window_height
            
            # Check bottom-right corner
            elif abs((window_x + window_width) - screen_right) < self.snap_threshold and abs((window_y + window_height) - screen_bottom) < self.snap_threshold:
                new_x = screen_right - window_width
                new_y = screen_bottom - window_height
            
            # Apply snap if position changed
            if new_x != window_x or new_y != window_y:
                self.move(new_x, new_y)
        except Exception as e:
            # Silently handle errors
            pass

    def apply_title_bar_style(self):
        """Apply minimal styling to fix only the title bar text visibility."""
        try:
            # Import FluentWindow's theme detection
            from qfluentwidgets import isDarkTheme
            
            # Determine if we're in dark mode using FluentWindow's built-in detection
            is_dark_theme = isDarkTheme()
            
            # Set only text color - don't change backgrounds or other styling
            if is_dark_theme:
                text_color = "#FFFFFF"
            else:
                text_color = "#000000"
            
            # Apply minimal styling - only target title text, not the entire window
            title_style = f"""
            /* Only style title label text color */
            QLabel[objectName="titleLabel"] {{
                color: {text_color} !important;
            }}
            
            QWidget[objectName="titleBar"] QLabel {{
                color: {text_color} !important;
            }}
            """
            
            # Don't override the entire window stylesheet, just add our specific rule
            current_style = self.styleSheet()
            if "QLabel[objectName=\"titleLabel\"]" not in current_style:
                self.setStyleSheet(current_style + title_style)
            
            # Try to find and style title components directly without changing backgrounds
            self.force_title_bar_styling(text_color)
            
            print(f"✓ Title bar text color applied ({'Dark' if is_dark_theme else 'Light'} theme) - Text: {text_color}")
        except Exception as e:
            print(f"⚠️  Error applying title bar styling: {e}")
    
    def force_title_bar_styling(self, text_color):
        """Find and style only the title text, preserving all other styling"""
        try:
            from PyQt5.QtWidgets import QLabel, QWidget
            
            # Find all QLabel widgets that might be the title
            all_labels = self.findChildren(QLabel)
            for label in all_labels:
                # Check if this might be a title label
                if (label.text() == "Mario Party Toolkit" or 
                    label.objectName() in ["titleLabel", "title"] or
                    "title" in label.objectName().lower()):
                    # Only change text color, preserve existing styling
                    current_style = label.styleSheet()
                    # Remove any existing color declarations
                    import re
                    current_style = re.sub(r'color\s*:\s*[^;]+;?', '', current_style)
                    # Add our color
                    label.setStyleSheet(f"{current_style} color: {text_color} !important;")
                    print(f"  → Styled title label: {label.objectName()} / '{label.text()}'")
            
            # Find title bar widgets and style only their text labels
            all_widgets = self.findChildren(QWidget)
            for widget in all_widgets:
                if ("title" in widget.objectName().lower() and 
                    "bar" in widget.objectName().lower()):
                    print(f"  → Found title bar widget: {widget.objectName()}")
                    
                    # Style only text labels in title bar, not the container
                    for child in widget.findChildren(QLabel):
                        current_style = child.styleSheet()
                        # Remove any existing color declarations
                        import re
                        current_style = re.sub(r'color\s*:\s*[^;]+;?', '', current_style)
                        # Add our color
                        child.setStyleSheet(f"{current_style} color: {text_color} !important;")
                        print(f"    → Styled title bar label: '{child.text()}'")
                        
        except Exception as e:
            print(f"  ⚠️ Error in force styling: {e}")
