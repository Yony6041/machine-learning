"""Display message for users to run a script to activate the env"""

from rich.console import Console

console = Console()
console.print(
    "\n :gear: :hammer_and_wrench: [bold magenta] Dependencies installed![/bold magenta]:gear: :hammer_and_wrench: \n",
    emoji=True,
)
