# this docker file is aimed to make a proxy server that use nginx to proxy the request to the backend server

# use the nginx image as the base image
FROM nginx

# make app directory
WORKDIR /server


# copy the nginx configuration file to the nginx server

COPY nginx.conf /etc/nginx/nginx.conf

# start the nginx server
CMD ["nginx", "-g", "daemon off;"]