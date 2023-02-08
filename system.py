import sys, threading, time, re #start with builtins
import ram, rom, fsystem, console, exec #then use the custom stuff

LRAM = ram.ram() #LRAM is low-function RAM (for system processes)
LROM = rom.rom({
    'user_list' : ['root'],
    'pass_list' : ['toor'],
    'su_list' : [True],
    'dumpfile' : 'sys\\00.dmp',
    'use_regexp' : '|',
    'usefile': 'sys\\users.use',
    'root' : fsystem.cwd() + '\\root\\',
    'server' : 'chat.freenode.net',
    'channel' : '#mk-comms',
    'inbox_dest' : 'sys\\inbox',
    'post_dest' : 'sys\\post.inb'})

LRAM.wT('host_name', 'micro_ii') #system name (like dave, for instance
LRAM.wT('system_active', True) #is the power button in
LRAM.wT('crash', False) #should we straight up kill the computer?
LRAM.wT('restart_q', False) #queuing for restart?

def start():
    if LRAM.rT('crash'):
        #There are no fatal crashes (they all are), so don't even bother. If it's bad enough to warrant a crash, it's pretty bad.
        pass

    fsystem.cd(LROM.rT('root') + 'home\\')

    RAM = ram.ram()
    RAM.purge()


    RAM.wT('usefile_content', open(LROM.rT('root') + LROM.rT('usefile')).read().split('\n'))
    RAM.wT('su_list', re.split(LROM.rT('use_regexp'), RAM.rT('usefile_content')[0]) + LROM.rT('su_list'))
    RAM.wT('user_list', re.split(LROM.rT('use_regexp'), RAM.rT('usefile_content')[1]) + LROM.rT('user_list'))
    RAM.wT('pass_list', re.split(LROM.rT('use_regexp'), RAM.rT('usefile_content')[2]) + LROM.rT('pass_list'))
    RAM.wT('user_session_active', False)

    while LRAM.rT('system_active'):
        while not(RAM.rT('user_session_active')):
            console.write('please log in.')
            RAM.wT('user_name', console.read('\tusername: '))
            RAM.wT('pass_word', console.read('\tpassword: '))
            if RAM.rT('user_name') in RAM.rT('user_list') + LROM.rT('user_list'):
                if RAM.rT('pass_word') in RAM.rT('pass_list') + LROM.rT('pass_list'):
                    #clear console, as the user has just started their session.
                    console.clr()
                    #if user has sudo privs, set su status
                    RAM.wT('user_is_su', 'True' == RAM.rT('sudo_list'[RAM.rT('user_list').index(RAM.rT('user_name'))]))
                    #login successful so display the message
                    console.write('welcome to microsystems mk.ii! you have logged in successfully as: ' + LRAM.rT('host_name') + '@' + RAM.rT('user_name') + '.')
                    RAM.wT('user_session_active', True)
                else:
                    console.clr()
                    console.write('error: password incorrect.')
                    console.write('')

        #regular runtime stuff here
        uInput = console.read('>')
        if uInput == 'logout':
            RAM.wT('user_session_active', False)
        else:
            try:
                exec.run(LROM.rT('root') + 'bin\\' + uInput + '.mcs')
            except:
                console.write('input is not a file, nor a recognized command.')
