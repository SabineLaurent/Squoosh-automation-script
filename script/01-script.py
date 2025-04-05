import subprocess

img = input('mettez le chemin de votre image: ')

# Exécution de la commande via Python
subprocess.run(["npx", "@squoosh/cli", "--webp", "{quality:50}", "-d", "out", f"{img}"])
