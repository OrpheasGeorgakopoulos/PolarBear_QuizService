import openai
from ttkthemes import ThemedTk
from tkinter import *
from tkinter import ttk
import time

client = openai.OpenAI(api_key = "YOUR-OPENAI-KEY")

window = ThemedTk(theme="arc")
window.configure(themebg="arc")
window.geometry("500x500")
window.title("PolarBear - Quiz Services - 10 Question Demo Quiz")
window.resizable(False, False)
score = 0
questionsasked = 0
def check(uasnwer):
    global score
    global questionsasked
    if answer==uasnwer:
        score += 1
        questionsasked += 1
        pb['value'] +=10
        lblscore.configure(text="Correct Answers: "+str(score)+ " / "+str(questionsasked))
    else:
        questionsasked += 1
        lblscore.configure(text="Wrong Question! Correct Answers: "+str(score)+ " / "+str(questionsasked))
    if questionsasked == 3:
        time.sleep(1)
        global btnreset, framebuttons, lbl
        framebuttons.pack_forget()
        pb.pack_forget()
        lblscore.pack_forget()
        lbl.pack_forget()
        btnreset.configure(text="Reset", )
        btnreset.pack()
    else:
        generate_question()

def reset():
    global score,questionsasked
    score = 0
    questionsasked = 0
    lbl.pack()
    framebuttons.pack()
    pb.pack()
    lblscore.pack()
    generate_question()
    btnreset.pack_forget()




lbl = ttk.Label(window,text="", font =("Comic Sans MS" ,11))
lbl.pack()

btnreset = ttk.Button(window,text="",command=reset)


framebuttons = ttk.Frame()
framebuttons.pack()

yesbtn = ttk.Button(framebuttons, text = "YES", command=lambda:check("yes"))
yesbtn.pack(side='left')

nobtn = ttk.Button(framebuttons, text = "NO", command=lambda:check("no"))
nobtn.pack()


lblscore=ttk.Label(window, text = "")
lblscore.pack()

pb = ttk.Progressbar(window, length=300)
pb.pack()
def generate_question():
    global answer
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Generate a simple and short yes/no question in English about microcontrollers with a clear correct answer."
                                        "Return the format: 'Question: <question> | Answer: <yes/no>' "},
            {"role": "user", "content": "Generate a simple yes/no question."}
        ]
    )
    # print(response)
    result = response.choices[0].message.content.strip()
    # print(result)
    question_part, answer_part = result.split(" | ")
    # print(question_part)
    # print(answer_part)
    question = question_part.replace("Question: ", "").strip()
    answer = answer_part.replace("Answer: ", "").strip().lower()
    print(question)
    print(answer)
    lbl.configure(text = question)



generate_question()
window.mainloop()
