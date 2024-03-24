# Stage 1: Build frontend assets
FROM node:14 as frontend_build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Clear npm cache
RUN npm cache clean --force

# Install dependencies including react-scripts
RUN npm install react-scripts@4.0.3

# Copy the rest of the frontend files
COPY . ./

# Debugging: Print the contents of the working directory
RUN ls -al

# Debugging: Print the contents of package.json
RUN cat package.json

# Debugging: Print the contents of node_modules directory
RUN ls -al node_modules

# Build the frontend
RUN npm run build

# Stage 2: Serve frontend assets with NGINX
FROM nginx:latest

# Copy built assets from the first stage to NGINX server's HTML directory
COPY --from=frontend_build /app/build /usr/share/nginx/html

# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
