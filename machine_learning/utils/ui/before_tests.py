"""Display message for developers before tests run"""

import time

from rich.console import Console

# Create Console Object
console = Console()

console.print(
    ":mage: [bold magenta]Let's see what you've got![/bold magenta] :sparkles:",
    emoji=True,
)

# Time-lapse effect (pause for 3 seconds)
time.sleep(3)
