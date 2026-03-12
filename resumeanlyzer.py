import tkinter as tk
from tkinter import filedialog
import PyPDF2
import re

# Skills required
required_skills = [
    "python","java","c++","data structures",
    "algorithms","sql","machine learning",
    "git","html","css"
]

# Project keywords
project_keywords = [
    "project","quiz","planner","analyzer","system","tracker"
]

def analyze_resume():

    file_path = filedialog.askopenfilename(filetypes=[("PDF Files","*.pdf")])

    if not file_path:
        return

    text_box.delete(1.0, tk.END)

    try:
        with open(file_path,"rb") as file:

            reader = PyPDF2.PdfReader(file)

            resume_text = ""

            for page in reader.pages:
                resume_text += page.extract_text()

            resume_text = resume_text.lower()

    except:
        text_box.insert(tk.END,"Error reading PDF file")
        return

    matched = []
    missing = []

    for skill in required_skills:
        if re.search(skill,resume_text):
            matched.append(skill)
        else:
            missing.append(skill)

    score = len(matched)
    percentage = (score/len(required_skills))*100

    # Progress bar
    bars = int(percentage/10)
    progress = "█"*bars + "-"*(10-bars)

    result = "Resume Score: "+str(round(percentage,2))+"%\n"
    result += "Progress: "+progress+"\n\n"

    result += "Matched Skills:\n"
    for skill in matched:
        result += "- "+skill+"\n"

    result += "\nMissing Skills:\n"
    for skill in missing:
        result += "- "+skill+"\n"

    # Project detection
    result += "\nDetected Project Keywords:\n"
    found_project = False

    for word in project_keywords:
        if word in resume_text:
            result += "- "+word+"\n"
            found_project = True

    if not found_project:
        result += "No projects detected\n"

    # Suggestions
    result += "\nSuggestions:\n"

    if "data structures" in missing:
        result += "- Learn Data Structures for interviews\n"

    if "git" in missing:
        result += "- Learn Git and GitHub\n"

    if "sql" in missing:
        result += "- Add SQL / Database skills\n"

    if "machine learning" in missing:
        result += "- Try learning Machine Learning basics\n"

    if percentage >= 80:
        result += "\nExcellent Resume 👍"
    elif percentage >= 50:
        result += "\nGood Resume but can improve"
    else:
        result += "\nResume needs improvement"

    text_box.insert(tk.END,result)


# GUI Window
window = tk.Tk()
window.title("Resume Analyzer")
window.geometry("550x500")

title = tk.Label(window,text="Resume Analyzer",font=("Arial",18))
title.pack(pady=10)

upload_button = tk.Button(window,text="Upload Resume PDF",command=analyze_resume)
upload_button.pack(pady=10)

text_box = tk.Text(window,height=22,width=65)
text_box.pack(pady=10)

window.mainloop()