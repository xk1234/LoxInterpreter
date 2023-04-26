# Lox Interpreter

This repository contains an interpreter for the Lox programming language, as described in the Crafting Interpreters book. Lox is a simple, high-level, dynamically-typed, interpreted programming language designed for educational purposes.

Features
- Dynamically-typed language
- Variables and basic data types: numbers, strings, and booleans
- Control structures: if, while, for
- Functions, including closures and anonymous functions (lambdas)
- Classes and simple inheritance

## Code Sample
```
class POS {
    init() {
        print "Taking Order:";
        print "Bread($1.99)";
        print "Fish($1.99)";
        print "Sausage($1.99)";
        print "Cabbage($1.99)";
        print "Brownies($1.99)";
        this.orderc = 0;
    }

    order(number) {
        if (number == 5) {
            serve();
        }
    }

    serve() {
        for (var i = 0; i < this.orderc; i = i + 1) {
            print("Serving...");
        }
    }


}

var pos = POS();
```

### Tokens
```
CLASS class null
IDENTIFIER POS null
LEFT_BRACE { null
IDENTIFIER init null
LEFT_PAREN ( null
RIGHT_PAREN ) null
LEFT_BRACE { null
PRINT print null
STRING "Taking Order:" Taking Order:
SEMICOLON ; null
PRINT print null
STRING "Bread($1.99)" Bread($1.99)
SEMICOLON ; null
PRINT print null
STRING "Fish($1.99)" Fish($1.99)
SEMICOLON ; null
PRINT print null
STRING "Sausage($1.99)" Sausage($1.99)
SEMICOLON ; null
PRINT print null
STRING "Cabbage($1.99)" Cabbage($1.99)
SEMICOLON ; null
PRINT print null
STRING "Brownies($1.99)" Brownies($1.99)
SEMICOLON ; null
THIS this null
DOT . null
IDENTIFIER orderc null
EQUAL = null
NUMBER 0 0.0
SEMICOLON ; null
RIGHT_BRACE } null
IDENTIFIER order null
LEFT_PAREN ( null
IDENTIFIER number null
RIGHT_PAREN ) null
LEFT_BRACE { null
IF if null
LEFT_PAREN ( null
IDENTIFIER number null
EQUAL_EQUAL == null
NUMBER 5 5.0
RIGHT_PAREN ) null
LEFT_BRACE { null
IDENTIFIER serve null
LEFT_PAREN ( null
RIGHT_PAREN ) null
SEMICOLON ; null
RIGHT_BRACE } null
RIGHT_BRACE } null
IDENTIFIER serve null
LEFT_PAREN ( null
RIGHT_PAREN ) null
LEFT_BRACE { null
FOR for null
LEFT_PAREN ( null
VAR var null
IDENTIFIER i null
EQUAL = null
NUMBER 0 0.0
SEMICOLON ; null
IDENTIFIER i null
LESS < null
THIS this null
DOT . null
IDENTIFIER orderc null
SEMICOLON ; null
IDENTIFIER i null
EQUAL = null
IDENTIFIER i null
PLUS + null
NUMBER 1 1.0
RIGHT_PAREN ) null
LEFT_BRACE { null
PRINT print null
LEFT_PAREN ( null
STRING "Serving..." Serving...
RIGHT_PAREN ) null
SEMICOLON ; null
RIGHT_BRACE } null
RIGHT_BRACE } null
RIGHT_BRACE } null
VAR var null
IDENTIFIER pos null
EQUAL = null
IDENTIFIER POS null
LEFT_PAREN ( null
RIGHT_PAREN ) null
SEMICOLON ; null
EOF  null
```


## Build Instructions
```
javac App.java
java App [filename]
```

The build instructions provided are for compiling and running the Java implementation of the Lox language interpreter. Here is a detailed explanation of each step:

1. javac App.java: This command compiles the App.java file, which is the main entry point of the Lox interpreter. The javac command is the Java compiler, and it takes one or more Java source files as input. In this case, it compiles the App.java file, along with any other required Java files that are imported by App.java. The result of the compilation is a set of Java bytecode files with the .class extension, which can be executed by the Java Virtual Machine (JVM).

2. java App [filename]: This command runs the compiled Java bytecode of the Lox interpreter using the JVM. The java command takes the name of the main class (without the .class extension) as its argument, in this case, App. The optional [filename] argument is used to specify a Lox script file to be executed by the interpreter. If the [filename] argument is not provided, the interpreter will start in REPL (Read-Eval-Print Loop) mode, allowing you to enter Lox statements and expressions interactively.

In summary, the build instructions consist of two steps: first, compile the Java source files using javac, and second, run the compiled bytecode using the java command. When running the interpreter, you can provide an optional Lox script file to be executed, or you can start the interpreter in REPL mode for interactive use.