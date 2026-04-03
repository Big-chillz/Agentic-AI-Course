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

pattern 1 : Few-Shot
messages = [
    {
        "role" : "user",
        "content" : """
        Example 1 : 
        Q : If you have 2 oranges and 3 apples, how many total fruits?
        A : 5

        Example 2 : 
        Q : A pack of pens and you have 2 packs, how many total pens?
        A : 10

        Now Solve : 
        A store sells 5 packs of Eraser and 7 packs of pencil , each pack has 5 units , total how many units do we have?

        What combinatinos are possible?
        """
    }
]


pattern 2 : Chain-Of-Thought
messages = [
    {
        "role" : "user",
        "content" : """
        Task : 
        Find all combinations

        Instructions : 
        - step 1 : List possible counts of pencils and erasers
        - step 2 : Calculate or sum the total units available of both
        - step 3 : Provide all possible permutaions

        Question : 
        A store sells 5 packs of Eraser and 7 packs of pencil , each pack has 5 units , total how many units do we have?

        What combinatinos are possible?
        """
    }
]

pattern 3 : Output_format

messages = [
    {
        "role" : "user",
        "content" : """
        Example : 
        Q : 2 pack of pencils, 3 pack of erasers, and each pack has 5 units , total how many units?
        A : {
            "number of units in a packs" : 5,
            "pack of pencils" : 2,
            "pack of erasers" : 3
            "total units" = (2+3) * 5 = 15
        }

            A store sells 8 packs of seeds and 4 packs of fruits , each pack has 11 units , total how many units do we have?
    """
    }
]