import pandas as pd
from dataformer.llms.asyncllm import AsyncLLM
from googletrans import Translator

from prompts import create_requests, qtemplate

trans = Translator()

api_key = ""
llm = AsyncLLM(api_key, api_provider="openai")

df = pd.read_csv("QA.csv")

prompts = [qtemplate.format(row[0]) for idx, row in df.iterrows()]

reqlist = create_requests(
    prompts,
    "You are a history question-maker. You have to phrase questions related to Telugu History and Culture.",
)

responses = llm.generate(reqlist)
EQ = [response[1]["choices"][0]["message"]["content"] for response in responses]
TQ = trans.translate(EQ, dest="te", src="en")

reqlist = create_requests(
    TQ,
    "You are a historian with expertise in Telugu History and Culture. Answer in Telugu",
)

responses = llm.generate(reqlist)
TA = [response[1]["choices"][0]["message"]["content"] for response in responses]
EA = trans.translate(EQ, dest="te", src="en")

df["TQ"], df["EQ"], df["TA"], df["EA"] = TQ, EQ, TA, EA
df.to_csv("QA2.csv")
