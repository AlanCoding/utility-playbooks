# utility-playbooks
Ansible playbooks for various things that need to be done

Things that these do

 - install simplejson on a system
 - install python rpm bindings
 - install python apt bindings for Fedora

### Cloud Module Testing

This playbook serves the role of testing authentication to various
Ansible modules.

Example:

```
ansible-playbook -i localhost, cloud_module_testing.yml -e ansible_python_interpreter=$(which python) --tags=tower
```

this command will yield a number of possible results:

 - error due to `ansible-tower-cli` not being installed
 - authentication failure to host `127.0.0.1`
 - authentication failure to provided host
 - success

Why might it attempt to connect to `127.0.0.1` there? Because this is the
default setting value! If the intent was to provide a host, then failing
to connect to _this_ host is an indicator that the authentication was
not correctly specified.
