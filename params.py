# Env settings
set_visible_devices = True
visible_devices = '2,3'

#LLM parameters
#model_name = "eachadea/vicuna-13b-1.1"
#model_name = "lmsys/vicuna-13b-v1.3"
model_name = "lmsys/vicuna-13b-v1.5-16k"
tokenizer_path = "./tokenizer/%s" %model_name.split("/")[1]

seq_lengths = {"lmsys/vicuna-13b-v1.3" : 2048,
               "lmsys/vicuna-13b-v1.5-16k" : 16384}
seq_length = seq_lengths[model_name]


#Embedding model parameters
embedding_model_name =   "all-mpnet-base-v2" #Highest scoring all-round, does 2800 sentences/s
#embedding_model_name = "all-MiniLM-L6-v2" #93% of best score, 5X faster
chunk_size = 1024 #Size of chunks to break the text store into
chunk_overlap = 128 #How much overlap between chunks

init_docs = True #Recompute embeddings?
overwrite_embeddings = True #Overwrite embeddings if already exist? -- will raise val error of init_docs is True and this is not
N_hits = 4 #How many hits of context to provide?


#List of folders to add to doc store
doc_paths = ["DOC_STORE/APS-Science-Highlight", 
             "DOC_STORE/APS-Docs", 
             "DOC_STORE/ALCF-Docs",
             "DOC_STORE/CNM-Science-Highlight"]


#Embedding paths
base_path = 'embeds/' 
embed_path = '%s/%s' %(base_path, embedding_model_name)
pdf_path = '%s/pdf' %embed_path
