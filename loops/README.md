### How do I take actions on files in a folder in Ansible

Two ways to accomplish the same general goal, demonstrated with the specific
problem of executing python scripts in the scripts folder.

```
ansible-playbook loops/loop_control.yml
ansible-playbook loops/fileglob.yml
```

Both of these will drop the `loops/scripts/file.txt` file down, proving
that they ran the scripts.
