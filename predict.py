from ml.train import get_model

model = get_model()


def predict_difficulty(text):
    words = len(text.split())

    # simple logic: concept_count approx
    concept_count = max(1, words // 3)

    prediction = model.predict([[words, concept_count]])

    return prediction[0]