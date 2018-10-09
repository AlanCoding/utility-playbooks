### Including encrypted variables

This is derived from example at:

https://gist.github.com/tristanfisher/e5a306144a637dc739e7

The original unencrypted version of the variables is provided at
`stuff_backup.yml`, this is then copied to the destination where it
gets encrypted.

```
cp include_vars/stuff_backup.yml include_vars/stuff.yml
ansible-vault encrypt include_vars/stuff.yml --vault-id=alan@prompt
```

Details of the vault credential needed:
 - id: alan
 - password: password

Run the playbook

```
ansible-playbook -i localhost, include_vars/vault_vars.yml --vault-id=alan@prompt
```
