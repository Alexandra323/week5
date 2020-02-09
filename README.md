# WEEK 5 
02/08/2020

## Recap
- Functions
- Package, module
- OOP concepts:
    - Classes
    - Objects
    - Inheritence
    - method/function overriding
    - Encapsulation (hiding data >> __name )

- Polymorphism (and function overloading)
    (see examples in polymorphism.py)
- abstraction 
    with classes, interface (blueprint of classes, just declare the functions and attributes , you dont define funciton (no body of the functions))

## Exception handling and testing your code

### Creating your tests, testing your code
Pytest, unittest etc

    Test1 (functions)
    1. precodition
    2. action
    3. verify >> generates PASS/FAIL (assert)

    Test2 (functions)
    1. precodition
    2. action
    3. verify >> generates PASS/FAIL (assert)


### Exception handling

    def funtionname(arg1, arg2):
        try: 
            <your main is here>
        except ZeroDivisionError:
            <code if you face division by zero>
        except:
            <code if you have an error>
   

## Testing framework (Web Testing)
*How to create a project for automated web testing*

**PYTEST**

Pytest collects all files and functions starting with 'test'


# Selenium basics

Steps:
1. Download and Install from command line:
    pip install selenium
2. Intro to test framework
3. Create basic script (manual) to automate 
    Test Case: Searching 'T-shirt' on automationpractice.com web store
    
4. Automate the steps with selenium script
5. apply pytest framework set up