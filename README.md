# Ansible Role: solr

This is an Ansible solr role with systemd support, the service is configured similar to what happens with the solr install\_solr\_service.sh script, but by implementing the code in Ansible it allows systemd support and easier idempotent results.
The role also allows to create cores with custom configuration if you configure a path in item.src in solr\_cores.

## Requirements

The standard solr requirements apply. To avoid additional dependencies for the installation of a single package, the role can also install openjdk.
The role has been tested with solr 8.

## Role Variables


Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies


## Examples

Include the role in your playbook:

```
    - hosts: servers
      roles:
         - role: fiaasco.solr
```

## Tags

No tags available.

## License

MIT

## Credits

This role got some inspiration from:
* https://github.com/jiv-e/ansible-multicore-solr
* https://github.com/geerlingguy/ansible-role-solr
Both MIT licensed.


## Author Information

Luc Stroobant
