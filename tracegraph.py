#!/usr/bin/python
import sys
import re

class Host(object):
  def __init__(self, step, name, ip):
    self.step = step
    self.name = name
    self.ip = ip
    self.pings = []

  def add_ping(self, ping):
    self.pings.append(ping)

  def max_ping(self):
    return max(self.pings) if self.pings else 0

  def min_ping(self):
    return min(self.pings) if self.pings else float('inf')

class Step(object):
  def __init__(self):
    self.hosts = []

def to_host(line):
  parts = re.split(r'\s+', line.strip())

  step = ''
  if parts[0].isdigit():
    step = int(parts[0])
    parts = parts[1:]

  x = 0
  while  x < len(parts) and parts[x] == '*':
    x += 1

  name = '?'
  ip   = '?'

  if x < len(parts):
    name = parts[x]
    x += 1

  if x < len(parts):
    ip = parts[x]
    x += 1

  pings = [float(t) for t in parts[x:] if t != 'ms' and t != '*']

  host = Host(step, name, ip)
  for ping in pings:
    host.add_ping(ping)
  return host

def barplot(host, scale):
  if not host.pings:
    return ''

  p0 = int(host.min_ping() * scale)
  p1 = int(host.max_ping() * scale)

  return (max(0, p0 - 1) * ' '
          + 'o'
          + (p1 - p0 - 1) * '-'
          + ('o' if p1 > p0 else ''))

def rchop_to(s, l):
  if len(s) <= l:
    return s
  return '...' + s[-l+3:]

if len(sys.argv) > 1:
  # Pass arguments to traceroute
  import subprocess
  #lines = subprocess.check_output(['traceroute'] + sys.argv[1:]).splitlines()
  p = subprocess.Popen(['traceroute'] + sys.argv[1:], stdout=subprocess.PIPE, stderr=None)

  lines = []
  for line in iter(p.stdout.readline,''):
    lines.append(line.rstrip())
    print line.rstrip()
else:
  print 'Reading from stdin.'
  lines = sys.stdin.read().splitlines()
  print 'traceroute:'
  print '\n'.join(lines)

print ''
print 'tracegraph:'

hosts = list(to_host(line) for line in lines)
max_ping = max(h.max_ping() for h in hosts)

WIDTH = 60

scale = float(WIDTH) / max_ping

for host in hosts:
  print '%2s %-20s | %s' % (host.step, rchop_to(host.name, 20), barplot(host, scale))

print 25 * ' ' + '  0ms' + (WIDTH - 8) * ' ' + ' %.1fms' % max_ping
