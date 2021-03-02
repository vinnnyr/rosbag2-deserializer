FROM ros:rolling
COPY deserialize.py /opt/deserialize.py
SHELL ["/bin/bash", "-c"]