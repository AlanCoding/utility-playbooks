

from ansible.module_utils.stuff import bar
raise Exception(bar)

from ansible.module_utils import foo
raise Exception(foo)


from ansible.plugins.callback.default import CallbackModule
