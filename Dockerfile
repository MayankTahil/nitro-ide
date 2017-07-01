FROM kdelfour/cloud9-docker
MAINTAINER Mayank Tahilramani from Citrix Technical Secialist 

# Install dependencies
RUN apt-get -y update && apt-get -y install python-pip git python-setuptools wget && rm -rf /var/lib/apt/lists/*

# Make temporary folder and install SDK's and clean up
RUN mkdir /stage
COPY ./ /stage
RUN pip install -r /stage/requirements.txt
RUN cd /stage/nitro-python-1.0 ; python setup.py install
RUN cd /stage/mas_nitro-python-1.0 ; python setup.py install
RUN rm -r /stage

# Install gitui for git management
WORKDIR /workspace
RUN wget -O - https://raw.githubusercontent.com/alberthier/git-webui/master/install/installer.sh | bash ; git -b cpx-101 clone https://github.com/Citrix-TechSpecialist/NetScalerNITRO.git

# Cloud 9 IDE
EXPOSE 80
# Gitui interface
EXPOSE 8000

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
	