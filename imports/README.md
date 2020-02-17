### Import testing

Tests the ability to import things in various collections and other ways
of defining module_utils.

#### Without collection

trying with callback plugin, did not work:
(imports can not import)

```
ANSIBLE_CALLBACK_PLUGINS=non_collection/callbacks ANSIBLE_MODULE_UTILS=non_collection/utils ansible-playbook ../debug_verbosity.yml -i localhost,
```

trying with inventory, did not work:

```
ANSIBLE_INVENTORY_PLUGINS=non_collection/inventory ANSIBLE_MODULE_UTILS=non_collection/utils ansible-playbook ../debug_verbosity.yml -i test_inventory.yml
```

Repeating, but using folder named literally "module_utils:
did not work:

```
ANSIBLE_STDOUT_CALLBACK=test_display ANSIBLE_CALLBACK_PLUGINS=non_collection/callbacks ANSIBLE_MODULE_UTILS=non_collection/module_utils ansible-playbook ../debug_verbosity.yml -i localhost,
```

same with inventory plugin:

```
ANSIBLE_INVENTORY_PLUGINS=non_collection/inventory ANSIBLE_MODULE_UTILS=non_collection/module_utils ansible-playbook ../debug_verbosity.yml -i test_inventory.yml
```

trying with module:

this works

```
ANSIBLE_MODULE_UTILS=non_collection/module_utils ansible localhost -m test_module
```

#### With collection

This "works" (by failing):

```
ANSIBLE_STDOUT_CALLBACK=foo.bar.test_display ANSIBLE_COLLECTIONS_PATHS=col ansible-playbook ../debug_verbosity.yml -i localhost,
```

This works

```
ANSIBLE_COLLECTIONS_PATHS=col ansible localhost -m foo.bar.test_module
```

##### Conclusions

This is very hard to get right, and all of the conclusions above are non-obvious.
The custom module_utils path can be used, but only under certain circumstances.
Due to come presumed circular issue, the display callback seems to be unable
to import from the custom set user module_utils folder, although the same
can be imported by modules themselves. This probably relates to loading order
in some way or another.

However, the very same configuration works if done by a collection, instead
of modifying the Ansible paths for these resources.
This is likely related to the fact that collections are a different kind
of package, with root of `ansible_collections` as opposed to `ansible`, but
this is all still speculation.

Even the collection case, however, did not work using the `__init__.py` example,
"foo" in the examples.
