# Educhain based MCP Server (via Google Gemini)

This project devises an MCP server that handles various functions like: generating MCQs, flashcards, lesson-plans etc.,

## Structure
```bash
Claude Desktop(Front end) <-> MCP Server <-> LLM (google Gemini)
```

## Installation and Initialization
### Recommended Python version: 3.10
Packages Manager: [uv](https://docs.astral.sh/uv/) (Recommended) or [pip](https://pip.pypa.io/en/stable/)
### Step 0: Clone this repository
```bash
git clone Anudeep-CodeSpace/educhain_mcp_server.git
cd educhain_mcp_server
```
### Step 1: Install uv
```bash
pip install uv # universal
brew install uv # mac os only
```
### Step 2: Initialize project
```bash
uv init # initialize an already existing project
```
### Step 3: Add required packages
```bash
# They contain all the required sub -packages in them
uv add "educhain" "mcp[cli]"
```
### Step 4: Add your Google gemini api key
```python
# inside .env file
GOOGLE_API_KEY=<Your Google api key without quotes>
```
### Step 5: Debug your MCP server
```bash
uv run mcp dev main.py
```
It produces a **tokenised proxy server** at 
```txt
http://localhost:6274/?PROXY_API_TOKEN=<proxy token>
```
Paste it and navigate to the link in a browser.
Click "Connect" and you can debug your tools, resources and prompts in that site.
### Step 6: Install Claude Desktop app
Install [Claude Desktop app](https://claude.ai/download) and login with your account(can be new).
### Step 7: Add MCP server to Claude Desktop app
In the git repo folder run
```bash
# Adds the MCP Server to Claude Desktop client
uv run mcp install main.py
```

After that your **claude_desktop_config.json** should look like this:
```json
{
  "mcpServers": {
    "Educhain - MCP server": {
      "command": "absolute/path/to/uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "absolute/path/to/main/main.py"
      ]
    }
  }
}
```
### Final step: Check for any discrepancies in the logs
All the logs are located at:
```bash
%APPDATA%\\Claude\\logs\\mcp.log # in windows
~/Library/Logs/Claude/mcp.log # in macOS
```
### Metadata
get_info(`about://info`) resource lists out all the tools and resources provided by this server

## Key Characteristics of this project
**Modularity:** Separating the server initialization (server.py), route handling (handlers.py), and the main entry point (main.py) makes the codebase clean, scalable, and easy to maintain.

**Clear Schema Definitions:** Use of Pydantic models in the schema directory. It ensures strong data validation, clear API contracts, and self-documenting code for requests and responses.

**Dependency Injection:** Passing the mcp server instance to handler functions (handle_resources(mcp)) is a good practice. It avoids circular dependencies and global state issues.

**Use of Decorators:** The @mcp.resource and @mcp.tool decorators provide a clean and declarative way to define the server's capabilities.

## Known Issues
### Claude Desktop client cannot direclty access Resource Templates (Beta stage)
For Example Claude Desktop client cannot access the **generate_lessonplan** resource(`uri = lessonplan://{topic}`) cannot be used directly as it is in **beta** stage and doesn't support dynamic resource uri's!!!

So ``Generate a lesson plan to teach algebra`` cannot invoke the **generate_lessonplan** tools!
### Needs external LLM to generate content
Claude being a powerful llm cannot direclty generate content according to our tools and resources! (Hence I am using Gemini)

## Key Contributors
*Myself*(`Anudeep-CodeSpace`), Chatgpt, Perplexity AI, Gemini(Free LLM)

## Note
**Node js(LTS)** version is required for debugging
**pyenv is not recommended**(That wasted a lot of time for me 😭)