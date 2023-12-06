from .llm import LLM


def get_subgoals(query):
    llm = LLM()
    prompt = """
    You are an assistant that considers the user query as a task,
    and devides achiving that task into proper sub-task steps.
    Don't write too many or too few steps.
    
    Output: the sub-tasks of the task

    Format Output: a json list of sub-tasks with keys:
    name: a name for the subtask, up to 5 words.
    summary: a brief description of the subtask, up to 100 words.
    """
    return llm.get_output(prompt=prompt, query=query)


def get_related_goals(query):
    goals = ""
    llm = LLM()
    prompt = f"""
    You are an assistant that gets a new message from the user,
    and decides if this new information is related to any of given tasks for that user
    the user tasks are:
    {goals}
    
    Output: up to 3 top relevent goals
    
    Format Output: a json list of object with keys:
    id: id of the task
    name: name of the task
    score: the probability between 0.00 to 1.00 that indicates if the information is related to the task
    """

    return llm.get_output(prompt=prompt, query=query)


def get_related_people(query):
    llm = LLM()
    people = ""
    prompt = f"""
    You are an assistant who finds the people mentioned in the query and outputs them.
    Return an empty list if nobody was mentioned.
    The list of people:
    {people}

    Output: people who were mentioned in the query
   
    Format Output: a json list of people with keys:
    id: id of the person
    name: name of the person
    reference: the part of query that match the name
    """

    return llm.get_output(prompt=prompt, query=query)
