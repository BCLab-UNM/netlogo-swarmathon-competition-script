#!/bin/bash  
export CLASSPATH=${CLASSPATH}:/anaconda/share/py4j/py4j0.10.3.jar:/Applications/NetLogo5.2/NetLogo.jar
javac NetLogoBridge.java
java NetLogoBridge
