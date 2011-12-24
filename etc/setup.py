from fabric import api

def echo(cmdline1):
    option1 = api.env
    run("echo '%s %s'" % (option1, cmdline1) )
    
