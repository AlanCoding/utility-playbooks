#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible_collections.foo.bar.plugins.module_utils.stuff import bar

module = AnsibleModule(
    argument_spec = dict()
)
module.exit_json(changed=True, foo=bar)