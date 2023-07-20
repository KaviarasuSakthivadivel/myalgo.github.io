An inverted index is a data structure used in search engines that allows for fast full-text searches. It is called "inverted" because it inverts a mapping of words to documents into a mapping of documents to words.

In an inverted index, each unique word in a set of documents is assigned a unique identifier called a term ID. For each document in the set, the index records which terms occur in that document, along with their frequency. This information is usually stored in a hash table or a search tree.

Elasticsearch is a search engine that uses an inverted index to store and search data. When you index data in Elasticsearch, it tokenizes the text and creates an inverted index for each token. This means that when you search for a term, Elasticsearch can quickly look up all the documents that contain that term by consulting the inverted index.

In addition to searching for exact terms, Elasticsearch can also perform full-text search, phrase search, and fuzzy search. It can also perform relevance scoring to rank the search results based on how well they match the search query.

Overall, the inverted index is a powerful tool for enabling fast and efficient searching in Elasticsearch, making it a popular choice for applications that require full-text search capabilities.

Suppose we have the following three documents:

```java
Doc 1: The quick brown fox
Doc 2: The quick brown dog
Doc 3: The lazy brown dog
```

We want to create an inverted index for these documents. Here's how that might work:

1. First, we tokenize the documents by breaking them up into individual words:

```java
Doc 1: The quick brown fox -> [the, quick, brown, fox]
Doc 2: The quick brown dog -> [the, quick, brown, dog]
Doc 3: The lazy brown dog  -> [the, lazy, brown, dog]
```

1. Next, we create a dictionary of all the unique words in the documents, along with a posting list that indicates which documents contain each word:

```json
{
  "the": [1, 2, 3],
  "quick": [1, 2],
  "brown": [1, 2, 3],
  "fox": [1],
  "dog": [2, 3],
  "lazy": [3]
}
```

Here, the key of each entry in the dictionary is a unique word, and the value is a list of document IDs where that word appears.

1. Finally, we can use the inverted index to quickly find documents that match a query. For example, if we search for the term "quick brown", we can use the posting lists to find all the documents that contain both the word "quick" and the word "brown", which in this case would be documents 1 and 2.