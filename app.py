from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 簡單的回應邏輯
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

# 路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
