::it's important to leave the JARs where they install, as the NetLogo.jar file has a dependency on a specific (old) version of Scala
::that is included and referenced in a relative path

javac -cp "C:\Program Files (x86)\Python36-32\share\py4j\py4j0.10.4.jar;C:\Program Files (x86)\NetLogo 5.2.0\NetLogo.jar" NetLogoBridge.java

::opens a second command line prompt to run python script
start cmd /k python HSDivisionTeamValidationScript_P3.py test.nlogo pause

java -cp "C:\Program Files (x86)\Python36-32\share\py4j\py4j0.10.4.jar;C:\Program Files (x86)\NetLogo 5.2.0\NetLogo.jar;." NetLogoBridge
pause
