# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

* pwd - show current working directory path
* mkdir NAME 					 				:creating a directory
* rm -R NAME 					 				:deleting a directory (permanent)
* touch NAME 					 				:creating a file using `touch` command
* rm NAME		 					 				:deleting a file
* mv OLD_NAME NEW_NAME 				:renaming a file
* ls -a 							 				:listing hidden files
* cp FILE_PATH NEW_FILE_PATH	:copying a file from one directory to another
* cd ../											:move up one folder level
* nano NAME.txt								:create a new text file in nano editor
---

### Q2.  List Files in Unix   

What do the following commands do:  
* `ls`     : lists all files and directories in the current directory.
* `ls -a`  : lists all files and directories (including hidden files) in the current directory.
* `ls -l`  : lists all files as a table
* `ls -lh` : lists all files, their size, and the datetime last modified 
* `ls -lah`: lists all files (including hidden files), their size, and the datetime last modified  
* `ls -t`  : lists all files sorted by time and date
* `ls -Glp`: lists all the files and directories giving their size and ordered by datetime last modified  


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* ls -d :lists all directories
* ls -m :lists all names as csv
* ls -p : displays all directories to end with "/"
* ls -R : displays the subdirectories as well (however, beware not to use this at the very top level of the directory)
* ls -u : displays files by access time

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.
__

xargs repeats an operation on a list of files or, more generally speaking, a collection of multiple items.

For example, if I wanted to print out the content of several .txt files, I would use the following code:

ls *.txt | xargs cat

 

