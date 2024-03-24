# Stage 1: Build frontend assets
FROM node:14 as frontend_build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Install dependencies including react-scripts
RUN npm install react-scripts@4.0.3

# Copy the rest of the frontend files
COPY . ./

# Build the frontend
RUN npm run build

# Stage 2: Serve frontend assets with NGINX
FROM nginx:latest

# Copy built assets from the first stage to NGINX server's HTML directory
COPY --from=frontend_build /app/build /usr/share/nginx/html

# Copy NGINX configuration file from the frontend directory
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
