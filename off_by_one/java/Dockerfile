FROM maven:3.9.9-eclipse-temurin-21

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        nano \
        vim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone https://github.com/eclipse-jdt/eclipse.jdt.debug.git . && \
    git checkout 093343f751b4b7d06046cdaef60caef7f159c18f

RUN mvn clean install -DskipTests

# run only LineTrackerTests
CMD ["mvn", "test", "-Dtest=org.eclipse.jdt.debug.tests.core.LineTrackerTests"]