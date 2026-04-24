from fastmcp import FastMCP

from hamqsl_mcp.hamqsl import mcp as hamqsl_mcp

mcp = FastMCP('HamServer')
mcp.mount(hamqsl_mcp, namespace='hamqsl')

def main():
    mcp.run()

if __name__ == '__main__':
    main()
