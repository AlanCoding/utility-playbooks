#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.stuff import bar

module = AnsibleModule(
    argument_spec = dict()
)
module.exit_json(changed=True, bar=bar)