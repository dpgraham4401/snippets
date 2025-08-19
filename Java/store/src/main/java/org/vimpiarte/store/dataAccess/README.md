# Access Data in Databases

Java has several was to implement our data access layer

1. JDBC - Java DataBase Connectivity - The standard API for connecting with DB's 
    - We have to manually manage everything, prepare SQL statement, execute them, open/close the connections. 
    - If we miss any of these steps, we're going to run into issues.
    - It's powerful but low level and verbose
2. JPA - Jakarta Persistence API
    - Higher level API
    - It's a specification for mapping Java objects to DB tables (like an ORM)
    - We don't write SQL, we usually write these operations in Java.
    - it's just a specification
      - we have to use one of it's implementation like Hibernate (most popular), OpenJPA, others.
      - Adds caching, adds a powerful Query language, automatic schema generation
3. Spring Data JPA
    - One of the spring projects, built on JPA, simplifies JPA further.
    - Allows us to create repository interfaces and we get a lot of data access out of the job
