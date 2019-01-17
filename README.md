###News Data Project

### Required Packages
Python 3 ([Download](https://www.python.org/downloads/))
psycopg2: Run `pip install psycopg2`.

### Environment Setup
##### Download and Install
__Virtualbox__ ([Download](https://www.virtualbox.org/wiki/Downloads)). Install the platform package for your operating system. You do not need the extension pack or the SDK

__Vagrant__ ([Download](https://www.vagrantup.com/downloads.html)). Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.

##### Download the VM configuration
You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called __FSND-Virtual-Machine__. It may be located inside your __Downloads__ folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

##### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will prompt Vagrant to download the Linux operating system and install it. Be patient as this could take a while.

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!

Inside the VM, change directory to `/vagrant`. The files you see here are the same as the ones in the `vagrant` subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

To run this program, make sure all the program files are within the `vagrant` folder on your machine and then change directory to where those files live. If you have already installed the database on your virtual machine, run `python newsdata.py`. Otherwise, read on.

##### Set up the database
[Download the database data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it into your `vagrant` directory. On your virtual machine in the same directory as the sql file run `psql -d news -f newsdata.sql`. Now the data is imported into your database and the program can be run.


### Running the Program
You will be prompted to make a selection:
```
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

Which query would you like to run?
```
Selection 1 calls the `get_articles()` function and should return something like this:
```
The three most popular articles of all time are: 

"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views
```

Selection 2 calls the `get_authors()` function and should return something like this: 
```
The most popular article authors of all time are: 

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views
```

Selection 3 calls the `get_404s()` function and should return something like this:
```
The days on which more than 1% of requests lead to errors are: 

July 17, 2016 -- 2.26% errors
```

