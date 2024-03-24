# Use Node.js 14 as the base image
FROM node:14 as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Build the application
RUN npm run build

# Use nginx as the base image for the production environment
FROM nginx:alpine

# Copy the built static files from the build stage to the nginx web root directory
COPY --from=build /app/build /usr/share/nginx/html

# Copy nginx.conf to the appropriate location
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Command to start nginx
CMD ["nginx", "-g", "daemon off;"]
