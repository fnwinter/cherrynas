class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls, *args, **kwargs).__new__(cls, *args, **kwargs)
        return cls.instance
