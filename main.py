# main.py
# entrypoint to the server
from handlers import handle_resources, handle_tools
from server import mcp

# Register handlers before main method
handle_resources(mcp)
handle_tools(mcp)

if __name__ == '__main__':
	print("Starting mcp server....")
	mcp.run()