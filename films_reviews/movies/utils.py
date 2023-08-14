import requests
from .tokens import HUGGING_FACE_TOKEN

def get_review_rating(review_text):
    API_URL = "https://api-inference.huggingface.co/models/lockiultra/rating_model"
    headers = {"Authorization": HUGGING_FACE_TOKEN}
    response = requests.post(API_URL, headers=headers, json={"inputs": review_text,})
    return int(response.json()[0][0]['label'].split('_')[1])

def get_review_status(review_text):
    API_URL = "https://api-inference.huggingface.co/models/lockiultra/status_model"
    headers = {"Authorization": HUGGING_FACE_TOKEN}
    response = requests.post(API_URL, headers=headers, json={"inputs": review_text,})
    return int(response.json()[0][0]['label'].split('_')[1])