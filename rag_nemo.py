import os
import sys
import nest_asyncio
nest_asyncio.apply()
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
sys.path.append("../NeMo-Guardrails")
from nemoguardrails import RailsConfig, LLMRails
os.environ["NVIDIA_API_KEY"] = "APIKEY"
embeddings = NVIDIAEmbeddings(base_url="http://192.168.100.64:2000/v1",model='nvidia/nv-embedqa-e5-v5')
vect = Chroma(persist_directory=persist_directory, embedding_function=embeddings,collection_name=collection_name)
CNretriever = vect.as_retriever()
config = RailsConfig.from_path("config")
rails = LLMRails(config)
prompt_template = """You are a helpful Computer Network bot  for our teaching institute . Only answer if your have got content in "Context".
Otherwise tell the user in a friendly way that you do not know and can not help with that.
Context: {context}
Question: {question}
Answer here:"""
PROMPT = PromptTemplate(template=prompt_template,input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}
CNqa = RetrievalQA.from_chain_type(llm=rails.llm,chain_type="stuff",retriever=CNretriever,chain_type_kwargs=chain_type_kwargs)
rails.register_action(CNqa, name="qa_chain")
input1 = str
while input1 != "bye":
    input1 = str(input("Enter the Question :- ") )
    history = [{"role": "user","content": input1}]
    response = rails.generate(messages=history)
    print(response['content'])
