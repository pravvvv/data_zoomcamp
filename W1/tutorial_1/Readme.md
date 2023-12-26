# Exp 1

Create a docker file(Refer Dockerfile in the folder)  :
* image : python 3.9
* Run in bash : pip install pandas

Tip : Use 'Dockerfile' instead of 'DockerFile'

To build the image use :
```
$ docker build -t test:pandas .
``````

To run the image use :
```
$ docker run -it test:pandas

``````


# Exp 2

* image : python 3.9
* Run in bash : pip install pandas
* Docker file will copy pipeline.py to working folder ([PWD]/app)

To build the image use :
```
$ docker build -t test:pandas .
``````

To run the image use :
```
$ docker run -it test:pandas
$ python pipeline.py

``````


# Exp 3

* image : python 3.9
* Run in bash : pip install pandas
* Docker file will copy pipeline.py to working folder ([PWD]/app)
* It opens at python entrypoint and runs "pipeline.py"

To build the image use :
```
$ docker build -t test:pandas .
``````

To run the image use :
```

$ docker run -it test:pandas 2021-12-01 
```
It will print the output as :

```
"Job ran successfully for day <date passed>"
```




