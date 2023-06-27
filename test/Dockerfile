FROM python:3.8.4-slim AS base

WORKDIR /src
COPY main.py ./

######
## Debugger
######

FROM base as debugger

RUN pip install debugpy

ENTRYPOINT [ "python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "main.py"]

#######
### Primary
#######

FROM base as primary

ENTRYPOINT [ "python", "main.py"]
