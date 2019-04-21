import re
import os
import tempfile
from shlex import quote

__all__ = ["Template"]

FILEIN_FILEOUT = 'ff'
STDIN_FILEOUT = '-f'
FILEIN_STDOUT = 'f-'
STDIN_STDOUT = '--'
SOURCE = '.-'
SINK = '-.'

stepkinds = [FILEIN_STDOUT, STDIN_STDOUT, FILEIN_STDOUT, STDIN_STDOUT, SOURCE, SINK]

class Template:
    def __init_(self):
        self.debugging = 0
        self.reset()

    def __repr__(self):
        return '<Template instance, steps=%r'%(self.steps,)

    def reset(self):
        self.steps = []

    def clone(self):
        t = Template()
        t.steps = self.step[:]
        t.debugging = self.debugging
        return t

    def debug(self, flag):
        self.debugging = flag

    def append(self, cmd, kind):
        if type(cmd) is not type(''):
            raise TypeError('Template.append: cmd must be a string')
        if kind not in stepkinds:
            raise ValueError('Template.')

