# Base Image
FROM python:3.7

# MAINTAINER INFO
MAINTAINER jackson.zhang1@hotmail.com

# Configure the user as root
User root

# Port Expose Configurations
EXPOSE 8000
EXPOSE 8001
# Port Expose for Supervisord
# EXPOSE 9001

# Configure the Proxy for this image.
# Please change it based on your own Host Env.
ENV workdir=/opt/Thunes/
#	http_proxy=http://xxxxx:xxxx\
#	https_proxy=http://xxxx:xxxx
 
# Configure The Working Dir
WORKDIR $workdir

# Add the Extra File 
ADD APISecret.ini ../APISecret.ini
ADD APISecret.ini ./APISecret.ini
ADD requirements.txt ./requirements.txt
ADD supervisord.conf ./conf/supervisord.conf


# Update the PIP Installation
# PIP Install ShopSite Package And Its Requirements
RUN pip install --upgrade pip\
 && pip install -r requirements.txt

WORKDIR $workdir/thunes/

# Update the ShopSite Package
RUN pip install thunes
RUN pip install --target=. thunes

WORKDIR $workdir

# Add the entrypoint sh and change its ownships
ADD run_supervisord.sh ./run_supervisord.sh
RUN chmod 766 ./run_supervisord.sh 

# Unset the proxy
#ENV http_proxy=""\
#	https_proxy=""
