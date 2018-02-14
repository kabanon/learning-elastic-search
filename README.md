# Learning Elasticsearch
## Working environment
- Ubuntu 16.04
- Docker 17.12.0-ce
- Elasticsearch 6.2.1
## Requirements
- [Install working environnement](./01-Install-working-environnement)
## Run Elasticsearch
```bash
#!/bin/bash
sudo docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.1
```
## Summary
- [Install working environnement](./01-Install-working-environnement)
- [Discovering Elasticsearch Query API](./02-Discovering-Elasticsearch-Query-API)
