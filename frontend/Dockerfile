# Stage 1: Build frontend assets
FROM node:14 as frontend_build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Install dependencies including react-scripts
RUN npm install

# Copy the rest of the frontend files
COPY . ./

# Build the frontend
RUN npm run build

# Stage 2: Serve frontend assets with NGINX
FROM nginx:latest

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy built assets from the first stage to NGINX server's HTML directory
COPY --from=frontend_build /app/build ./

# Set permissions for static files
RUN chown -R nginx:nginx /usr/share/nginx/html

# Copy NGINX configuration file from the same directory
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
