from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_chroma import Chroma
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from uuid import uuid4
from langchain_text_splitters import RecursiveCharacterTextSplitter

embeddings = NVIDIAEmbeddings(model='nvidia/nv-embedqa-e5-v5')
print("Embedding model initailized")
collection_name =str(input("Enter the collection_name you want to give :- "))
persist_directory = str(input("Enter the path to create you vector database :- "))
vector_store = Chroma(
    collection_name= collection_name,
    embedding_function= embeddings,
    persist_directory= persist_directory,  # Where to save data locally, remove if not necessary
)
print("Database Folder created")

file_path="PDF_File_path.pdf"

loader = PyPDFLoader(file_path)
document = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunked_documents = text_splitter.split_documents(document)
print("Chunk Created")

uuids = [str(uuid4()) for _ in range(len(chunked_documents))]
vector_store.add_documents(documents=chunked_documents, ids=uuids)
print('PDF Added')


