# Use the nginx image as the base image
FROM nginx

# Set the working directory
WORKDIR /server

# Copy the nginx configuration file to the nginx server
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf


# Expose the port that nginx will listen on
EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]