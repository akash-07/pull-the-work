## EDNA, a software tool for verifying the normalization of Relations during the logical database design process

**What does the existing tool do?**

1. Input: Fields/Attributes and FD's
2. Output: Decomposed schema based on FD's for different normal forms as specified. Also, it provides a facility of generating SQL commands to create the physical table structure in a number of popular database management systems.

**Possible Improvements**

Stated in paper itself ->
1. Better user interface
2. Including 4th and 5th normal forms
3. Add a facility to print sets of FD's or export them to another program so that they can be easily given to students for normalization as a manual task.
4. Drag and drop features for specifying FD's once attributes have been defined.

My thoughts ->
1. Introduce learning component than just taking input and showing output. Possibly, this could be showing step by step execution of how the algorithm decomposes the schema.
2. Have a static set of examples for teaching decomposition into different normal forms.
3. Allow users to enter their own schema definition (which they are already doing) such that they can see step by step visualization of how the algorithm for decomposition proceeds.

**Inspired from**
https://www-m9.ma.tum.de/graph-algorithms/matchings-hopcroft-karp/index_en.html  
