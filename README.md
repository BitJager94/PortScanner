# GitHub Documentation: Port Scanner

## Introduction

The Port Scanner is a Python script with a graphical user interface (GUI) that allows you to scan ports on a specified host. It supports scanning a range of ports and provides the flexibility to set the number of threads for parallel scanning. The script utilizes the `socket` and `tkinter` libraries to perform the port scanning and display the results.

## Prerequisites

Before using the Port Scanner, make sure you have the following dependencies installed:

- Python 3.x

No additional packages are required as the script uses built-in libraries.

## Usage

To use the Port Scanner, follow the steps below:

1. Import the necessary libraries:

```python
import socket
import tkinter as tk
import threading
```

2. Implement the `port_scan` function to initiate the port scanning process:

```python
def port_scan():
    # ...
```

3. Implement the `chunk_port_range` function to divide the port range into equal chunks for parallel scanning:

```python
def chunk_port_range(start_port, end_port, num_chunks):
    # ...
```

4. Implement the `perform_port_scan` function to perform the actual port scanning:

```python
def perform_port_scan(target_host, port_range):
    # ...
```

5. Create the GUI using the `tkinter` library:

```python
window = tk.Tk()
window.title("Port Scanner")

frame = tk.Frame(window)
frame.pack()

# Define GUI elements (labels, entries, buttons, etc.) and their layout

window.mainloop()
```

6. Run the script to start the GUI application.

7. Enter the target host address, start and end port numbers, and the desired number of threads.

8. Click the "Start Scanning" button to initiate the port scanning process.

9. The results will be displayed in the result text area.

## Example

Here's an example of how to use the Port Scanner:

```python
python PortScanner.py
```

## Conclusion

The Port Scanner script provides a convenient graphical interface to perform port scanning on a specified host. It supports parallel scanning using multiple threads and displays the results in real-time. Customize the script further based on your specific requirements and make use of the provided functions to extend its functionality. Happy port scanning!