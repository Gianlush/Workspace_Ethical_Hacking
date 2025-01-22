def read_file(file_path):
    try:
        # Apertura del file in modalità di lettura
        with open(file_path, 'rb') as file:
            # Lettura del contenuto del file
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Errore: Il file {file_path} non è stato trovato."
    except Exception as e:
        return f"Si è verificato un errore: {e}"

# Percorso del file (modifica con il percorso reale del tuo file)
file_path = '/home/kali/Workspace_Ethical_Hacking/hack_the_box/htb_machines/backfire/t.pfx'

# Leggi e stampa il contenuto del file
file_content = read_file(file_path)
print(file_content)
