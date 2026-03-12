# Resume Analyzer (Python GUI)

A Python GUI application that analyzes a resume (PDF) and evaluates it based on technical skills and project keywords.

## Description

This tool allows users to upload their resume in PDF format and automatically checks for important technical skills such as Python, Java, Data Structures, SQL, and Machine Learning.
It calculates a resume score, highlights matched and missing skills, detects project keywords, and provides suggestions for improvement.

## Features

* Upload resume in **PDF format**
* Automatic **skill detection**
* **Resume score calculation**
* Shows **matched and missing skills**
* Detects **project-related keywords**
* Provides **improvement suggestions**
* Simple **Tkinter GUI interface**

## Technologies Used

* Python
* Tkinter (GUI)
* PyPDF2 (PDF reading)
* Regular Expressions (re module)

## Project Structure

```
resume-analyzer
│
├── resume_analyzer.py
├── sample_resume.pdf
└── README.md
```

## Installation

Install the required library:

```
python -m pip install PyPDF2
```

## How to Run

Run the Python file:

```
python resume_analyzer.py
```

Then:

1. Click **Upload Resume PDF**
2. Select your resume file
3. The application will display the **analysis results**

## Output Includes

* Resume score percentage
* Progress bar
* Matched skills
* Missing skills
* Detected project keywords
* Suggestions for improvement

## Future Improvements

* Add support for **DOCX resumes**
* Export analysis results as **PDF report**
* Add **AI-based resume suggestions**
* Improve skill database

## Author

Created as a practice project for learning **Python GUI development and resume analysis tools**.

