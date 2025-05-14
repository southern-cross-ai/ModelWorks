# Takes a query and returns a concatonated string of relevant text
def retrieve(query: str, k, embedding_model, vector_db):
    query_embedding = embedding_model.embed_query(query)
    docs = vector_db.similarity_search_by_vector(query_embedding, k=k)
    return [doc.page_content for doc in docs]