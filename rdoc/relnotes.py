#!/usr/bin/python

# Generate the release notes in release-notes.html. Call as
#   relnotes.py <rootsrc> master
# or
#   relnotes.py <rootsrc> v6-06-00-patches
# where <rootsrc> is the location of the ROOT sources
#
# Axel, 2015-11-26
 
import sys
from glob import glob
from subprocess import check_call

def make(rootsrc, branch):
    versionDir = branch.replace('-00-patches', '').replace('-', '')
    if versionDir == 'master':
        # Take the one with the highest number:
        mdDir = sorted(glob('README/ReleaseNotes/v*/'))[-1]
    else:
        mdDir = 'README/ReleaseNotes/' + versionDir + '/'

    invocation = ['pandoc',
                  '-f', 'markdown',
                  '-t', 'html',
                  '-s', '-S',
                  '-f', 'markdown',
                  '--toc',
                  '-H', rootsrc + 'documentation/users-guide/css/github.css',
                  '--mathjax',
                  rootsrc + mdDir + 'index.md',
                  '-o', 'release-notes.html']

    print('Invoking: ' + ' '.join(invocation))
    check_call(invocation)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    make(sys.argv[1], sys.argv[2])