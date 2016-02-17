# -*- coding: utf-8 -*-
'''
infratest

module to test server state using testinfra
documentation for the main python project: http://testinfra.readthedocs.org/
'''

import testinfra
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
    if 'pillar.get' in __salt__:
        global tests
        tests =  __salt__['pillar.get']('infratest')
        return __virtualname__
    return False

def test_file_exists(thing, expected):
    detail = '{} exists: {}'.format(thing, expected)
    if File(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_isfile(thing, expected):
    detail = '{} is: {}'.format(thing, expected)
    if File(thing).is_file:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_isdir(thing, expected):
    detail = '{} is: {}'.format(thing, expected)
    if File(thing).is_directory:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_ispipe(thing, expected):
    detail = '{} is: {}'.format(thing, expected)
    if File(thing).is_pipe:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_issocket(thing, expected):
    detail = '{} is: {}'.format(thing, expected)
    if File(thing).is_socket:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_issymlink(thing, expected):
    detail = '{} is: {}'.format(thing, expected)
    if File(thing).is_symlink:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_linkedto(thing, expected):
    detail = '{} is linked to: {}'.format(thing, expected)
    if File(thing).linked_to == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_user(thing, expected):
    detail = '{} is owned by user: {}'.format(thing, expected)
    if File(thing).user == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_group(thing, expected):
    detail = '{} is owned by group: {}'.format(thing, expected)
    if File(thing).group == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_uid(thing, expected):
    detail = '{} is owned by uid: {}'.format(thing, expected)
    if File(thing).uid == vals['uid']:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_gid(thing, expected):
    detail = '{} is owned by gid: {}'.format(thing, expected)
    if File(thing).gid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_mode(thing, expected):
    if type(expected) == int:
        # convert int to str if required
        expected = str(expected)
    if len(expected) == 3:
        # add 0 pad to mode, i.e. 644 => 0644
        expected = '0' + expected
    detail = '{} has mode: {}'.format(thing, expected)
    if oct(File(thing).mode) == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_contains(thing, expected):
    detail = '{} contains: {}'.format(thing, expected)
    if File(thing).contains(expected):
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_md5sum(thing, expected):
    detail = '{} has md5sum: {}'.format(thing, expected)
    if File(thing).md5sum == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_file_sha256sum(thing, expected):
    detail = '{} has sha256sum: {}'.format(thing, expected)
    if File(thing).sha256sum == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_mtime(thing, expected):
    '''
    python yaml tries to convert dates automatically on import
    but it is not predictable, necessarily
    make sure datetime in pillar is in quotes
    i.e. mtime: '2015-09-01 23:11:03'
    see https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html#automatic-datetime-conversion
    '''
    detail = '{} has mtime: {}'.format(thing, expected)
    if File(thing).mtime.strftime('%Y-%m-%d %H:%M:%S') == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_file_size(thing, expected):
    detail = '{} has size: {}'.format(thing, expected)
    if File(thing).size == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_package_isinstalled(thing, expected):
    detail = '{} is installed: {}'.format(thing, expected)
    if Package(thing).is_installed == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_package_version(thing, expected):
    detail = '{} is version: {}'.format(thing, str(expected))
    if Package(thing).version.startswith(str(expected)):
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_service_isrunning(thing, expected):
    detail = '{} is running: {}'.format(thing, expected)
    if Service(thing).is_running == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_service_isenabled(thing, expected):
    detail = '{} is enabled: {}'.format(thing, expected)
    if Service(thing).is_enabled == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_socket_islistening(thing, expected):
    detail = '{} is listening: {}'.format(thing, expected)
    if Socket(thing).is_listening == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_user_exists(thing, expected):
    detail = '{} exists: {}'.format(thing, expected)
    if User(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_uid(thing, expected):
    detail = '{} has uid: {}'.format(thing, expected)
    if User(thing).uid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_gid(thing, expected):
    detail = '{} has gid: {}'.format(thing, expected)
    if User(thing).gid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_group(thing, expected):
    detail = '{} has group: {}'.format(thing, expected)
    if User(thing).group == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_gids(thing, expected):
    detail = '{} has gids: {}'.format(thing, expected)
    if User(thing).gids == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_groups(thing, expected):
    detail = '{} has groups: {}'.format(thing, expected)
    if User(thing).groups == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_home(thing, expected):
    detail = '{} has home: {}'.format(thing, expected)
    if User(thing).home == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_user_shell(thing, expected):
    detail = '{} has shell: {}'.format(thing, expected)
    if User(thing).shell == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST

def test_group_exists(thing, expected):
    detail = '{} exists: {}'.format(thing, expected)
    if Group(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_group_gid(thing, expected):
    detail = '{} has gid: {}'.format(thing, expected)
    if Group(thing).gid == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_interface_exists(thing, expected):
    detail = '{} exists: {}'.format(thing, expected)
    if Interface(thing).exists == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_interface_speed(thing, expected):
    detail = '{} has speed: {}'.format(thing, expected)
    if Interface(thing).speed == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_interface_address(thing, expected):
    detail = '{} has address: {}'.format(thing, expected)
    if expected in Interface(thing).addresses:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_type(expected):
    '''
    finds an expected type from a given list
    '''
    detail = 'type: {}'.format(expected)
    if SystemInfo.type == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_distribution(expected):
    '''
    finds an expected distribution from an given list
    '''
    detail = 'distribution: {}'.format(expected)
    if SystemInfo.distribution == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_release(expected):
    '''
    finds an expected release from a given list
    '''
    detail = 'release: {}'.format(expected)
    if SystemInfo.release == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_systeminfo_codename(expected):
    '''
    finds an expected codename from a given list
    '''
    detail = 'codename: {}'.format(expected)
    if SystemInfo.codename == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    
def test_sysctl(thing, expected):
    '''
    tests to see if sysctl setting is as expected
    '''
    detail = '{}: {}'.format(thing, expected)
    if Sysctl(thing) == expected:
        INFRATEST['Passed'].append(detail)
    else:
        INFRATEST['Failed'].append(detail)
    return INFRATEST
    

def run_all(details=True):
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
