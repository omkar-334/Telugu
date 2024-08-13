import random

system = "You are a Telugu AI designed to interpret and explain the meaning of Telugu figurative texts. You will be provided with a Telugu figurative text, and your task is to interpret this text, and answer in Telugu language only\n"

prompt1 = (
    system
    + "What does the expression '{}' mean, and in what context is it typically used? Provide an example scenario where this expression would be appropriately applied."
)
prompt2 = (
    system
    + "Explain the meaning of '{}'. How might this expression be used in a real-life conversation? Give an example to illustrate your explanation."
)
prompt3 = (
    system
    + "What is the significance of '{}'? Describe a situation in which this expression would be relevant and explain why."
)
prompt4 = (
    system
    + "What does '{}' imply? Provide a detailed explanation and an example of a scenario where this expression could be used effectively."
)
prompt5 = (
    system
    + "Analyze the meaning of '{}'. How can this expression be applied in everyday life? Illustrate your answer with a practical example."
)


def createPrompts(exp):
    prompts = [
        prompt1.format(exp),
        prompt2.format(exp),
        prompt3.format(exp),
        prompt4.format(exp),
        prompt5.format(exp),
    ]
    prompt = random.choice(prompts)
    return prompt


def create_requests(prompts: list[str], system: str):
    reqlist = [
        {
            "messages": [
                {
                    "role": "system",
                    "content": system,
                },
                {"role": "user", "content": prompt},
            ]
        }
        for prompt in prompts
    ]
    return reqlist


qtemplate = """You are given a question/ Rewrite and rephrase the question into a thoughtful detailed question. Ensure that the question stays relevant to the original question.

# Question - {}"""
