a='''
accept command line arguments, but with flags like '-std' etc

in this example, will have multiple flags that will be looking for:
-swap (boolean T/F)
-height (integer 0 thru inf)
-path (string of directory)

argument format will be:
>> python script.py -swap=True -height=10 -path=some/local/path


NOTE: need to see if tab completion still works in this format for paths
UPDATE: YES IT WORKS

NOTE: also need to be able to reject unknown flags (exit program if
    dont recognize)
UPDATE: works

NOTE: check if arguments can be in any order
UPDATE: yes, they can be.
'''


from sys import argv
if(argv[1] == '--help'or argv[1]=='-help'):
    print a
    exit()

# initialize default values:
config={}
config['-path']='another/local/path/'
config['-height']=7
config['-swap']=False

# update config with input arguments
def updateConfig(conf,argsin):
    # setup comparison dict
    argin={}
    for iarg in argsin[1:]:
        (k,v) = iarg.split('=')
        argin[k]=v
    # check to make sure no unknown flags in arguments
    for ikey in argin.keys():
        if(ikey not in conf.keys()):
            print '\nERROR, unrecognized flag '+ikey+'. exiting...'
            exit()
    # assuming that all keys/flags given are correct, then add to relevant places
    for ikey in argin.keys():
        conf[ikey] = argin[ikey]
    # return results
    return conf

config = updateConfig(config,argv)

for ikey in config.keys():
    print ikey,':',config[ikey]






#eof
