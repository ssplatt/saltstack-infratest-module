# -*- coding: utf-8 -*-
'''
infratest

module to test server state using testinfra
documentation for the main python project: http://testinfra.readthedocs.org/
'''

try:
    import testinfra
    HAS_TESTINFRA = True
except ImportError:
    HAS_TESTINFRA = False

import logging

LOG = logging.getLogger(__name__)

__virtualname__ = 'infratest'

conn = testinfra.get_backend('local://')
File = conn.get_module("File")
Package = conn.get_module("Package")
Service = conn.get_module("Service")
Socket = conn.get_module("Socket")
Process = conn.get_module("Process")
Group = conn.get_module("Group")
User = conn.get_module("User")
Interface = conn.get_module("Interface")
SystemInfo = conn.get_module("SystemInfo")
Sysctl = conn.get_module("Sysctl")

# TODO
# process tests
# http://testinfra.readthedocs.org/en/latest/modules.html#process

# localcommand tests
# http://testinfra.readthedocs.org/en/latest/modules.html#localcommand

# socket clients tests
# http://testinfra.readthedocs.org/en/latest/modules.html#testinfra.modules.Socket.clients

# socket get_listening_sockets
# http://testinfra.readthedocs.org/en/latest/modules.html#testinfra.modules.Socket.get_listening_sockets

INFRATEST = {}
INFRATEST['Passed'] = []
INFRATEST['Failed'] = []

def __virtual__():
    '''
    only load if testinfra is available
    '''
    
    if HAS_TESTINFRA:
        return __virtualname__
    else:
        return (False, 'infratest execution module cannot be loaded: testinfra python module unavailable.')

