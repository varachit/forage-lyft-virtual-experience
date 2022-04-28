# Lyft Back-End Engineering Virtual Experience Program
Lyft is in the process of rolling out a new rental fleet in the hopes of encouraging more connected, 
sustainable cities across the US. You are the fortunate inheritor of an unfortunately messy component utilized 
by the rental fleet’s new logistics system. The component is responsible for determining whether cars in Lyft’s 
new rental fleet should be serviced when they are returned. Whether or not a car should be serviced depends on 
two factors at the moment - the engine and battery. There are five car models in Lyft’s fleet, 
each with a different engine-battery combination. Each of the three types of engines has its own criteria 
for determining when it should be serviced. The same applies to each type of battery. These service criteria 
will change somewhat frequently in the future, and new car models are bound to be added to the fleet. 

With this in mind, it’s very important that the component is extensible and easy to modify, so new service 
criteria can be added quickly and efficiently. Just today, you learned that the system must also take tires 
into account when determining if a car should be serviced in the future. Tacking this functionality onto the 
current system would be difficult and messy - instead, you have been instructed to take the time to refactor 
the codebase prior to making the change. The first step of this process is to draft up a new (clean) 
system architecture that will allow for the seamless inclusion of the new functionality. 
Your task is to draft and submit a class diagram that maps out how the system will be reorganized.

## Instruction
The starter repository is provided @ [github.com/vagabond-systems/forage-lyft-starter-repo](https://github.com/vagabond-systems/forage-lyft-starter-repo)

#### Service criteria:
- Engines
  - Capulet Engine - should be serviced once every 30,000 miles
  - Willoughby Engine - should be serviced once every 60,000 miles
  - Sternman Engine - should be serviced only when the warning indicator is on
- Batteries
  - Spindler Battery - should be serviced once every 2 years
  - Nubbin Battery - should be serviced once every 4 years

#### Car models:
- Calliope
  - Capulet Engine
  - Spindler Battery
- Glissade
  - Willoughby Engine
  - Spindler Battery
- Palindrome
  - Sternman Engine
  - Spindler Battery
- Rorschach
  - Willoughby Engine
  - Nubbin Battery
- Thovex
  - Capulet Engine
  - Nubbin Battery

### Task 1 - Software Architecture
The starter repo contains the core functionality of the fleet service component referenced above. 
To come up with a better design, the current state of the codebase must be fully comprehend. 
When have clear understand of the current system, find the best way to re-design it and write a proper UML Diagram.

- Resources\
  [Git](https://git-scm.com/book/en/v2)\
  [Composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance)\
  [Behavioral patterns](https://sourcemaking.com/design_patterns/behavioral_patterns)\
  [UML Class Diagram Tutorial](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/)

### Original Design
![initial_design.png](https://i.imgur.com/1QUi0U2.png)

### New Design
![refactored_design.png](https://i.imgur.com/5ZtYXoV.png)

### Task 2 - Refactoring
Using the repository from the last task as a starting point, refactor the codebase to reflect the new design.

- Resources\
  [Factory Method](https://refactoring.guru/design-patterns/factory-method)\
  [Refactoring Strategy](https://refactoring.guru/design-patterns/strategy)\
  [Refactoring](https://refactoring.guru/refactoring)

### Task 3 - Unit Testing
Add unit tests to the codebase. Replace the old test suite in the tests folder with own series of unit tests.
The old test suite is broken due to the new implementation or refactoring.

- Resources\
  [The Clean Code Blog](https://blog.cleancoder.com/uncle-bob/2017/05/05/TestDefinitions.html)\
  [UnitTest](https://martinfowler.com/bliki/UnitTest.html)\
  [Unit testing framework](https://docs.python.org/3/library/unittest.html)\
  [Getting Started With Testing in Python](https://realpython.com/python-testing/)

### Task 4 - Test-Driven Development (TDD)
Add some new functionality using TDD. Throughout this task, use a test-driven development workflow - 
write tests that check for the expected behavior, write code to satisfy those tests, rinse and repeat. 

1. **Upgrade Spindler batteries**\
First, modify the Spindler battery, so it requires service after three years instead of two. 

2. **Add tire servicing criteria**\
There are two types of tires currently in use by the Lyft fleet - Carrigan tires and Octoprime tires. 
The new tire wear sensors produce an array of four numbers between 0 and 1 inclusive, 
representing how worn each of the tires are. This array will be passed to each function in the car factory class,
to be used by your tire implementation. Carrigan tires should be serviced only when one or more of the values in
the tire wear array is greater than or equal to 0.9. Octoprime tires should be serviced only when the sum of
all values in the tire wear array is greater than or equal to 3.

- Resources\
  [The Art of Agile Development: Test-Driven Development](http://www.jamesshore.com/v2/books/aoad1/test_driven_development)\
  [The Three Laws of TDD](http://www.butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)

### Final Design
![final_design.png](https://i.imgur.com/mfpw46V.png)