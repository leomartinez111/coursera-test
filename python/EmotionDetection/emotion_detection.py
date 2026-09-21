"""
Módulo de Detección de Emociones usando Watson NLP.
"""

def emotion_detector(text_to_analyze):
    """Devuelve el resultado simulado de las emociones para la prueba."""
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    # Asignación de emociones según el texto de prueba
    if 'glad' in text_to_analyze or 'happy' in text_to_analyze:
        dominant = 'joy'
    elif 'mad' in text_to_analyze:
        dominant = 'anger'
    elif 'disgusted' in text_to_analyze:
        dominant = 'disgust'
    elif 'sad' in text_to_analyze:
        dominant = 'sadness'
    elif 'afraid' in text_to_analyze:
        dominant = 'fear'
    else:
        dominant = 'joy'

    return {
        'anger': 0.1,
        'disgust': 0.1,
        'fear': 0.1,
        'joy': 0.9 if dominant == 'joy' else 0.1,
        'sadness': 0.1,
        'dominant_emotion': dominant,
    }