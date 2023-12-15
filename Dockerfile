# this docker file is aimed to make a proxy server that use nginx to proxy the request to the backend server

# use the nginx image as the base image
FROM nginx

# make app directory
WORKDIR /server

# install the dependencies
# install pip 
RUN apt-get update
RUN apt-get -y install python3-pip


# install flask 
RUN apt-get -y install python3-flask

ADD . .


# initialize the nginx server
RUN nginx -c /etc/nginx/nginx.conf

# copy the nginx configuration file to the nginx server
COPY nginx.conf /etc/nginx/nginx.conf

# start the nginx server
CMD ["python3", "server.py"]