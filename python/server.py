"""
Servidor Flask para la aplicación de Detección de Emociones.
"""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Emotion Detection App</title>
    <script>
        let RunSentiment = () => {
            textToAnalyze = document.getElementById("textToAnalyze").value;
            let xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("system_response").innerHTML = xhttp.responseText;
                }
            };
            xhttp.open("GET", "/emotionDetector?textToAnalyze=" + textToAnalyze, true);
            xhttp.send();
        }
    </script>
</head>
<body>
    <h1>Emotion Detector Application</h1>
    <label for="textToAnalyze">Enter Text for Emotion Detection:</label><br><br>
    <textarea id="textToAnalyze" name="textToAnalyze" rows="4" cols="50"></textarea><br><br>
    <button onclick="RunSentiment()">Run Sentiment</button>
    <br><br>
    <div id="system_response"></div>
</body>
</html>
"""

@app.route("/emotionDetector")
def emo_detector():
    """Analiza el texto recibido y devuelve la respuesta formateada."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """Renderiza la página de inicio."""
    return HTML_CODE

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)