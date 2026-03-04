from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class Tracker(App):
    """A task tracking app"""

    CSS_PATH = "tracker_app.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        self.main_box = Static("TEST", id="main_box")
        yield self.main_box

    def on_mount(self):
        pass
        # self.main_box.styles.box_sizing = "content-box"
        # self.main_box.styles.padding = 0

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = Tracker()
    app.run()
