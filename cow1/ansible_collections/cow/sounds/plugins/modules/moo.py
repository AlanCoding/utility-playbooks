#!/usr/bin/python

# Copyright: public domain
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: moo
author: "Alan Rominger <please dont email me about this>"
version_added: "2.10"
short_description: moo.
description:
    - Test module that returns "moo" for the sound.
options:
'''


EXAMPLES = '''
- moo:
'''

from ansible.module_utils.basic import AnsibleModule


def main():

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    if module.check_mode:
        module.exit_json(**{'changed': False, 'sound': 'nom'})

    module.exit_json(**{'changed': True, 'sound': 'moo'})


if __name__ == '__main__':
    main()
