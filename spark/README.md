# Article on Medium that teachs how to make a spark cluster:
https://medium.com/@SaphE/testing-apache-spark-locally-docker-compose-and-kubernetes-deployment-94d35a54f222

# Build image
```
docker build -t our-own-apache-spark:3.5.3 .
```

# Run Spark
```
docker compose up
```

# Enter on master container
```
docker exec -i -t bb0c08208d7a /bin/bash
```
