# QtCalculator

A simple calculator application built using Python and the PySide6 framework for a graphical user interface.

## Architecture Overview

The `qtcalculator` repository is structured with three main components:

1. **README.md**: This file provides an overview of the project, including setup instructions.
2. **main.py**: The core logic of the calculator application. It handles both GUI and CLI modes.
3. **main.ui**: A Qt Designer UI file that defines the graphical layout of the calculator.

The `main.py` script imports necessary modules from PySide6 to load and display the UI defined in `main.ui`. It also contains the `Calculator` class, which manages the calculator's logic, including handling button clicks and performing calculations.

## Tech Stack

- **Programming Language**: Python
- **GUI Framework**: PySide6 (a set of Python bindings for Qt libraries)
- **UI Designer**: Qt Designer (for creating the `.ui` file)

## Getting Started / Setup Guide

### Prerequisites

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install PySide6 using pip:
   ```bash
   pip install PySide6
   ```

### Installation and Execution

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/qtcalculator.git
   cd qtcalculator
   ```

2. Run the calculator application:
   ```bash
   python main.py
   ```

This will launch the GUI version of the calculator. If you want to run it in CLI mode, modify the `mode` variable at the top of `main.py` from `'gui'` to `'cli'`.

### Building the UI

The `main.ui` file is generated using Qt Designer. To edit or rebuild this file:

1. Install Qt Designer if not already installed.
2. Open `main.ui` with Qt Designer and make any necessary changes.
3. Save the changes, which will automatically update the `.ui` file.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.