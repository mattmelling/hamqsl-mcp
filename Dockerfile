FROM python:3.12.8-slim-bookworm
RUN apt-get update && apt-get install -y python3-setuptools python3-venv python3-pip
RUN mkdir -p /opt/hamqsl-mcp 
ADD . /opt/hamqsl-mcp
RUN python3 -m venv /opt/hamqsl-mcp/venv
RUN /opt/hamqsl-mcp/venv/bin/pip install /opt/hamqsl-mcp
RUN apt-get clean
CMD ["/opt/hamqsl-mcp/venv/bin/hamqsl-mcp"]