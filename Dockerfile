# Docker container for building the CosmOS documentation pages.

FROM alpine:latest

RUN apk add --no-cache bash doxygen py3-pip python3 make git
RUN pip3 install GitPython
