from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from src.core.models import AttendanceRecord

console = Console()

def print_welcome():
    console.print(Panel.fit("[bold blue]Registro Presenze CLI[/bold blue]\n[italic]Controlla il progresso del tuo corso[/italic]", border_style="blue"))

def print_menu_options():
    console.print("\n[bold]Seleziona un'opzione:[/bold]")
    console.print("1. [green]Controlla le mie Presenze[/green]")
    console.print("2. [yellow]Verifica Integrità Foglio (Trainer)[/yellow]")
    console.print("3. [red]Esci[/red]")

def print_stats(record: AttendanceRecord):
    table = Table(title=f"Statistiche per Studente ID: {record.student_id}")

    table.add_column("Metrica", style="cyan", no_wrap=True)
    table.add_column("Valore", style="magenta")

    table.add_row("Lezioni Totali", str(record.total_lectures))
    table.add_row("Presenze", str(record.present_count))
    table.add_row("Assenze", str(record.absence_count))
    
    # Color code the percentage
    pct = record.attendance_percentage
    color = "green" if pct >= 75 else "yellow" if pct >= 50 else "red"
    
    table.add_row("Percentuale Presenze %", f"[{color}]{pct:.1f}%[/{color}]")

    console.print(table)

def print_error(msg: str):
    console.print(f"[bold red]Errore:[/bold red] {msg}")

def print_success(msg: str):
    console.print(f"[bold green]Successo:[/bold green] {msg}")
