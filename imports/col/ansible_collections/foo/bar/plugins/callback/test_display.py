


# from ansible_collections.foo.bar.plugins import module_utils
# raise Exception(module_utils.foo)

from ansible_collections.foo.bar.plugins.module_utils.stuff import bar
raise Exception(bar)


from ansible.plugins.callback.default import CallbackModule
