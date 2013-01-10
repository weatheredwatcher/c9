# C9 


### About


C9 is a launcher utility for Cloud9 IDE.  It allows you to launch an instance of the editor from the command line.


### Installation

Clone the repo to the directory of your choice, then type:

    cp -l c9.sh /usr/local/bin/c9

This will create a symbolic link in your bin folder. 

From here on out, you can run an instance of the Cloud9 IDE by typing:

    c9 -w /path/to/workspace -p 3131 (port is optional)

### Features

C9 can be configured to the install location of your cloud9 install.  It also remembers what ports are being used and increments the port numbers for you.  C9 ports start at 3131 and increment by one. (3132, 3133, 3134).

Once you load a workspace on a port, C9 remembers and persists that port assignment.  So you can create bookmarks for projects.
