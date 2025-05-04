FROM node:20

WORKDIR /app

# installing pnpm (kiota-typescript uses this) and dependencies
RUN npm install -g pnpm
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

# cloning kiota-typescript repo
RUN git clone --branch main https://github.com/microsoft/kiota-typescript.git .

# keep getting warnings without a pnpm workspace file so just making a dummy file
RUN echo "packages:\n  - 'packages/*'" > pnpm-workspace.yaml

RUN pnpm install
RUN cd packages/serialization/json && pnpm add uuid

# creating wrapper test file to import both test files we want to run
RUN cd packages/serialization/json/test && \
    echo "import '../../text/test/common/textParseNode.ts';" > runSelectedTests.test.ts && \
    echo "import './common/JsonParseNode.ts';" >> runSelectedTests.test.ts

# run both textParseNode and jsonParseNode tests
CMD ["pnpm", "vitest", "run", "runSelectedTests.test.ts"]