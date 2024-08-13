import re
from urllib import parse

import requests
from bs4 import BeautifulSoup, Comment, Declaration


def is_article_text(element):
    if element.parent.name in ["style", "script", "[document]", "head", "title"]:
        return False
    elif re.match("<!--.*-->", str(element)):
        return False
    elif type(element) is Comment or type(element) is Declaration:
        return False
    elif len(str(element)) < 200:
        return False
    return True


import time

questions = []
answers = []

for section in range(7):
    for page in range(10):
        url = f"https://www.examveda.com/state-gk/practice-mcq-question-on-telangana/?section={section+1}&page={page+1}"
        for t in range(3):
            try:
                time.sleep(2**t)
                soup = BeautifulSoup(requests.get(url).content, "html.parser")
                q = [
                    i.text
                    for i in soup.findAll("div", attrs={"class": "question-main"})
                ]
                a = [
                    [j.text.replace("\n", "").strip() for j in i.findAll("p")]
                    for i in soup.findAll(
                        "div", attrs={"class": "form-inputs clearfix question-options"}
                    )
                ]

                if len(q) == len(a):
                    print(f"{section+1}-{page+1}")
                    questions.extend(q)
                    answers.extend(a)
                    break
            except:
                pass


def xfil(x):
    return list(filter(None, x))


answers2 = [xfil(i) for i in answers]

import pandas as pd

df = pd.DataFrame({"Q": questions, "A": answers2})
df["A"], df["B"], df["C"], df["D"] = zip(*answers2)
for i in ["A", "B", "C", "D"]:
    df[i] = df[i].str.replace(f"{i}. ", "")

mask = df["Q"].str.contains(
    "written|poetry|books|authors|wrote|book", case=False, na=False, regex=True
)

# Drop rows where the mask is True
dfc = df[~mask]
