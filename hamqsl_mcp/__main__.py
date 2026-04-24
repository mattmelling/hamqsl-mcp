import argparse
from fastmcp import FastMCP

from hamqsl_mcp.hamqsl import mcp as hamqsl_mcp

mcp = FastMCP('HamServer')
mcp.mount(hamqsl_mcp, namespace='hamqsl')

def main():
    mcp.run()

def main_http():
    mcp.run(transport="http", host="127.0.0.1", port=8000)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('hamqsl-mcp')
    parser.add_argument('-u', '--http', action='store_true')
    args = parser.parse_args()
    if args.http:
        main_http()
    else:
        main()
