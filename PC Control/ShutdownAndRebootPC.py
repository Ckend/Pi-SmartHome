#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pexpect
import os
import sys
import time
def shutdown(ip=sys.argv[1], username=sys.argv[2], password=sys.argv[3]):
    # ssh login
    proc = pexpect.spawn("ssh %s@%s " % (str(username), str(ip)))
    index = proc.expect([".*assword.*", ".*yes.*"])
    if index > 0:
        proc.sendline("yes")
        proc.expect(".*assword.*")
    proc.sendline(password)
    # shutdown the dst machine
    # proc.interact()
    proc.expect(".*Ckend>.*")
    # print proc.readline()
    proc.send("shutdown.exe -s -t 00"+'\r\n')
    time.sleep(1)

def reboot(ip=sys.argv[1], username=sys.argv[2], password=sys.argv[3]):
    # ssh login
    proc = pexpect.spawn("ssh %s@%s " % (str(username), str(ip)))
    index = proc.expect([".*assword.*", ".*yes.*"])
    if index > 0:
        proc.sendline("yes")
        proc.expect(".*assword.*")
    proc.sendline(password)
    # shutdown the dst machine
    # proc.interact()
    proc.expect(".*Ckend>.*")
    # print proc.readline()
    proc.send("shutdown.exe -r -t 00"+'\r\n')
    time.sleep(1)

if sys.argv[4] == 'reboot':
    reboot()
elif sys.argv[4] == 'shutdown':
    shutdown()