# Use the nginx image as the base image
FROM nginx:latest

# Set the working directory
WORKDIR /server

# Copy the nginx configuration file to the nginx server
COPY nginx.conf     /etc/nginx/nginx.conf
COPY default.conf   /etc/nginx/conf.d/default.conf


# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]