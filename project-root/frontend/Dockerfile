FROM node:24-alpine

# Install only essential packages and clean cache in one layer
RUN apk add --no-cache --update \
    curl \
    && rm -rf /var/cache/apk/*

# Configure npm for better network connectivity
RUN npm config set registry https://registry.npmjs.org/ && \
    npm config set fetch-retries 5 && \
    npm config set fetch-retry-mintimeout 20000 && \
    npm config set fetch-retry-maxtimeout 120000

WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies with retry mechanism
RUN npm ci --no-audit --no-fund || npm ci --no-audit --no-fund || npm ci --no-audit --no-fund

# Copy source code
COPY . .

# Build the app for production
RUN npm run build

# Install serve to run the built app with retry mechanism
RUN npm install -g serve --no-audit --no-fund || npm install -g serve --no-audit --no-fund || npm install -g serve --no-audit --no-fund

EXPOSE 3000

# Serve the built app
CMD ["serve", "-s", "build", "-l", "3000"]
