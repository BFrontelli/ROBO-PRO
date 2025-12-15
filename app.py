from flask import Flask, render_template
import threading, time, os
from settings import *
from plugin_loader import carregar
from mensagens import montar
from whatsapp import enviar
from cache import ja_enviado
from envio import delay

app = Flask(__name__)
PLATS = carregar()

def robo():
    while True:
        for p, f in PLATS:
            for o in f():
                if o["desconto"] < DESCONTO_MIN:
                    continue
                if ja_enviado(o["link"]):
                    continue
                enviar(montar(o, p))
                delay()
        time.sleep(INTERVALO_CICLO_MIN * 60)

import threading

_robo_started = False

def iniciar_robo():
    global _robo_started
    if not _robo_started:
        _robo_started = True
        threading.Thread(target=robo, daemon=True).start()
        print("🤖 Robô iniciado")

iniciar_robo()


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
