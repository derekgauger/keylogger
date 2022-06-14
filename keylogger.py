import keyboard
from collections import Counter
import mouse
keys_logged = []

class Keylogger:
    def callback(self, event):
        name = event.name

        if len(name) >= 1:
            keys_logged.append(name)

        keys_logged.sort()
        keys = list(Counter(keys_logged).keys())
        values = list(Counter(keys_logged).values())
        key_value_pairs = []

        if (len(keys) == len(values)):
            for i in range(len(keys)):
                key_value_pairs.append((keys[i], values[i]))

        print_string = ""
        for entry in key_value_pairs:
            print_string += str(entry[0]) + ": " + str(entry[1]) + " \n"
        f = open("KeysLog.txt", "w")
        f.write(print_string)
        f.close()

    def update_log(self):
        keys_logged.sort()
        keys = list(Counter(keys_logged).keys())
        values = list(Counter(keys_logged).values())
        key_value_pairs = []

        if (len(keys) == len(values)):
            for i in range(len(keys)):
                key_value_pairs.append((keys[i], values[i]))

        print_string = ""
        for entry in key_value_pairs:
            print_string += str(entry[0]) + ": " + str(entry[1]) + " \n"
        f = open("KeysLog.txt", "w")
        f.write(print_string)
        f.close()

    def start(self):
        keyboard.on_release(callback=self.callback)
        
        mouse.on_click(lambda: keys_logged.append("Left Click"))
        mouse.on_right_click(lambda: keys_logged.append("Right Click"))
        mouse.on_click(callback=self.update_log)
        mouse.on_right_click(callback=self.update_log)


        keyboard.wait()


if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()