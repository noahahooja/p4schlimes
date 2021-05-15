def metadata():
    greeting = "#"
    name = "Metadata"
    doa = "Metadata is data that gives information about another set of data. In this code, a list full of dictionaries is made. Each dictionary in the list can be considered metadata of the list. This is because we are using the list to hold a set of data (video game consoles) and each item in the list corresponds to a dictionary that contains the metadata of the item in the list (release year and full name)."
    job = "#"
    embed = "https://repl.it/@BradleyBartelt1/WebscrapeCollegeBoard?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def algorithmic():
    greeting = "#"
    name = "Algorithmic Efficiency"
    doa = "When programming, it's important to be efficient. Efficient code takes less time to write, and will generally run smoother. In this code, 2 different methods for completing the same task are used. The first version is a much more beginner approach to collecting user input, while the second one is optimised in order to make it shorter and more efficient."
    job = "#"
    embed = "https://repl.it/@BradleyBartelt1/Collegeboard-simulations?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def undecidable():
    greeting = "#"
    name = "Undecidable problems"
    doa = "An Undecidable problem is one that a program can not give an answer to. In this code, 2 different situations are set up. The first one is undecidable and doesn't give an output, while the second one is decidable and has an output."
    job = "#"
    embed = "https://repl.it/@BradleyBartelt1/Collegeboard-undecidable-problems?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def binary():
    greeting = "#"
    name = "Binary and Mathematical expressions"
    doa = "This code is an integer to binary converter. It uses the fundamental principles of binary in order to convert numbers into it. All you have to do is type in an integer, and the program will convert it to binary. It demonstrates our knowledge of binary and python mathematical expressions."
    job = "#"
    embed = "https://repl.it/@BradleyBartelt1/DanesChallange?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def function():
    greeting = "#"
    name = "Functions, Classes and Lists"
    doa = "This is an older project that was worked on that shows a lot of understanding of functions classes and lists. The project allows the user to enter in words that are filled into a mad libs style story. Functions and classes can be used in order to organize chunks of code. They also allow you to “call” on that code in other parts of the program."
    job = "#"
    embed = "https://repl.it/@AndrewZhang4/MadLib?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info


def playlist():
    return [metadata(), algorithmic(), undecidable(), binary(), function()]