# GRP11_MIDTERMS
CS0053 MIDTERM LAB
GROUP 11:
Que, Adrian Dominique
Que, Desmond Khalel
Valentino, Ferdinand Paul

## To-Do Application
A simple command-line to-do list application that allows users to add, view, and remove tasks. Tasks are persisted to a file (`tasks.txt`).

## Setup and Usage

### Requirements
- Python 3.6+ installed on your system

### How to Run
1. Navigate to the project directory:
   ```
   cd GRP11_MIDTERMS
   ```

2. Run the program:
   ```
   python toDoApp.py
   ```

### How to Use
- **Main Menu**: Choose from 4 options by entering 1-4
  - `[1] Add Task` - Enter a new task to add to your list
  - `[2] Show Tasks` - Display all your current tasks
  - `[3] Remove Task` - Delete a task by entering its number
  - `[4] Exit` - Close the application

- **Task Persistence**: All tasks are automatically saved to `tasks.txt` and will be loaded when you restart the program

## Coding Standards Implemented

### 1. Documentation
- Docstrings for all functions following PEP 257
- Module-level docstring
- Comprehensive parameter and return value documentation

### 2. Naming Conventions (PEP 8)
- `snake_case` for functions and variables
- `UPPER_CASE` for constants (e.g., `TASKS_FILE`)
- Descriptive variable names (e.g., `choice` instead of `ch`, `task_input` instead of `t`)

### 3. Code Structure
- Proper indentation (4 spaces)
- Consistent spacing around operators
- Logical organization of functions

### 4. Functional Programming Principles
- **No global variables** - eliminated the use of `global` statement
- Functions accept parameters and return values instead of modifying global state
- Pure functions where possible, making code more testable and maintainable

### 5. Pythonic Practices
- Used `enumerate()` instead of manual range indexing
- List comprehensions for reading tasks from file
- `if __name__ == "__main__":` guard for module execution

### 6. Error Handling
- Bounds checking in `remove_task()` to prevent index errors
- Validation of user input

### 7. Code Quality Improvements
- Proper conversion between 1-based user input and 0-based list indexing
- Improved readability with f-strings for output formatting
- Added newline spacing in menu for better user experience

## FINAL VERSION - Additional Refinements & Bug Fixes

### Changes Made:
1. **UI Flow Improvement - Bug fix on delete task**
   - Added optional `pause` parameter to `show_tasks()` function
   - Set `pause=False` when displaying tasks before removal to eliminate redundant "Press Enter" prompt

2. **Exit Screen Enhancement**
   - Centered developer names on exit screen using `.center(50)` method
   - Consistent formatting with bordered layout (50-character width)
   - Professional presentation of team member credits:
     - Que, Adrian
     - Que, Desmond
     - Valentino, Ferdinand

3. **Code Readability**
   - Updated `show_tasks()` docstring to document the `pause` parameter
   - Maintained backward compatibility with default `pause=True`
   - Clear and explicit function calls: `show_tasks(tasks, pause=False)`

### Technical Details:
- Modified `show_tasks(tasks, pause=True)` to accept optional boolean parameter
- Conditional execution of `input("\nPress Enter to continue...")` based on `pause` value
- Consistent use of `.center(50)` for all centered text elements
- Maintained all previous features from V3 (pylint compliance, file persistence, error handling)

---

## Changelog

### Version 3 (V3) - UI Enhancement & Complete Pylint Compliance (QUE, D.)

**Major Refactoring (Pylint Compliance):**
- **Eliminated global variables** - removed all `global` statements
- Refactored all functions to accept `tasks` as parameter and return updated list
- Added `if __name__ == "__main__":` guard for proper module execution
- Replaced manual range indexing with `enumerate()` for Pythonic iteration
- Fixed all PEP 8 spacing issues:
  - `tasks=[]` → proper spacing
  - `if len(tasks)==0` → `if len(tasks) == 0`
  - `for i in range (len(tasks))` → `enumerate(tasks, start=1)`
- Improved variable names: `ch` → `choice`, `t` → `task_input`, `n` → `task_num`
- Enhanced docstrings with complete Args and Returns sections
- Added module-level docstring

**UI Enhancements:**
- Added `clear_screen()` function for better user experience (uses `cls` on Windows, `clear` on Unix)
- Redesigned UI with decorative borders and centered titles
- Added "Press Enter to continue..." prompts for flow control
- Improved task display with bordered layout and bracket notation `[1]`
- Added comprehensive input validation:
  - Empty task prevention
  - Try-except block for invalid numeric input
  - Shows removed task name in confirmation message
- Professional exit screen with thank you message
- Better spacing and organization throughout the interface

**Key Features:**
- No global variables - functional programming approach
- Cross-platform screen clearing
- Consistent 50-character width layout
- User-friendly error messages
- Improved readability with f-strings
- Maintains file persistence from V2

---

### Version 2 (V2) - File Persistence & Constants (QUE, A.)

**Changes from V1:**
- **Added file persistence functionality:**
  - `load_tasks()` function - loads tasks from `tasks.txt` file on startup using `os.path.exists()`
  - `save_tasks()` function - saves tasks to file after add/remove operations
  - Tasks now persist between program sessions
  - Proper file handling with `open()` and context managers (`with` statement)
  - UTF-8 encoding for proper character support
  - Whitespace removal across the entire program
  - Removal of unecessary semi-colon ';' in break statement within the switch case menu
- **File I/O features:**
  - Added `import os` module for file operations
  - Introduced `TASKS_FILE` constant with proper UPPER_CASE naming convention
  - Used list comprehension for reading file lines efficiently
  - Proper file closing with context manager
- Used `global tasks` keyword in `load_tasks()` to modify global list (later removed in V3)
- Enhanced menu formatting with box characters `|`
- Added "Exiting program" message
- Calls `load_tasks()` at program start to restore saved tasks
- Calls `save_tasks()` after every add/remove operation

**Key Features:**
- **Task persistence between sessions via file I/O**
- Automatic file creation if doesn't exist
- Data durability - tasks survive program restarts
- Constant naming conventions (TASKS_FILE)

---

### Version 1 (V1) - Documentation & Standards (VALENTINO)

**Changes from V0:**
- Added comprehensive docstrings to all functions following PEP 257
- Implemented `snake_case` naming convention:
  - `addtask` → `add_task`
  - `showTasks` → `show_tasks`
  - `removetask` → `remove_task`
- Added function parameter and return documentation (Args sections)
- Fixed indentation issues from V0
- Module-level comments (Docstrings)
- Improved code organization and readability
- Maintained consistent 4-space indentation

**Issues Present:**
- Still used global `tasks` variable
- Inconsistent spacing around operators (`tasks==0`, `range (len`)
- Menu formatting inconsistencies (`"1 Add Task"` vs `"2.Show Tasks"`)
- No file persistence - tasks lost when program exits

---

### Version 0 (V0) - Initial Implementation

**Initial Features:**
- Basic to-do list functionality:
  - `addtask()` - add tasks to list
  - `showTasks()` - display all tasks
  - `removetask()` - remove task by index
  - `main()` - command-line menu interface
- Global `tasks` list for storage
- Simple 4-option menu (Add/Show/Remove/Exit)
- In-memory storage only (no file persistence)

**Issues Present:**
- No docstrings or comments
- Inconsistent naming (mixed camelCase and lowercase)
- Poor indentation (main function incorrectly indented inside removetask)
- No input validation
- Inconsistent menu formatting
- No error handling
- Used semicolon after `break` statement (not Pythonic)
- **No file persistence - all tasks lost when program exits**

