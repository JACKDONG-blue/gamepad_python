'''线程'''
import threading

class KillableThread(threading.Thread):
    '''可以被杀死的线程'''
        
    def kill(self) -> None:
        '''用非安全的手段杀死线程, 因此这个线程不能掌握重要资源'''
        # 获取_tstate_lock这个锁
        # lock = self._tstate_lock
        # if lock is not None and lock.locked():
        #     # 锁释放
        #     lock.release()
        # self.join()
        self._wait_for_tstate_lock()
    
    def _wait_for_tstate_lock(self, block=True, timeout=-1):
        # Issue #18808: wait for the thread state to be gone.
        # At the end of the thread's life, after all knowledge of the thread
        # is removed from C data structures, C code releases our _tstate_lock.
        # This method passes its arguments to _tstate_lock.acquire().
        # If the lock is acquired, the C code is done, and self._stop() is
        # called.  That sets ._is_stopped to True, and ._tstate_lock to None.
        lock = self._tstate_lock
        if lock is None:  # already determined that the C code is done
            assert self._is_stopped   # we see that we don't wait for anything here
        elif lock.acquire(block, timeout):
            lock.release()
            self._stop()