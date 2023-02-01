#!/usr/bin/env python3

import glob
import os
import re
import subprocess
import random
import shutil
import string
import sys

print('THIS SCRIPT REQUIRES THE SPIDERMONKEY SHELL TO BE ON YOUR PATH!')
print('If it blows up, this is probably why.')

js = 'js'

[os.remove(f) for f in glob.iglob('build/dist/*', recursive=True)]
for ext in ['*.wasm', '*.wat']:
    [os.remove(f) for f in glob.iglob('build/**/' + ext, recursive=True)]

os.makedirs('build', exist_ok=True)

print('Compiling...')
subprocess.run([
    js, 'build-sm.js',
    'src/memory-discard-mem32.wat', 'build/memory-discard-mem32.wasm',
])
# subprocess.run([
#     js, 'build-sm.js',
#     'src/memory-discard-mem64.wat', 'build/memory-discard-mem64.wasm',
# ])

#
# Output the dist folder for upload
#

print('Building dist folder...')
os.makedirs('build/dist', exist_ok=True)

buildId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) # so beautiful. so pythonic.

root = 'src/index.html'
assets = [
    'src/tachyons.css',
    'build/memory-discard-mem32.wasm',
    # 'build/memory-discard-mem64.wasm',
]

rootContents = open(root).read()

def addId(filename, id):
    parts = filename.split('.')
    parts.insert(-1, buildId)
    return '.'.join(parts)

for asset in assets:
    basename = os.path.basename(asset)
    newFilename = addId(basename, buildId)
    shutil.copy(asset, 'build/dist/{}'.format(newFilename))

    rootContents = rootContents.replace(basename, newFilename)

with open('build/dist/index.html', 'w') as f:
    f.write(rootContents)

print('Done!')
