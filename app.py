# app.py (Flask backend for AegisDefenseChatbot)
from flask import Flask, request, render_template
from model_loader import load_qa_chain
from voice.mic import listen_and_convert
from updater import auto_update_csv
import os

app = Flask(__name__)

# Automatically update CSV database when app starts
auto_update_csv()

# Function to process user query
def process_query(user_input):
    if not user_input:
        return "Please enter a question."
    try:
        response = qa_chain.run(user_input)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    bot_response = ""

    if request.method == "POST":
        if "voice" in request.form:
            user_input = listen_and_convert()
        else:
            user_input = request.form.get("query")

        bot_response = process_query(user_input)

    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
