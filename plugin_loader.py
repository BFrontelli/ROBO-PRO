import os
import importlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLAT_DIR = os.path.join(BASE_DIR, "plataformas")

def carregar():
    plataformas = []

    if not os.path.exists(PLAT_DIR):
        print("⚠️ Pasta plataformas não encontrada:", PLAT_DIR)
        return plataformas

    for arq in os.listdir(PLAT_DIR):
        if arq.endswith(".py") and arq != "__init__.py":
            nome = arq[:-3]
            mod = importlib.import_module(f"plataformas.{nome}")
            plataformas.append((nome, mod.coletar_ofertas))

    return plataformas
