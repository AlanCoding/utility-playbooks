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

### Collection Conflict Testing

There are two folders which offer a collection by the same name.
These collection namespaces are `cow1.sounds` and `cow2.sounds`.
The playbook `cow.yml` will invoke the `moo` module which exists in
both collections.

The point here is to test which module will be ran.

Run just one module:

```
ANSIBLE_COLLECTIONS_PATHS=cow1 ansible-playbook -i localhost, cow.yml
ANSIBLE_COLLECTIONS_PATHS=cow2 ansible-playbook -i localhost, cow.yml
```

the first cow makes a short "moo", the second cow makes a longer and
more lifelike moo-like sound.

Now, make them compete.

```
ANSIBLE_COLLECTIONS_PATHS=cow2:cow1 ansible-playbook -i localhost, cow.yml
ANSIBLE_COLLECTIONS_PATHS=cow1:cow2 ansible-playbook -i localhost, cow.yml
```

You can see that the output in both of these cases is different.
The 2nd one does "moo".
This means that the 1st entry has higher precedence.
