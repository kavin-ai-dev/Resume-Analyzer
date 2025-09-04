# Resume Analyzer 📝

A Python project that analyzes resumes in PDF format and scores them based on important job-related keywords.  
It helps you identify missing skills and improve your resume for tech roles like AI, Python, Cloud, and more.

---

## Features
- Extracts text from PDF resumes using PyPDF2
- Checks for keywords like Python, AI, SQL, Cloud, AWS, Azure, Java, etc.
- Calculates:
  - Total Score
  - Percentage
  - Rating (Excellent ⭐, Good 👍, Average ⚠️, Poor ❌)
- Suggests missing skills to improve your resume

---

## Example Output
Yes Python is present
Yes AI is present
No 'Machine learning' was not found
No 'Cloud' was not found
Yes SQL is present
No 'Java' was not found

Final Resume Score: 90/260
Percentage: 34.62%
Rating: Poor ❌

You should add these skills in your resume to improve:
Machine learning, Cloud, Java

---

## Tech Stack
- Python
- PyPDF2

---

## How to Run
1. Clone the repo:  
   ```bash
   git clone https://github.com/YOURUSERNAME/Resume-Analyzer.git


Install dependencies:

pip install PyPDF2


Run the code:

python resume_analyzer.py


Make sure your resume PDF (e.g., KavinCV.pdf) is in the same folder as the code.

Author

👨‍💻 Kavin Prasanna S S
LinkedIn Profile
 (www.linkedin.com/in/kavin-prasanna-s-s-b8938031b)

