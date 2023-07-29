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


def predicate(document):
  """
  Checks if a document matches a predicate.

  Args:
    document: The document to check.

  Returns:
    True if the document matches the predicate, False otherwise.
  """

  raise NotImplementedError
