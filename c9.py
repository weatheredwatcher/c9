
"""Cloud 9 Launcher

Launches the Cloud 9 IDE with the specified workspace.  Uses port numbers for different instances
c9 [path to workspace] -p [port number](optional)
Options:
  -p ..., --project=...   use specified project/domainS
  -h, --help              show this help
  -d                      show debugging information while parsing


"""

__author__ = "David Duggins (weatheredwatcher@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/08 09:03:19 $"
__copyright__ = "Copyright (c) 2013 David Duggins"
__license__ = "GPL3"


import sys
import getopt
import ConfigParser
import subprocess




class C9():
    """This is the main class file for the c9 launcher"""
    def __init__(self, argv):
        config = ConfigParser.RawConfigParser()
        #todo: check to see if config file exists
        #todo: create initial config file
        #todo: read config file and checkk for values
        #todo: if path is not set, exit program
        # here we handle the command line input and test it for validity,
        # if there is an issue, we end the program and spit out errors.
        try:
            opts, args = getopt.getopt(argv, "hwc:", ["help", "workspace=", "config="])
        except getopt.GetoptError:           
            usage()                          
            sys.exit(2)  
        for opt, arg in opts:                
            if opt in ("-h", "--help", " "):      
                usage()                     
                sys.exit()                                
            elif opt in ("-w", "--workspace"): 
                self.project = arg
            elif opt in ("--config"):
                self.path = arg
                #todo: write configuration and exit program
                print "Configuration Written: %s" % (self.path, )
                sys.exit()
            
    def run_ide(self):
        path = "home/weatheredwatcher/source/cloud9/bin/cloud9.sh"
        args = " -p 3131 -w %s" % (self.project, )
        subprocess.call('ls', ' -l')
        #print path + args

def usage():
        print __doc__
        
def main(argv):
    
    
    
    me = C9(argv)
    me.run_ide()
    
    

main(sys.argv[1:])