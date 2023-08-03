all_documents = [
    {"title": "Document 1", "content": "This is the content of Document 1."},
    {"title": "Document 2", "content": "This is the content of Document 2."},
    {"title": "Document 3", "content": "This is the content of Document 3."},
    # Add more documents here...
]

class Query:
    def __init__(self):
        self.predicates = []

    def add_predicate(self, predicate_func):
        self.predicates.append(predicate_func)

def search(query):
    """
    Searches for documents that match the given query.

    Args:
        query: The query to search for.

    Returns:
        A list of the documents that match the query.
    """
    documents = []
    for document in all_documents:
        if all(predicate(document) for predicate in query.predicates):
            documents.append(document)

    return documents

def predicate_title_contains(document, keyword):
    """
    Predicate to check if the title of a document contains the given keyword.

    Args:
        document: The document to check.
        keyword: The keyword to search for in the title.

    Returns:
        True if the title contains the keyword, False otherwise.
    """
    return keyword.lower() in document["title"].lower()

def predicate_content_contains(document, keyword):
    """
    Predicate to check if the content of a document contains the given keyword.

    Args:
        document: The document to check.
        keyword: The keyword to search for in the content.

    Returns:
        True if the content contains the keyword, False otherwise.
    """
    return keyword.lower() in document["content"].lower()

# Example usage:
query = Query()
query.add_predicate(lambda doc: predicate_title_contains(doc, "Document"))
query.add_predicate(lambda doc: predicate_content_contains(doc, "content"))

result = search(query)
for doc in result:
    print(doc)
