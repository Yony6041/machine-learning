"""Display message for users before tests run"""

from rich.console import Console

# Create Console Object
console = Console()

console.print(
    ":mage: [bold magenta] Tests went well! You shall pass[/bold magenta] :sparkles:",
    emoji=True,
)
