from flask import Flask, jsonify
import os
import platform

app = Flask(__name__)

SERVICE_VER = os.getenv("SERVICE_VER", "1.0")
STAGE_NAME = os.getenv("STAGE_NAME", "container-env")

@app.route("/")
def status():
    return jsonify({
        "service": "birxil-servis",
        "state": "active",
        "version": SERVICE_VER,
        "stage": STAGE_NAME,
        "kernel": platform.release()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
