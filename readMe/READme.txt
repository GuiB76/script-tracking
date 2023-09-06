Pour créer un script Python qui se lance automatiquement à l'ouverture de la session sur votre ordinateur Windows et enregistre toutes les actions dans un fichier texte jusqu'à l'arrêt de l'ordinateur, vous devez suivre plusieurs étapes :

**1. Installation de Python :**

Si Python n'est pas déjà installé sur votre ordinateur, téléchargez et installez la dernière version de Python depuis le site officiel de Python (https://www.python.org/downloads/windows/).

**2. Installation des bibliothèques nécessaires :**

Vous aurez besoin de la bibliothèque `keyboard` pour surveiller les événements clavier. Vous pouvez l'installer en utilisant la commande suivante dans votre terminal :

```
pip install keyboard
```

**3. Création du script Python :**

Voici un exemple de script Python qui enregistre les actions dans un fichier texte avec l'heure de chaque action :

```python
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
```

**4. Création d'un exécutable :**

Pour que le script se lance automatiquement à l'ouverture de la session, vous pouvez créer un exécutable qui appelle le script Python. Pour ce faire, vous pouvez utiliser le module `pyinstaller` pour créer un exécutable à partir de votre script Python.

Installez `pyinstaller` avec la commande suivante :

```
pip install pyinstaller
```

Ensuite, utilisez `pyinstaller` pour créer un exécutable à partir de votre script Python :

```
pyinstaller --onefile nom_de_votre_script.py
```

Cela créera un dossier "dist" dans le répertoire de votre script, et à l'intérieur, vous trouverez l'exécutable. Vous pouvez déplacer cet exécutable dans le dossier de démarrage de Windows.

**5. Ajout de l'exécutable au démarrage de Windows :**

Pour que l'exécutable soit lancé automatiquement à l'ouverture de la session, suivez ces étapes :

- Appuyez sur `Win + R` pour ouvrir la boîte de dialogue "Exécuter".
- Tapez `shell:startup` et appuyez sur Entrée. Cela ouvrira le dossier de démarrage de l'utilisateur actuel.
- Copiez l'exécutable que vous avez créé avec `pyinstaller` dans ce dossier.

Désormais, votre script se lancera automatiquement chaque fois que vous ouvrez une session sur votre ordinateur Windows et enregistrera toutes les actions dans le fichier journal jusqu'à l'arrêt de l'ordinateur.

Assurez-vous de respecter la législation locale en matière de surveillance et de vie privée lorsque vous utilisez un tel script, et informez les utilisateurs de l'ordinateur de sa présence, le cas échéant.