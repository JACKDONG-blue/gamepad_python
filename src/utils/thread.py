'''线程'''
import threading

class KillableThread(threading.Thread):
    '''可以被杀死的线程'''
    def kill(self, consequences: bool = False) -> None:
        '''用非安全的手段杀死线程, 因此这个线程不能掌握重要资源'''
        # 获取_tstate_lock这个锁
        lock = self._tstate_lock
        
        if lock is not None and lock.locked():
            # 锁释放
            lock.release()
        self.join()
