# import ptvsd
# ptvsd.enable_attach(address=("0.0.0.0", 5678))
# ptvsd.wait_for_attach()  # blocks execution until debugger is attached

import debugpy
debugpy.listen(('localhost', 5678))
def test_always_passes():
    assert True

# debugpy.breakpoint() 
def test_always_fails():
    assert False
