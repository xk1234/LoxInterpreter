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