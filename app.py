from flask import Flask, render_template, request, redirect, send_file
import os
import openai
from dotenv import load_dotenv  # python-dotenv 라이브러리를 import

# .env 파일 로드
load_dotenv()
API_KEY= os.getenv("FLASK_API_KEY")
app = Flask("MakeReport")

@app.route("/")
@app.route("/home")
def home():
    return Rendering()

def Rendering():
    return render_template("report_index.html", API_KEY=API_KEY)

@app.route("/askSubmit")
def ResponseForAsk(API_KEY=API_KEY):
    askText = request.args.get("askText")
    print(API_KEY)
    # set api key
    openai.api_key = API_KEY
    
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "너는 보고서를 작성하는 마법사이다. 보고자, 글내용, 제목, 각각의 특징들을 분석하여 보고서 양식에 맞게 작성하라"},
        {"role": "system", "content": "사용자가 보고서의 보고자명, 내용, 보고서제목 등을 입력하도록 유도하라"},
        {"role": "system", "content": "매 문단의 끝에 HTML &lt;br&gt; 태그를 추가하여 줄바꿈을 하라."},
        {"role": "user", "content": f" '{askText}' 앞의 내용을 보고서 양식대로 작성해줘"},
    ],
    temperature=0.8,
    max_tokens=2048
    )
    message_result = completion["choices"][0]["message"]["content"].encode("utf-8").decode("utf-8")
    print(message_result)
    # return render_template("report_index.html",response_text=message_result)
    return render_template("report_index.html",response_text=message_result , beforeAsk=askText)


if __name__ == '__main__':
    app.run(debug = True, port=5000)
