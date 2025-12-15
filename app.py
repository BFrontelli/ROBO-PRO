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

@app.before_first_request
def start():
    threading.Thread(target=robo, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
