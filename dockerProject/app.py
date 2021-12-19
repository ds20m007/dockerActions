from flask import Flask, send_file, request
from transformers import pipeline

print("Will download models... this may take some time...")

model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
app = Flask(__name__)

print("Sever started!")

@app.route('/mlModel',methods=['POST'])
def get_id():
   QA_input = {
    'question': request.form.get('question'),
    'context': request.form.get('context')
   }
   res = nlp(QA_input)
   return {"input_question" : QA_input["question"],
         "input_context" : QA_input["context"],
         "answer" : res["answer"],
         "score" : res["score"]
      }
   

@app.route('/')
def home():
   return send_file('index.html')