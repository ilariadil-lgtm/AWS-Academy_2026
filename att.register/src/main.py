import sys
import os

# Add the project root directory to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ui.menu import run_menu

def main():
    try:
        run_menu()
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
