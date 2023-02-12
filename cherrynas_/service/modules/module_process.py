# Copyright 2019 fnwinter@gmail.com

from multiprocessing import Process

class ModuleProcess():
    """ Module Process """
    def __init__(self, name, context, func):
        self.func = func
        self.name = name
        self.context = context
        self.process = Process(target=self.func, args=([self.context]))

    def start(self):
        self.process.start()

    def join(self):
        self.process.join()
