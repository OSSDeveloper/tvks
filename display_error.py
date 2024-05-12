import sys
import rich
from rich.pretty import Pretty
from rich.traceback import install
from rich.traceback import Traceback
install()

def display_exception(exc: Exception) -> None:
    """Display an exception object in a well-formatted way"""
    exc_type, exc_value, exc_traceback = sys.exc_info()  # Get exception info
    traceback = Traceback.from_exception(exc_type, exc_value, exc_traceback)  # Create Traceback object

    rich.print("[bold red]Error:", exc.__class__.__name__)
    rich.print(Pretty(exc))
    rich.print("[bold red]Traceback:")
    rich.print("[gray]-----------------------------------------------------")
    rich.print(traceback)
    rich.print("[gray]-----------------------------------------------------")