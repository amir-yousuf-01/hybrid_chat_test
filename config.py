# config_example.py — copy to config.py and fill with real values.
NEO4J_URI = "neo4j+s://14d4007c.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

OPENAI_API_KEY = "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" # your OpenAI API key

PINECONE_API_KEY = "pcsk_3ipniZ_DpJPkS2omZCbcmQen9z5jbjvX6WHH47Ymyn3dXk8s929fPVuQQUdt23tzo3Ek6t6" # your Pinecone API key
PINECONE_ENV = "us-east1-aws"   # example
PINECONE_INDEX_NAME = "vietnam-travel"
PINECONE_VECTOR_DIM = 1536       # adjust to embedding model used (text-embedding-3-large ~ 3072? check your model); we assume 1536 for common OpenAI models — change if needed.
