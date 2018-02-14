# Discovering Elasticsearch

## Requirements
- Run Elasticsearch

## Init working space
```bash
./00-Init-working-space.sh
```
## Working with simple requests
### List all families - Sort by id ASC
```bash
http GET 127.0.0.1:9200/rome/_search < json/01.00-get_families.json
```
### List all domains of family "A", sort by id ASC
```bash
http GET 127.0.0.1:9200/rome/_search < json/02.00-get_domains.json
```
### List all domains of family "A", sort label id ASC
Not a good idea ! Look : the output is not as expected !
-> @todo : check how to fix this..
```bash
http PUT 127.0.0.1:9200/rome/_mapping/_doc < json/02.01-0-get_domains_order_by_label.json
```
Fix illegal_argument_exception error :
```bash
http PUT 127.0.0.1:9200/rome/_mapping/_doc < json/02.01-0-get_domains_order_by_label.json
```
And run again the request.
```
http GET 127.0.0.1:9200/rome/_search < json/02.01-1-get_domains_order_by_label.json
```
(′︿‵｡)
### Get all jobs associated to "Espaces naturels et espaces verts"
```bash
http GET 127.0.0.1:9200/rome/_search < json/03.00-get_card.json
```
### Get all jobs releated to "Protection du patrimoine naturel"
```bash
http GET 127.0.0.1:9200/rome/_search < json/04.00-get_jobs.json
```
### Get all jobs releated to "Protection du patrimoine naturel", with "parc" in label
Scoring is coming... (sort element have been removed)
```bash
http GET 127.0.0.1:9200/rome/_search < json/05.00-get_jobs-parc.json
```
### Get all jobs releated to "Protection du patrimoine naturel", with "parc" and "garde" in label
```bash
http GET 127.0.0.1:9200/rome/_search < json/06.00-get_jobs-parc-garde.json
```
Test with "terms"... But "terms" filters documents that have fields that match any of the provided terms
```bash
http GET 127.0.0.1:9200/rome/_search < json/06.01-get_jobs-parc-garde.json
```
One term by must :
```bash
http GET 127.0.0.1:9200/rome/_search < json/06.02-get_jobs-parc-garde.json
```
### Get all jobs releated to "Protection du patrimoine naturel", with "parc" and "garde" in label but not "moniteur"
```bash
http GET 127.0.0.1:9200/rome/_search < json/06.03-get_jobs-parc-garde-moniteur.json
```
### Get all jobs with "web" in label
```bash
http GET 127.0.0.1:9200/rome/_search < json/07.00-get_jobs-web.json
```
### Get all jobs with "web" in label and "developpeur" or "designer" in label
```bash
http GET 127.0.0.1:9200/rome/_search < json/08.00-get_jobs-web.json
```
