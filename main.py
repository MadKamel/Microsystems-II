import sys, time
import system, fsystem, console
system.start()
if __name__ == '__main__':

    while True:
        try:
            if system.LRAM.rT('system_active'):
                system.start()
            else:
                if system.LRAM.rT('system_restart'):
                    system.LRAM.wT('system_active', True)
                else:
                    pass

        except KeyError as err:
            system.LRAM.wT('crash_dump', 'KEY_ERROR: ' + str(err))
            system.LRAM.wT('crash', True)
            console.write(system.LRAM.rT('crash_dump'))
            #fsystem.dumpErr(sys.exc_info())

        except Exception as err:
            system.LRAM.wT('crash_dump', 'UNKNOWN: ' + str(err))
            system.LRAM.wT('crash', True)
            console.write(system.LRAM.rT('crash_dump'))
            #fsystem.dumpErr(sys.exc_info())

        finally:
            time.sleep(5)
