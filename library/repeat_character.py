#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: repeat_character
short_description: Repeats a character many times to test size limits
version_added: "2.10"
description:
    - "Tries to break ansible-runner callback reciever"
options:
    character:
        description:
            - Character to repeat in output data
        required: false
        default: a
    times:
        description:
            - Number of times to repeat character
        required: false
        default: 1000
'''

EXAMPLES = '''
- name: Repeat a character
  repeat_character:
    character: b
    times: 500
'''

RETURN = '''
message:
    description: The output message that the test module generates
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        character=dict(type='str', required=False, default='a'),
        times=dict(type='int', required=False, default=1000)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    module.exit_json(
        changed=False,
        message=module.params['character'] * module.params['times']
    )

def main():
    run_module()

if __name__ == '__main__':
    main()
