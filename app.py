from flask import Flask, request, render_template
import vertexai
from vertexai.generative_models import GenerativeModel, Part

app = Flask(__name__)

# Initialize Vertex AI
PROJECT_ID = "second-base-438714-i3"
vertexai.init(project=PROJECT_ID)

model = GenerativeModel("gemini-1.5-flash-002")



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf_url = request.form.get("url")
        pdf_part = Part.from_uri(uri=pdf_url, mime_type="application/pdf")
        prompt = """
        You are a very professional document summarization specialist.
        Please summarize the given document in its original language.
        """
        contents = [pdf_part, prompt]
        response = model.generate_content(contents)

        return render_template("index.html", summary=response.text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
