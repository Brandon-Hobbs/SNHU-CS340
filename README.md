# CS-340
SNHU CS-340 Client Server


How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

Writing code with a modular ideal is useful for maintainability and readability. For example, instead of creating a monolithic block of code, containing all of the functions, classes, and main, it might be better to organize the files into classes. Each of these files could contain the class and its associated getter and setter. Main would be its own file. Any helper functions could be organized into libraries. With this scheme an individual library could be tweaked/fixed and then any code importing this library ebenefits from that fix/tweak.


How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

I try to start with an overall picture of what should be built, top down/requirements driven approach, instead of starting to code individual components, bottoms-up. I have found if I start throwing code at the problem there is often a lot of re-work as function develop, e.g., need to pass differnt arguments or return a different type.
