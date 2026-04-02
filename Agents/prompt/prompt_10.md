# by default template

messages = [
    {
        "role" : "system",
        "content" : "Give me information in point form"
    },
    {
        "role" : "user",
        "content" : "Give me some information on the job loss due to AI"
    }
]


# one of the most : 

messages = [
    {
        "role" : "system",
        "content" : """
        You are an Expert AI and ML Tutor.

        Constraints / Rules :
        - Explain in terms of theoritical
        - Don't Exagerate
        - Give me mini tasks for topics

        Output format : 
        - Give it in synapses format
        - Give me mcq based questions
        """
    },
    {
        "role" : "user",
        "content" : """
        Task :
        Explain me about Transformer Architecture

        Constraints/Rules : 
        - simple language
        - cover a lot of technical keywords and explain
        - Ask questions to test myself
        """
    }
]


# another important template : 
messages = [
    {
        "role" : "system",
        "content" : "You are a critical reviewer"
    },
    {
        "role" : "user" ,
        "content" : "Explain in 2 points"
    },
    {
        "role" : "assistant",
        "content" : "AI is advanced version of ML"
    },
    {
        "role" : "user",
        "content" : "Review the above answer"

    }
]