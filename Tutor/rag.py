from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# cargar documentos
loader = TextLoader("conocimiento.txt", encoding="utf-8")
documents = loader.load()

# dividir en chunks
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# base vectorial
vectorstore = FAISS.from_documents(docs, embeddings)

# función para obtener contexto
def obtener_contexto(pregunta):
    resultados = vectorstore.similarity_search(pregunta, k=2)
    contexto = "\n".join([doc.page_content for doc in resultados])
    return contexto
query = "What is the verb to be?"

resultados = vectorstore.similarity_search(query, k=2)

print("\nRESULTADOS DEL RAG:\n")

for r in resultados:
    print(r.page_content)
    print("-----")