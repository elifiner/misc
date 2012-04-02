import hotshot
import hotshot.stats

__profiled__ = False

def profile(func):
    global __profiled__
    __profiled__ = True
    def _wraper(*args, **kwargs):
        prof = hotshot.Profile("profile.prof")
        result = prof.runcall(func, *args, **kwargs)
        prof.close()
        return result
    return _wraper
    
def print_stats():
    def func_std_string(func):
        file, line, name = func
        return '%(name)s at File "%(file)s", line %(line)d' % locals()
    
    if __profiled__:
        import hotshot.stats
        import pstats
        pstats.func_std_string = func_std_string
        stats = hotshot.stats.load("profile.prof")
        stats.sort_stats('time', 'calls')
        stats.print_stats(20)
        
import atexit
atexit.register(print_stats)

import __builtin__
__builtin__.profile = profile
