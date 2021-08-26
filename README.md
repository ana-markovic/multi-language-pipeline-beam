# Multi-language word count - Apache Beam

This repository contains examples of Apache Beam's multilingual features. This particular example is a Java word count pipeline that calls a Python-based external transform. It is similar to the example in the following [link](https://beam.apache.org/documentation/patterns/cross-language/).
To execute the example locally, make sure that you: 

- have Docker installed 
- have Java 1.8 set as your default JRE
- have Python installed - Beam currently supports Python versions up to 3.8, here we use Python 3.7.3 


## Running the pipeline

Make sure Docker is started and start the **Job Server** which will translated into the stage that will run on your back-end or runner (here we used Spark):

```sh
docker run --network=host apache/beam_spark_job_server
``` 

Then, start the expansion service by navigating to `/examples/count/python` and running the following command: 

```sh
python expansion_service.py -p 9097
```

Once you get a message that expansion service is running at a specific port (currently, the port is set to 12345), you can proceed with executing the Java pipeline by navigating to `/examples/count/java` and running: 


```sh
mvn exec:java -Dexec.mainClass=apache.beam.app.Main -Dexec.args="--useExternal=true --runner=PortableRunner --expansionServiceURL=localhost:9097 --jobEndpoint=localhost:8099 --experiments=beam_fn_api"
```
