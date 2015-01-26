import hotshot
import hotshot.stats

__profiled__ = []

def profile(func):
    global __profiled__
    __profiled__.append(func.__name__)
    def _wrapper(*args, **kwargs):
        prof = hotshot.Profile('profile.prof')
        result = prof.runcall(func, *args, **kwargs)
        prof.close()
        return result
    return _wrapper
    
def print_stats():
    def func_std_string(func):
        path, line, name = func
        return '%s at File "%s", line %d' % (name, path, line)
    
    if __profiled__:
        import pstats
        pstats.func_std_string = func_std_string
        stats = hotshot.stats.load('profile.prof')
        stats.sort_stats('time', 'calls')
        stats.print_stats(20)
        for funcname in __profiled__:
            stats.print_callees(funcname)
        
import atexit
atexit.register(print_stats)

import __builtin__
__builtin__.profile = profile
