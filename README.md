Für das Folgende Programm wurde Python 3.9.7 genutzt.

# erstelle virtuelle Umgebung (MacOs/Unix)
falls nicht installiert:
```pip install virtualenv```

navigiere mit Terminal in noteapp-main:
```virtualenv venv --system-site-packages```
```source venv/bin/activate```

links sollte nun (venv) stehen

# erstelle virtuelle Umgebung (Windows)

fall nich installiert:
```pip install virtualenv```

navigiere mit Terminal in noteapp-main:
```python -m venv noteapp_env```
```noteapp_env\Scripts\activate```

links sollte nun (noteapp_env) stehen

# Installieren der Pakete
```pip install -r requirements.txt```

# start des Programms
```cd noteapp```
```python manage.py runserver```

nun läuft das  Programm unter localhost:8000 bzw. dem im Terminal erschienen Link.
