OMERO search engine
===================

Installs and configures the OMERO search engine.

Dependencies
------------

OMERO.docker.web is required.


Role Variables
--------------

- `apps_folder'`: The application data folder
- `database_server_url`: The database URL
- `database_port`: The database port
- `database_name`: The database name (e.g. omero)
- `database_username`: The database username
- `database_user_password`: The database user password
- `default_datasource`: The default datasource
- `search_engineelasticsearch_docker_image`: The Elasticsearch image (default: `docker.elastic.co/elasticsearch/elasticsearch:9.2.1`)
- `searchengine_docker_image`: The search engine Docker image
- `automatic_refresh`: Whether the search engine should reload the configuration when modified (true/false)
- `searchengine_secret_key`: The search engine secret key
- `searchengineurlprefix`: The URL prefix for the search engine (default: searchengine)
- `elasticsearch_no_nodes`: The number of nodes in the Elasticsearch cluster
- `elasticsearch_backup_folder`: The Elasticsearch data backup folder
- `ca_password`:  The CA password for the Elasticsearch certificate
- `keystore_password`: The keystore password for the Elasticsearch cluster
- `elastic_password`: The password for the Elasticsearch user
- `data_dump_folder`: The data dump folder (used for asynchronous search and container BFFs)
- `nginx_port`: The port Nginx should use
- `cache_rows`: The number of rows the indexing process can handle at one time
- `no_index_processes`: The number of parallel processes available for the indexing process

Example Playbook
----------------
::

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
         - database_user_password: mypassword
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
         - searchengine_docker_image: khaledk2/searchengine:new_packages


The role can also be used for:


- index the data
::

        ansible-playbook install_searchengine.yml  --tags "indexer"

- Backup the Elasticsearch data
::

    ansible-playbook install_searchengine.yml  --tags "backup"

- Restore the Elasticsearch data
::

    ansible-playbook install_searchengine.yml  --tags "restore"
- Generate the BFF files for the for the screens:
::

    ansible-playbook install_searchengine.yml  --tags "bff_screens"

- Generate the BFF files for the for the projects:
::

    ansible-playbook install_searchengine.yml  --tags "bff_projects"

Assuming the installation playbook name is `install_searchengine.yml`

Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk

