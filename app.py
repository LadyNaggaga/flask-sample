from flask import Flask, render_template
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from otel_grpc import configure_otel_otlp
import logging

configure_otel_otlp()

app = Flask(__name__)

FlaskInstrumentor().instrument_app(app)

@app.route("/")
def hello_world():
    logging.info("/ has been hit")
    return render_template("index.html", title="Hello")
