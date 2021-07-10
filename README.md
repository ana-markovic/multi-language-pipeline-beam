# Multi-language word count - Apache Beam

This repository contains examples of Apache Beam's multilinual features. This particular example is a Python word count pipeline that calls a Java-based external transform. 
To execute the example locally, make sure that you: 

- have Docker installed and running (no need to pull a specific image/start a particular container)
- have Java 1.8 set as your default JRE
- have Python installed - Beam currently supports Python versions up to 3.8, here we use Python 3.7.3 


## Running the pipeline

Make sure Docker is started. Navigate to `/examples/count` and run: 


```sh
sh ./start_expansion_service.sh
```
This will package the external transform into a JAR file and run it. 

Once you get a message that expansion service is running at a specific port (currently, the port is set to 12345), you can proceed with setting up a virtial environment for executing Python code: the Python version should be set to 3.7.3 and ```apache_beam``` package has to be installed. Afterwards, the ```wordcount.py``` program can be run. To do so, execute the following script in another terminal session:

```sh
sh ./run_direct_runner.sh
```
