#####FROM openjdk:8-jdk-alpine
#WORKDIR /app
#COPY ./target/atm-machine.jar /app.jar
#RUN mvn clean package
#CMD ["java", "-jar" , " app.jar"]

##### Étape 1 : Utilisez une image Maven pour construire votre application
#FROM maven:3.8.1-openjdk-8-slim AS build
#WORKDIR /app
#COPY ./ /app
#RUN mvn clean package

##### Étape 2 : Utilisez une image OpenJDK Alpine légère pour exécuter votre application
#FROM openjdk:8-jdk-alpine
#WORKDIR /app
#COPY --from=build /app/target/atm-machine.jar /app.jar
#CMD ["java", "-jar", "app.jar"]


FROM openjdk:11
WORKDIR /app
COPY ./src/main/java/com/example/*.java /app/
COPY ./src/main/java/com/example/*.java /app/
RUN javac Account.java ATM.java OptionMenu.java
CMD ["java", "ATM"] 