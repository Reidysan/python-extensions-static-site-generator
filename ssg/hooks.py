_callback = {}

def register(hook, order: 0):
    def event(self,hook, *args):
        for order in sorted(_callback.get(hook, {})):
            for func in self._callbacks[hook][order]:
                func(*args)

    def filter(self, hook, value, *args):
        for order in sorted(_callback.get(hook, {})):
            for func in self._callbacks[hook][order]:
                func(value, *args)
        return value 
    def register_callback(func):
        _callback.setdefault(hook, {}, order, [].append(func))
        return func
    return register_callback
