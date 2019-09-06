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

### Colored Output

This playbook runs a command that produces colored output.
Normally the output is not shown, but it will be if you run in
verbose mode or if you use a callback plugin.

```
ansible-playbook -i localhost, -e ansible_python_interpreter=$(which python) color_outputs.yml -vvv
ANSIBLE_STDOUT_CALLBACK=json ansible-playbook -i localhost, -e ansible_python_interpreter=$(which python) color_outputs.yml
```

### Test Use of collection

```
ansible-galaxy collection install chrismeyersfsu.tower_modules:0.0.1 -p alan
ANSIBLE_COLLECTIONS_PATHS=alan ansible-playbook -i localhost, -e ansible_python_interpreter=$(which python) tower_module_chris.yml
```

This will run a tower module, but this is not enough information to say it worked,
because the same modules already exist in Ansible core. To verify that, modify
your local Ansible install with the diff:

```
diff --git a/lib/ansible/modules/web_infrastructure/ansible_tower/tower_organization.py b/lib/ansible/modules/web_infrastructure/ansible_tower/tower_organization.py
index bba58d8894..f3e9586e69 100644
--- a/lib/ansible/modules/web_infrastructure/ansible_tower/tower_organization.py
+++ b/lib/ansible/modules/web_infrastructure/ansible_tower/tower_organization.py
@@ -88,6 +88,7 @@ def main():
             module.fail_json(msg='Failed to update the organization: {0}'.format(excinfo), changed=False)

     json_output['changed'] = result['changed']
+    json_output['this_is_the_old_one'] = True
     module.exit_json(**json_output)
```

And then run without the collection:

```
ansible-playbook -i localhost, -e ansible_python_interpreter=$(which python) tower_module_chris.yml
```

That output (and not the output when using the 'alan' collection path) should
contain `"this_is_the_old_one": true`.
This will confirm that the collection is working.

#### Doc Fragments

from issue https://github.com/ansible/ansible/issues/56226, we use the -M flag
as well as setting the collection path.

works:

```
ANSIBLE_COLLECTIONS_PATHS=alan ansible-doc -M alan/ansible_collections/chrismeyersfsu/tower_modules/plugins/modules/ -t module tower_organization
```

wrong:

```
ansible-doc -M alan/ansible_collections/chrismeyersfsu/tower_modules/plugins/modules/ -t module tower_organization
ERROR! module tower_organization missing documentation (or could not parse documentation): unknown doc_fragment(s) in file /Users/alancoding/Documents/repos/utility-playbooks/alan/ansible_collections/chrismeyersfsu/tower_modules/plugins/modules/tower_organization.py: chrismeyersfsu.tower_modules.tower
```

gives the wrong docs:

```
ANSIBLE_COLLECTIONS_PATHS=alan ansible-doc -t module tower_organization
```
