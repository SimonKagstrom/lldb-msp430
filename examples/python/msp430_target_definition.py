#!/usr/bin/python
#===-- msp430_target_definition.py -----------------------------*- C++ -*-===//
#
#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.
#
#===----------------------------------------------------------------------===//

#----------------------------------------------------------------------
# DESCRIPTION
#
# This file can be used with the following setting:
#   plugin.process.gdb-remote.target-definition-file
# This setting should be used when you are trying to connect to a 
# remote GDB server that doesn't support any of the register discovery
# packets that LLDB normally uses. This is the case for mspdebug,
# a gdb-server for MSP430 that LLDB was tested to work with.
#
# USAGE
#
# (lldb) settings set plugin.process.gdb-remote.target-definition-file /path/to/msp430_target_definition.py
# (lldb) gdb-remote 2000
#
#----------------------------------------------------------------------
from lldb import *

# Compiler and DWARF register numbers
name_to_gcc_dwarf_regnum = {
    'r0'   : 0 ,
    'r1'   : 1 ,
    'r2'   : 2 ,
    'r3'   : 3 ,
    'r4'   : 4 ,
    'r5'   : 5 ,
    'r6'   : 6 ,
    'r7'   : 7 ,
    'r8'    : 8 ,
    'r9'    : 9 ,
    'r10'   : 10,
    'r11'   : 11,
    'r12'   : 12,
    'r13'   : 13,
    'r14'   : 14,
    'r15'   : 15,
};

name_to_gdb_regnum = {
    'r0'   : 0 ,
    'r1'   : 1 ,
    'r2'   : 2 ,
    'r3'   : 3 ,
    'r4'   : 4 ,
    'r5'   : 5 ,
    'r6'   : 6 ,
    'r7'   : 7 ,
    'r8'    : 8 ,
    'r9'    : 9 ,
    'r10'   : 10,
    'r11'   : 11,
    'r12'   : 12,
    'r13'   : 13,
    'r14'   : 14,
    'r15'   : 15,
};

name_to_generic_regnum = {
    'r0' : LLDB_REGNUM_GENERIC_PC,
    'r1' : LLDB_REGNUM_GENERIC_SP,
};


def get_reg_num (reg_num_dict, reg_name):
    if reg_name in reg_num_dict:
        return reg_num_dict[reg_name]
    return LLDB_INVALID_REGNUM

def get_reg_num (reg_num_dict, reg_name):
    if reg_name in reg_num_dict:
        return reg_num_dict[reg_name]
    return LLDB_INVALID_REGNUM

msp_register_infos = [
{ 'name':'r0'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo, 'alt-name':'pc' },
{ 'name':'r1'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo, 'alt-name':'sp' },
{ 'name':'r2'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r3'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r4'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r5'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r6'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r7'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r8'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r9'    , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r10'   , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r11'   , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r12'   , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r13'   , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r14'   , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
{ 'name':'r15'   , 'set':0, 'bitsize':16 , 'encoding':eEncodingUint  , 'format':eFormatAddressInfo   },
];

g_target_definition = None

def get_target_definition ():
    global g_target_definition
    if g_target_definition == None:
        g_target_definition = {}
        offset = 0
        for reg_info in msp_register_infos:
            reg_name = reg_info['name']

            # Only fill in the offset if there is no 'slice' in the register info
            if 'slice' not in reg_info and 'composite' not in reg_info:
                reg_info['offset'] = offset
                offset += reg_info['bitsize']/8

            # Set the GCC/DWARF register number for this register if it has one    
            reg_num = get_reg_num(name_to_gcc_dwarf_regnum, reg_name)
            if reg_num != LLDB_INVALID_REGNUM:
                reg_info['gcc'] = reg_num
                reg_info['dwarf'] = reg_num

            # Set the generic register number for this register if it has one    
            reg_num = get_reg_num(name_to_generic_regnum, reg_name)
            if reg_num != LLDB_INVALID_REGNUM:
                reg_info['generic'] = reg_num

            # Set the GDB register number for this register if it has one    
            reg_num = get_reg_num(name_to_gdb_regnum, reg_name)
            if reg_num != LLDB_INVALID_REGNUM:
                reg_info['gdb'] = reg_num

        g_target_definition['sets'] = ['General Purpose Registers']
        g_target_definition['registers'] = msp_register_infos
        g_target_definition['host-info'] = { 'triple'   : 'msp430-unknown-unknown', 'endian': eByteOrderLittle }
        g_target_definition['g-packet-size'] = offset
    return g_target_definition

def get_dynamic_setting(target, setting_name):
    if setting_name == 'gdb-server-target-definition':
        return get_target_definition()
