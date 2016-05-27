# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. hostname: My computer's network name
2. man: Read through a manual page to find information about a command
3. apropos: When you forget the name of the command but know what it does
4. pushd: Takes you to the current directory and pushes into a list for later, then it changes to another directory. (AKA 'save where I am, then go here')
5. popd: Takes the last director you pushed and 'pops' it off, taking you back there
6. less: Page through a file (whole screen)
7. more: List contents in a file
8. mkdir -p: Make entire path even if all those directories don't exist yet
9. $|$: Takes output from command on the left and pipes it to the command on the right
10. $<$: The '<' will take and send the input from the file on the right to the program on the left
11. $>$: Takes the output of the command on the left, then writes it to the file on the right
12. $>>$ Takes the output of the command on the left, then appends it ot the file on the right
13. * = Wildcard
14. env: Look at your environment
15. echo: Print some arguments
16. exit: Exit

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls: list directory
ls -a: list all entries including those starting with a dot  
ls -l: list using a long listing format  
ls -lh: list files in human readable format size using a long listing format  
ls -lah: list all files in human readable format size including those starting with a dot using a long listing format  
ls -t: list sorting by modification time  
ls -Glp: display directories with /, excluding groups information, using a long listing format  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -q: display all nonprinting characters as ?  
ls -r: display files in reverse order  
ls -c: display files by file timestamp  
ls -C: display files in columnar format  
ls -m: display the names as a comma-separated list  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

'xargs' executes a command, passing through constructed argument lists. The arguments are typically a long list of file names piped. 'xargs' passes arguments to command in several bundles, allowing the command to process more arguments than it could otherwise handle at once.  

One of the most important usages of 'xargs' is with the find command.  
For example: Find all the .mp3 files in teh music folder and pass to the ls command, -print0 is required if any filenames contain whitespace:  
find ./music -name "*.mp3" -print0 | xargs -0 ls  

 

