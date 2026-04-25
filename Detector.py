from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print("🇳🇬 PRECIOUS AI loading.....")

scam_messages = [
    "You have won 5 million naira claim now",
    "URGENT your BVN will be blocked click link",
    "Congratulations you won iPhone 15 text WIN to 555",
    "Your account has been suspended verify now"
]
normal_messages = [
    "Merit how far, bring my charger abeg",
    "Mummy said come home after school",
    "LAUTECH post UTME form is out check portal",
    "Bro I dey Gbagba, network no dey"
]

all_messages = scam_messages + normal_messages
labels = [1,1,1,1,0,0,0,0] # 4 scams = 1, 4 normal = 0

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(all_messages)
ai_model = MultinomialNB()
ai_model.fit(X, labels)

print("✅ AI trained! Ready to detect scams")

while True:
    test_message = input("\nType SMS to check or 'quit' to exit: ")
    if test_message.lower() == 'quit':
        break

    test_X = vectorizer.transform([test_message])
    result = ai_model.predict(test_X)

    if result[0] == 1:
        print("⚠️ SCAM ALERT! Na scam be this o")
    else:
        print("✅ Safe message. No be scam")
