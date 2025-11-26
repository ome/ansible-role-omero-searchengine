OMERO Searchengine
==================

[![Actions Status](https://github.com/ome/ansible-role-omero-ms-image-region/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-omero-ms-image-region/actions)
[![Ansible Role](https://img.shields.io/badge/ansible--galaxy-omero_ms_image_region-blue.svg)](https://galaxy.ansible.com/ui/standalone/roles/ome/omero_ms_image_region/)

Installs and configures the OMERO Searchengine.

Dependencies
------------

OMERO.docker.web is required.


Role Variables
--------------

- `apps_folder': The application based older
- 'database_server_url': The omero database url
- 'database_port': The omero database port
- 'database_name' :The omero database name (e.g. omero)
- 'database_username': the omero database user name
- 'database_user_password': the database user password
- 'default_datasource': The default datasource
- 'search_engineelasticsearch_docker_image': The elasticsearch image, default is 'docker.elastic.co/elasticsearch/elasticsearch:9.2.1'
- 'searchengine_docker_image': The searchengine docker image
- 'automatic_refresh': if the searchengine configuration is modified, the app will load the new configure in case of this varibale is true
- 'searchengine_secret_key': The search engine secret key
- 'searchengineurlprefix': Url prefix for the searchengine, default is 'searchengine'
- 'elasticsearch_no_nodes': Number of nodes in the elasticsearch cluster3
- 'elasticsearch_backup_folder': Elasticsearch data backup folder
- 'ca_password' : Ca password for the Elasticsearch certificate
- 'keystore_password' : keystore password for the Elasticsearch cluster
- 'elastic_password': The password for the Elasticsearch user
- 'data_dump_folder': The data dump folder, will be used in case of asynchronize search and containers BFF
- 'nginx_port': The port which Nginx should use
- 'cache_rows': The number of the rows which indexing process can handle on a time
- 'no_index_processes': Number of parallel processes which can be be used in the indexing process

Example Playbook
----------------

    - name: Deploying search engine
      connection: local
      hosts: localhost
      become: true

      roles:
      - role:  omero_searchengine
        vars:
         - elastic_password: Jlsp2cZirz6G56&^hdlhkf7
         - apps_folder: /data
         - asynchronous_search: true
         - automatic_refresh: true
         - cache_rows: 50000
         - database_name: idr
         - database_user_password: GDj2PSoCYYwt2BvWvsT3xePW42TocQ8ZaIpfFWIBjCJX
         - database_port: '5432'
         - database_server_url: 192.168.10.38
         - database_username: omeroreadonly
         - elasticsearch_backup_folder: /searchengine_backup
         - searchengine_secret_key  : searchengine_secret_key
         - verify_certs: false
         - quires_folder: quires/
         - data_dump_folder: /data/data_dump/
         - default_datasource: omero
         - searchengineurlprefix: "searchengine"
         - ca_password: "ca_password_1234"
         - keystore_password: "keystore_password_1234"
         - no_index_processes: 6
         - elasticsearch_no_nodes: 3
         - nginx_port: 8080