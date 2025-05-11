# Use Node.js as the base image
FROM node:20-alpine

# Install git (needed for cloning)
RUN apk add --no-cache git

# Set working directory in the container
WORKDIR /app

# Clone the repository (replace with your repository URL)
RUN git clone https://github.com/RohithNair27/Client-Authentication.git .
RUN git checkout fae9a4e


# If your repo requires submodules, uncomment the line below
# RUN git submodule update --init --recursive

# Install dependencies
WORKDIR /app/React
RUN npm install

# Build the application
RUN npm run build

# Expose the port the app will run on
EXPOSE 5173

# Command to run the application
CMD ["npm", "run", "dev"]