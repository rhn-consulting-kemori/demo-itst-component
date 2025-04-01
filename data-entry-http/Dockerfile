# Use OpenJDK 17 as the base image
FROM registry.access.redhat.com/ubi9/openjdk-17

# Set working dir
WORKDIR /app
COPY target/camel-service-1.0-SNAPSHOT.jar app.jar
COPY data/ /app/data

USER root
RUN chgrp -R 0 /app/data && chmod -R g=u /app/data
USER 1001

# Expose the port that your Spring Boot application listens on
EXPOSE 8180

# Command to run the application
CMD ["java", "-jar", "app.jar"]