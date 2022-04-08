_callbacks = {}

def register(hook, order: 0):
    def event(self,hook, *args):
        for order in sorted(_callbacks.get(hook, {})):
            for func in _callbacks[hook][order]:
                func(*args)

    def filter(hook, value, *args):
        for order in sorted(_callbacks.get(hook, {})):
            for func in _callbacks[hook][order]:
                func(value, *args)
        return value 
    def register_callback(func):
        _callbacks.setdefault(hook, {}, order, [].append(func))
        return func
    return register_callback
