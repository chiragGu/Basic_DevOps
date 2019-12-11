# Basic_DevOps


[![Build Status](https://travis-ci.com/chiragGu/Basic_DevOps.svg?branch=master)](https://travis-ci.com/chiragGu/Basic_DevOps)

## This repository contains following files:
  - .travis.yml for Travis CI 
  - dock1 folder:
        -Dockerfile
        -basic.py 
        -basic_test.py

### Dockerfile

  It contains all the necessary configurations to run a python image on docker.

### basic file

  It is a simple python program to convert binary to deciaml and decimal to binary. It was kept simple for more clear implementation of DevOps.


### basic_test file

  This is the file which contains total of 12 test cases for the 2 functions created in basic python file.
  
  
  
### Installation

For the docker implementation:
    -- First clone the project
    -- Go to the project directory
```sh
$ docker build .
```
-- After this it should get a result as Successfully built 'container ID' 

    $ docker run container ID

For Travis CI 
-- I have attached the required screnshots of test cases successfully passing. 

