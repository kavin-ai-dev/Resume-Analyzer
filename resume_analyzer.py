import PyPDF2 
with open("KavinCV.pdf","rb") as file:
    reader=PyPDF2.PdfReader(file)
    text=""
    for page in reader.pages:
     text=text+page.extract_text()
keywordlist={
    "python":30,
    "AI":25,
    "Machine learning":15,
    "Deep Learning":15,
    "Gen AI":15,
    "NLP":15,
    "Cloud":20,
    "AWS":15,
    "Azure":15,
    "Data science":25,
    "SQL":20,
    "Java":30,
    "C++":10,
    "Prompt engineering":10,
    "HTML":15
    }
score=0
points_per_keyword=25
missing_keywords=[]
for keyword in keywordlist:
    if keyword.lower() in text.lower():
       print(f"Yes {keyword} is present\n")
       score=score+keywordlist[keyword]
    else:
       print(f"No '{keyword}' was not found\n")
       missing_keywords.append(keyword)
total_score=sum(keywordlist.values())
percentage=(score/ total_score)*100
if percentage>=80:
   rating="Excellent⭐"
elif percentage >=60:
   rating="Good👍"
elif percentage>=40:
   rating="Average⚠️"
else:
   rating="Poor❌"
print(f"Final resume score:{score}/{total_score}\n")
print(f"Percentage:{percentage:.2f}%")
print(f"Rating:{rating}\n")
if missing_keywords:
   print("You should add these skills in your resume to improve:\n","," .join(missing_keywords))
else:
   print("Great! Your resume has all the keywords\n")
