import components.retrieve as retrieve
import components.llm as llm
import components.history as history

# primary function
def call(query: str, messages: list = []):
    history_aware_query = history.contextualize(query, messages)

    context = retrieve.retrieve(history_aware_query)

    if context != []:
        contextualized_query = format(history_aware_query, context)
        llm_response = llm.call(contextualized_query)
    else: 
        llm_response = llm.call(history_aware_query)

    return llm_response

def format(query: str, context: str):
    # to be implimented
    return query
