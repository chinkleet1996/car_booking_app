# Use Node.js image as a base
FROM node:14-alpine

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source files
COPY . .

# Build the app
RUN npm run build

# Serve the app using nginx
FROM nginx:alpine
COPY --from=0 /usr/src/app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
