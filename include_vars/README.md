### Including encrypted variables

This tests the use of the include_vars task in conjunction with vaulted
Ansible variables. How to use:

Details of the vault credential needed:
 - id: alan
 - password: password

Run the playbook

```
ansible-playbook -i localhost, include_vars/vault_vars.yml --vault-id=alan@prompt
```

The next sections explain the generation of the secrets.

#### Whole-file encrypted variables

This is derived from example at:

https://gist.github.com/tristanfisher/e5a306144a637dc739e7

The original unencrypted version of the variables is provided at
`stuff_backup.yml`, this is then copied to the destination where it
gets encrypted.

```
cp include_vars/stuff_backup.yml include_vars/stuff.yml
ansible-vault encrypt include_vars/stuff.yml --vault-id=alan@prompt
```

#### Single variable encrypted

Here, the file `thing.yml` is not encrypted itself, but values inside of it
are encrypted. To do encryption, use command:

```
ansible-vault encrypt_string --vault-id=alan@prompt
```

Paste in the text:

```
people run into some space aliens and they end up fighting them
```

Then this is saved to the `thing.yml` file under the variable `spoiler_text`.

