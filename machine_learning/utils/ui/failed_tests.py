"""Display message for users before tests run"""

from rich.console import Console

# Create Console Object
console = Console()

console.print(
    ":mage: :no_entry_sign: [bold red]You shall not pass from here![/bold red] :no_entry_sign:",
    emoji=True,
)
