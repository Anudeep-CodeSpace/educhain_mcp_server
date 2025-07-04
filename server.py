from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
import os

### Connect any LLM for content and question generation ###
load_dotenv()
# Using gemini 1.5 flash llm model
gemini_model = ChatGoogleGenerativeAI(
	model="gemini-1.5-flash",
	api_key=os.getenv("GOOGLE_API_KEY")
)
flash_config = LLMConfig(custom_model=gemini_model)
llm_client = Educhain(config=flash_config) # this can execute prompts

mcp = FastMCP("Educhain - MCP server")

