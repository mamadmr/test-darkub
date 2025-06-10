# Use the nginx image as the base image
FROM nginx:latest

# Set the working directory
WORKDIR /server

# Copy the nginx configuration file to the nginx server
COPY default.conf   /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443
EXPOSE 8080


# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]