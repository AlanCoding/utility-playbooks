

from ansible_collections.foo.bar.plugins.module_utils.stuff import bar
raise Exception(bar)


from ansible.plugins.callback.default import CallbackModule
