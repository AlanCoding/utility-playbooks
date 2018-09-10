### Overriding the Ansible config

This is an example where the Ansible config is changed by putting a
config file in the cwd.

You need to run this playbook from the cwd.

Example of it working with ini file:

```
cd config_override/
ansible-playbook -i inv/inventory.ini debug.yml
```

Example of it not working with script file:

```
cd config_override/
ansible-playbook -i inv/foobar.py debug.yml
```

In AWX, it should work in both cases.
