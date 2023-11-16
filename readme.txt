1. Your name and CSM Campus Wide ID (CWID).

    Name: Eric McKevitt
    CWID: 10874645

2. What programming language and its version are used for developing your source codes?

    Python version 3.9.13

3. What OS and its version are used to compile and run the codes?

    macOS Monterey
    Version 12.3

4. How the code is structured.

    The entry-point to the program is the main function, which starts by using a helper function to read in command-line arguments.
    Then, another helper file reads in the .txt file and uses each line to construct a dictionary of adjacency lists for all the nodes. 
    This is how the graph is represented in this program. 
    Once the graph is returned, it is passed to the uniform_cost_search function along with the source and destination cities. 
    This function performs a UCS on the graph, keeping track of the shortest path as it is constructed. 
    Once the function returns the path, a helper function outputs the path in the correct format. 
    There is also a function that uses networkx to construct another representation of the graph so that it can be plotted simply using matplotlib. 
    This is optional, but adds a nice touch. 
    
    Also, there is another file called find_route_geography.py, which does the exact same thing as find_route.py, 
    but it first uses geopy to find the coordinates of each city and store those in a dictionary. This way, we can force the location 
    of each node in the plot to abide by it's coordiantes, which results in a much more realistic deptiction of the path when it is plotted later. 
    I included this in a separate file because it can take around 5 seconds to generate the coordinate dictionary. 

    There is a folder, "Test Cases", that contains 10 test cases you can run, along with their expected outputs. 

5. How to run the code, including very specific compilation instructions, if compilation is needed. Instructions such as "compile using g++" are NOT considered specific.

    In order to run the program, navigate to the folder containing find_route.py in a terminal and run a command of the following form: 

    python find_route.py {input_file} {source_city} {destination_city}

    Example:
    python find_route.py input1.txt Bremen Frankfurt

    Choose between input1.txt, input2.txt, or my custom file, custom_input.txt

    Note: If you want to run the other file, find_route_geography.py, you may need to install geopy first, using the following command: 
    pip install geopy

    If you have issues with this, you can say `pip3 install geopy`, and then run the file with: 
    python3 find_route_geography.py custom_input.txt Denver Golden

    This ensure that the version of Python the library was installed to is the version executing the script. 