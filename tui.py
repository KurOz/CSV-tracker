from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer, Static


class Tracker(App):
    """A task tracking app"""

    CSS_PATH = "tracker_app.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Static("Table_headers", id="table_headers")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = Tracker()
    app.run()

