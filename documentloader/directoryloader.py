from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',#folder name
    glob='*.pdf',#which files to choose
    loader_cls=PyPDFLoader #depend on file types
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)