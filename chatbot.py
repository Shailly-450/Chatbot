import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQChatbot:
    def __init__(self, data_path="data/faq.json"):
        with open(data_path, 'r') as f:
            self.faq = json.load(f)
        self.questions = [item["question"] for item in self.faq]
        self.answers = [item["answer"] for item in self.faq]
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def get_response(self, user_input):
        input_vector = self.vectorizer.transform([user_input])
        similarity = cosine_similarity(input_vector, self.question_vectors)
        best_match = similarity.argmax()
        if similarity[0, best_match] > 0.3:
            return self.answers[best_match]
        else:
            return "Sorry, I don't understand that."