def test_file_exists(thing, expected):
    '''
    test if file exists

    CLI Example::

        salt '*' infratest.test_file_exists /etc/passwd true
    '''
    
    detail = '{0} exists: {1}'.format(thing, expected)
    if File(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_isfile(thing, expected):
    '''
    test if file is a file

    CLI Example::

        salt '*' infratest.test_file_isfile /etc/passwd true
    '''
    
    detail = '{0} is: {1}'.format(thing, expected)
    if File(thing).is_file:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_isdir(thing, expected):
    '''
    test if file is a directory

    CLI Example::

        salt '*' infratest.test_file_isdirectory /etc/init.d true
    '''
    
    detail = '{0} is: {1}'.format(thing, expected)
    if File(thing).is_directory:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_ispipe(thing, expected):
    '''
    test if file is a pipe

    CLI Example::

        salt '*' infratest.test_file_ispipe /root/fifo1 true
    '''
    
    detail = '{0} is: {1}'.format(thing, expected)
    if File(thing).is_pipe:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_issocket(thing, expected):
    '''
    test if file is a socket

    CLI Example::

        salt '*' infratest.test_file_issocket /var/run/mysql.sock true
    '''
    
    detail = '{0} is: {1}'.format(thing, expected)
    if File(thing).is_socket:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_issymlink(thing, expected):
    '''
    test if file is a symlink

    CLI Example::

        salt '*' infratest.test_file_issymlink /var/run true
    '''
    
    detail = '{0} is: {1}'.format(thing, expected)
    if File(thing).is_symlink:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_linkedto(thing, expected):
    '''
    test what a file is linked to

    CLI Example::

        salt '*' infratest.test_file_linkedto /var/run /run
    '''
    
    detail = '{0} is linked to: {1}'.format(thing, expected)
    if File(thing).linked_to == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_user(thing, expected):
    '''
    test if file is owned by user

    CLI Example::

        salt '*' infratest.test_file_user /etc/passwd root
    '''
    
    detail = '{0} is owned by user: {1}'.format(thing, expected)
    if File(thing).user == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_group(thing, expected):
    '''
    test if file is owned by group

    CLI Example::

        salt '*' infratest.test_file_group /etc/passwd wheel
    '''
    
    detail = '{0} is owned by group: {1}'.format(thing, expected)
    if File(thing).group == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_uid(thing, expected):
    '''
    test if file is owned by uid

    CLI Example::

        salt '*' infratest.test_file_uid /etc/passwd 0
    '''
    
    detail = '{0} is owned by uid: {1}'.format(thing, expected)
    if File(thing).uid == vals['uid']:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_gid(thing, expected):
    '''
    test if file is owned by gid

    CLI Example::

        salt '*' infratest.test_file_gid /etc/passwd 0
    '''
    
    detail = '{0} is owned by gid: {1}'.format(thing, expected)
    if File(thing).gid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_mode(thing, expected):
    '''
    test file mode

    CLI Example::

        salt '*' infratest.test_file_mode /etc/passwd 0644
    '''
    
    if type(expected) == int:
        # convert int to str if required
        expected = str(expected)
    if len(expected) == 3:
        # add 0 pad to mode, i.e. 644 => 0644
        expected = '0' + expected
    detail = '{0} has mode: {1}'.format(thing, expected)
    if oct(File(thing).mode) == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_contains(thing, expected):
    '''
    test if file contains a pattern

    CLI Example::

        salt '*' infratest.test_file_contains /etc/passwd root
    '''
    
    detail = '{0} contains: {1}'.format(thing, expected)
    if File(thing).contains(expected):
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_md5sum(thing, expected):
    '''
    test file md5sum

    CLI Example::

        salt '*' infratest.test_file_md5sum /etc/passwd 2131233424234aabbccee...
    '''
    
    detail = '{0} has md5sum: {1}'.format(thing, expected)
    if File(thing).md5sum == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_sha256sum(thing, expected):
    '''
    test file sha256sum

    CLI Example::

        salt '*' infratest.test_file_sha256sum /etc/passwd 1ab1ab1ab3bbab31ba3b1a...
    '''
    
    detail = '{0} has sha256sum: {1}'.format(thing, expected)
    if File(thing).sha256sum == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_mtime(thing, expected):
    '''
    test file modification time

    CLI Example::

        salt '*' infratest.test_file_mtime /etc/passwd '2012-01-01 10:01:22'
    
    python yaml tries to convert dates automatically on import
    but it is not predictable, necessarily
    make sure datetime in pillar is in quotes
    i.e. mtime: '2015-09-01 23:11:03'
    see https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html#automatic-datetime-conversion
    '''
    
    detail = '{0} has mtime: {1}'.format(thing, expected)
    if File(thing).mtime.strftime('%Y-%m-%d %H:%M:%S') == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_size(thing, expected):
    '''
    test file size in bytes

    CLI Example::

        salt '*' infratest.test_file_size /etc/passwd 128
    '''
    
    detail = '{0} has size: {1}'.format(thing, expected)
    if File(thing).size == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_package_isinstalled(thing, expected):
    '''
    test if package is installed

    CLI Example::

        salt '*' infratest.test_package_isinstalled exim4 true
    '''
    
    detail = '{0} is installed: {1}'.format(thing, expected)
    if Package(thing).is_installed == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_package_version(thing, expected):
    '''
    test package version

    CLI Example::

        salt '*' infratest.test_package_version exim4 2.0-pre4-1
    '''
    
    detail = '{0} is version: {1}'.format(thing, str(expected))
    if Package(thing).version.startswith(str(expected)):
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_service_isrunning(thing, expected):
    '''
    test if service is running

    CLI Example::

        salt '*' infratest.test_service_isrunning exim4 true
    '''
    
    detail = '{0} is running: {1}'.format(thing, expected)
    if Service(thing).is_running == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_service_isenabled(thing, expected):
    '''
    test if service is enabled

    CLI Example::

        salt '*' infratest.test_service_isenabled exim4 true
    '''
    
    detail = '{0} is enabled: {1}'.format(thing, expected)
    if Service(thing).is_enabled == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_socket_islistening(thing, expected):
    '''
    test if socket is listening

    CLI Example::

        salt '*' infratest.test_socket_islistening tcp://22 true
    '''
    
    detail = '{0} is listening: {1}'.format(thing, expected)
    if Socket(thing).is_listening == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_user_exists(thing, expected):
    '''
    test if user exists

    CLI Example::

        salt '*' infratest.test_user_exists root true
    '''
    
    detail = '{0} exists: {1}'.format(thing, expected)
    if User(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_uid(thing, expected):
    '''
    test user uid

    CLI Example::

        salt '*' infratest.test_user_uid root 0
    '''
    
    detail = '{0} has uid: {1}'.format(thing, expected)
    if User(thing).uid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_gid(thing, expected):
    '''
    test user gid

    CLI Example::

        salt '*' infratest.test_user_gid root 0
    '''
    
    detail = '{0} has gid: {1}'.format(thing, expected)
    if User(thing).gid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_group(thing, expected):
    '''
    test if user is in a group

    CLI Example::

        salt '*' infratest.test_user_group root wheel
    '''
    
    detail = '{0} has group: {1}'.format(thing, expected)
    if User(thing).group == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_gids(thing, expected):
    '''
    test user has the gids listed

    CLI Example::

        salt '*' infratest.test_user_gids root 0,1,2
    '''
    
    detail = '{0} has gids: {1}'.format(thing, expected)
    if User(thing).gids == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_groups(thing, expected):
    '''
    test if user has the groups listed

    CLI Example::

        salt '*' infratest.test_user_groups root root,wheel
    '''
    
    detail = '{0} has groups: {1}'.format(thing, expected)
    if User(thing).groups == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_home(thing, expected):
    '''
    test user's home directory

    CLI Example::

        salt '*' infratest.test_user_home foo /home/foo
    '''
    
    detail = '{0} has home: {1}'.format(thing, expected)
    if User(thing).home == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_shell(thing, expected):
    '''
    test user's shell

    CLI Example::

        salt '*' infratest.test_user_shell foo /bin/bash
    '''
    
    detail = '{0} has shell: {1}'.format(thing, expected)
    if User(thing).shell == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_group_exists(thing, expected):
    '''
    test if group exists

    CLI Example::

        salt '*' infratest.test_group_exists bar true
    '''
    
    detail = '{0} exists: {1}'.format(thing, expected)
    if Group(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_group_gid(thing, expected):
    '''
    test if group has the set gid

    CLI Example::

        salt '*' infratest.test_group_gid bar 2
    '''
    
    detail = '{0} has gid: {1}'.format(thing, expected)
    if Group(thing).gid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_interface_exists(thing, expected):
    '''
    test if an interface is present

    CLI Example::

        salt '*' infratest.test_interface_exists eth1 true
    '''
    
    detail = '{0} exists: {1}'.format(thing, expected)
    if Interface(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_interface_speed(thing, expected):
    '''
    test interface speed setting

    CLI Example::

        salt '*' infratest.test_interface_speed eth0 1000
    '''
    
    detail = '{0} has speed: {1}'.format(thing, expected)
    if Interface(thing).speed == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_interface_address(thing, expected):
    '''
    test if an interface has the set address

    CLI Example::

        salt '*' infratest.test_interface_address eth0 192.168.1.2
    '''
    
    detail = '{0} has address: {1}'.format(thing, expected)
    if expected in Interface(thing).addresses:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_type(expected):
    '''
    test the system type

    CLI Example::

        salt '*' infratest.test_systeminfo_type linux
    '''
    
    detail = 'type: {0}'.format(expected)
    if SystemInfo.type == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_distribution(expected):
    '''
    test the system distribution

    CLI Example::

        salt '*' infratest.test_systeminfo_distribution debian
    '''
    
    detail = 'distribution: {0}'.format(expected)
    if SystemInfo.distribution == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_release(expected):
    '''
    test the system release version

    CLI Example::

        salt '*' infratest.test_systeminfo_release '8.3'
    '''
    
    detail = 'release: {0}'.format(expected)
    if SystemInfo.release == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_codename(expected):
    '''
    test the system codename

    CLI Example::

        salt '*' infratest.test_systeminfo_codename sarge
    '''
    
    detail = 'codename: {0}'.format(expected)
    if SystemInfo.codename == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_sysctl(thing, expected):
    '''
    test if a sysctl setting is present

    CLI Example::

        salt '*' infratest.test_systeminfo_type linux
    '''
    
    detail = '{1}: {0}'.format(thing, expected)
    if Sysctl(thing) == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    

def run_all(details=True):
    try:
        __salt__
    except:
        return (False, 'could not get pillar data')
    else:
        tests =  __salt__['pillar.get']('infratest')
        
    if 'file' in tests:
        for key, vals in tests['file'].items():
            if 'exists' in vals:
                test_file_exists(key,vals['exists'])
            if 'type' in vals:
                if vals['type'] == 'file':
                    test_file_isfile(key, vals['type'])
                elif vals['type'] == 'directory':
                    test_file_isdir(key, vals['type'])
                elif vals['type'] == 'pipe':
                    test_file_ispipe(key, vals['type'])
                elif vals['type'] == 'socket':
                    test_file_issocket(key, vals['type'])
                elif vals['type'] == 'symlink':
                    test_file_issymlink(key, vals['type'])
                else:
                    INFRATEST['Failed'].append("{} could not find a type match: {}".format(key, vals['type']))
            if 'linkedto' in vals:
                test_file_linkedto(key, vals['linkedto'])
            if 'user' in vals:
                test_file_user(key, vals['user'])
            if 'group' in vals:
                test_file_group(key, vals['group'])
            if 'uid' in vals:
                test_file_uid(key, vals['uid'])
            if 'gid' in vals:
                test_file_gid(key, vals['gid'])
            if 'mode' in vals:
                test_file_mode(key, vals['mode'])
            if 'contains' in vals:
                if type(vals['contains']) == list:
                    for content in vals['contains']:
                        test_file_contains(key, content)
                else:
                    test_file_contains(key, vals['contains'])
            if 'md5sum' in vals:
                test_file_md5sum(key, vals['md5sum'])
            if 'sha256sum' in vals:
                test_file_sha256sum(key, vals['sha256sum'])
            if 'mtime' in vals:
                test_file_mtime(key, vals['mtime'])
            if 'size' in vals:
                test_file_size(key, vals['size'])
            
    if 'package' in tests:
        for key, vals in tests['package'].items():
            if 'installed' in vals:
                test_package_isinstalled(key, vals['installed'])
            if 'version' in vals:
                test_package_version(key, vals['version'])
        
    if 'service' in tests:
        for key, vals in tests['service'].items():
            if 'running'in vals:
                test_service_isrunning(key, vals['running'])
            if 'enabled' in vals:
                test_service_isenabled(key, vals['enabled'])
        
    if 'socket' in tests:
        for key, vals in tests['socket'].items():
            if 'listening' in vals:
                test_socket_islistening(key, vals['listening'])
                
    if 'user' in tests:
        for key, vals in tests['user'].items():
            if 'exists' in vals:
                test_user_exists(key, vals['exists'])
            if 'uid' in vals:
                test_user_uid(key, vals['uid'])
            if 'gid' in vals:
                test_user_gid(key, vals['gid'])
            if 'group' in vals:
                test_user_group(key, vals['group'])
            if 'gids' in vals:
                test_user_gids(key, vals['gids'])
            if 'groups' in vals:
                test_user_groups(key, vals['groups'])
            if 'home' in vals:
                test_user_home(key, vals['home'])
            if 'shell' in vals:
                test_user_shell(key, vals['shell'])
    
    if 'group' in tests:
        for key, vals in tests['group'].items():
            if 'exists' in vals:
                test_group_exists(key, vals['exists'])
            if 'gid' in vals:
                test_group_gid(key, vals['gid'])
    
    if 'interface' in tests:
        for key, vals in tests['interface'].items():
            if 'exists' in vals:
                test_interface_exists(key, vals['exists'])
            if 'speed' in vals:
                test_interface_speed(key, vals['speed'])
            if 'addresses' in vals:
                if type(vals['addresses']) == list:
                    # list of addresses
                    for address in vals['addresses']:
                        test_interface_address(key, address)
                else:
                    # single address, string
                    test_interface_address(key, vals['addresses'])
    
    if 'systeminfo' in tests:
        if 'type' in tests['systeminfo']:
            test_systeminfo_type(tests['systeminfo']['type'])
        if 'distribution' in tests['systeminfo']:
            test_systeminfo_distribution(tests['systeminfo']['distribution'])
        if 'release' in tests['systeminfo']:
            test_systeminfo_release(tests['systeminfo']['release'])
        if 'codename' in tests['systeminfo']:
            test_systeminfo_codename(tests['systeminfo']['codename'])
                
    if 'sysctl' in tests:
        for key, vals in tests['sysctl'].items():
            test_sysctl(key, vals['value'])
    
    INFRATEST['Totals'] = {}
    INFRATEST['Totals']['Pass'] = 0
    INFRATEST['Totals']['Fail'] = 0
    
    for result in INFRATEST['Passed']:
        INFRATEST['Totals']['Pass'] += 1

    for result in INFRATEST['Failed']:
        INFRATEST['Totals']['Fail'] += 1

    if details:
        return INFRATEST
    else:
        return INFRATEST['Totals']
