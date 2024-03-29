import csv 
import chromadb

documents = []
metadata = []
ids = []

id = 0
with open('menu_items.csv') as file:
    lines = csv.reader(file)

    for i, line in enumerate(lines):
        if i == 0:
            continue

        documents.append(line[1])
        metadata.append({"item_id": line[0]})
        ids.append(str(id))
        id+=1



chroma_client = chromadb.Client()

# chroma_client.delete_collection(name="my_collection")

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=documents,
    metadatas=metadata,
    ids=ids
)

results = collection.query(
    query_texts=["shrimp"],
    n_results=2,
    include = ['documents']
)
print("database: ", collection)
print("results: ", results)