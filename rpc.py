from random import choice, randint
from pygetwindow import getWindowsWithTitle, getActiveWindow, PyGetWindowException
from pypresence import Presence, exceptions

CLIENT_ID = "1164662365531422780"
rpc = Presence(client_id=CLIENT_ID)
choice(["python", "cpp", "rust"])
buttons = [{"label": f"Check out my GitHub!", "url": f"https://github.com/AHOSUN-YOUSUF"},
           {"label": f"Yk Coding, join Coder Hub!", "url": f"https://discord.gg/dpuBe7wFTR"}]
lang_name = choice(["python", "cpp", "rust"])
bugs_added = randint(1, 10000000000)
random_msg = "Talking ppl known to be part of Cult organizition."
rpc.connect()

def reverse_string(text):

  reversed_text = ""
  for char in text[::-1]:
    reversed_text += char
  return reversed_text

def get_active_window_title():
    try:
        active_window = getWindowsWithTitle(getActiveWindow().title)
        if active_window:
             return active_window[0].title
    except AttributeError:
        pass

def check_active_window_and_set_rpc():
    try:
        result = str(get_active_window_title())
        if str(result[0:18]) == "Visual Studio Code":
            if result[-3:] == ".py":
                rpc.update(details = f"Adding bugs to: `{result[21:]}`.",
                           state = f"{bugs_added} bugs added!",
                           large_image = "python",
                           large_text = "Cooking some Code!",
                           small_image = "vsc",
                           small_text = "Using Visual Studio Code!",
                           buttons = buttons)

            elif result[-4:] ==  ".cpp":
                rpc.update(details = f"Adding bugs to: `{result[21:]}`.",
                           state = f"{bugs_added} bugs added!",
                           large_image = "cpp",
                           large_text = "Addin bugs to: `main.cpp`",
                           small_image = "vsc",
                           small_text = "Using Visual Studio Code!",
                           buttons = buttons)
            elif result[-3:] ==  ".rs":
                rpc.update(details = f"Adding bugs to: `{result[21:]}`.",
                           state = f"{bugs_added} bugs added!",
                           large_image = "cpp",
                           large_text = "Addin bugs to: `main.rs`",
                           small_image = "vsc",
                           small_text = "Using Visual Studio Code!",
                           buttons = buttons)
            else:
                rpc.update(details = f"Sitting on my Ass!",
                           state = f"🤨 What you looking at?????",
                           large_image = "idle",
                           large_text = "Addin bugs to: `main.rs`",
                           small_image = "vsc",
                           small_text = "Doing nothing!",
                           buttons = buttons)

            return "Visual Studio Code"

        elif reverse_string(result)[0:7] == "drocsiD":
            
            rpc.update(details = f"In {result[:-10]}!",
                       state = random_msg,
                       large_image = "discord",
                       large_text = random_msg,
                       small_image = "verified",
                       small_text = f"In {result[:-10]}",
                       buttons = buttons)

            return "Discord"

        elif result[0:7] == "YouTube":
            rpc.update(details = "Watching YouTube!",
                       state = "🙂",
                       large_image = "youtube",
                       large_text = "Watchin some YouTube!",
                       small_image = "verified",
                       small_text = f"{result[10:-10]}",
                       buttons = buttons)

            return "YouTube"

        elif reverse_string(result)[0:15] == "egdE ​tfosorciM":
            rpc.update(details = "Browsing the WEB!",
                       state = "🙂",
                       large_image = "msedge",
                       large_text = "Using Microsoft Edge!",
                       small_image = "verified",
                       small_text = "Why you need to know what I'm browsin???",
                       buttons = buttons)

            return "Microsoft Edge"

        elif result == "Task Switching":
            rpc.update(details = "Switching between Tasks!",
                       state = "🙂",
                       large_image = "switching",
                       large_text = "Swichin Task!",
                       small_text = "Why you need to know what I'm doin???",
                       buttons = buttons)

            return "Task Switching"

        else:
            return None

    except AttributeError:
        pass
    except PyGetWindowException:
        pass

while True:
    try:
        check_active_window_and_set_rpc()
    except exceptions.PipeClosed:
        rpc.connect()
    except exceptions.ResponseTimeout:
        rpc.connect()
    except exceptions.ServerError:
        rpc.connect()
    except PyGetWindowException:
        pass