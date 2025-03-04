import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("https://raw.githubusercontent.com/Apaulgithub/oibsip_taskno4/main/spam.csv", encoding='ISO-8859-1')
df.rename(columns={"v1": "Category", "v2": "Message"}, inplace=True)
df.drop(columns={'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'}, inplace=True)
df['Spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

X_train, X_test, y_train, y_test = train_test_split(df.Message, df.Spam, test_size=0.25)

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    print("\nTrain ROC AUC:", roc_auc_score(y_train, y_pred_train))
    print("Test ROC AUC:", roc_auc_score(y_test, y_pred_test))
    print("\nTrain Classification Report:")
    print(classification_report(y_train, y_pred_train))
    print("\nTest Classification Report:")
    print(classification_report(y_test, y_pred_test))
    
clf = Pipeline([
    ('vectorizer', CountVectorizer()),  
    ('nb', MultinomialNB())  
])

evaluate_model(clf, X_train, X_test, y_train, y_test)

def detect_spam(email_text):
    return "Spam Email!" if clf.predict([email_text])[0] else "Not spam Email!"

sample_email = """Subject: 🎉 Congratulations! You've Won a Free iPhone 15! 🎉

Dear User,

You have been selected as the lucky winner of our exclusive iPhone 15 giveaway! 🎁 To claim your brand-new iPhone, all you have to do is confirm your details by clicking the link below:

👉 Claim Your Prize Now 👈

Hurry! This offer expires in 24 hours. If you do not claim your prize, it will be given to the next lucky winner.

Best Regards,
The Giveaway Team
support@freeiphonepromo.com

"""
not_spam="""**Subject:** 📅 Reminder: Upcoming Team Meeting on March 10  

**Dear Alex,**  

I hope you're doing well. This is a reminder about our upcoming **team meeting** scheduled for **March 10 at 3:00 PM (IST)**.  

### **Agenda:**  
- Progress update on the **TeraSense AI Model**  
- Review of recent **satellite data analysis**  
- Discussion on **next steps for disaster prediction accuracy**  
- Addressing any roadblocks  
- Open floor for questions and feedback  

**Meeting Link:** [https://meet.example.com/terasense-meeting](#)  

Please make sure to join on time. Let me know if you have any conflicts or need any adjustments. Looking forward to catching up with everyone!  

Best Regards,  
**Ravi Sharma**  
AI Research Lead  
TeraSense Pvt. Ltd."""
print(detect_spam(not_spam))