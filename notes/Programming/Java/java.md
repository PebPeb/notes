
Compiles java project and outputs into bin folder

``` bash
javac -d bin/ src/App.java
```

Compiles files in bin/ folder into a .jar
This requires setting up the manifest.txt folder

``` bash
jar cfm FirstJavaProject.jar manifest.txt -C bin .
```
