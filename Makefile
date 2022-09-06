# -*- coding: utf-8 -*-

help: ## Show this help message
	@perl -nle'print $& if m{^[a-zA-Z0-9_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'


update-gzip: ## Update all *.tsv.gz file
	python ./bin/update_gzip.py


restore-tsv: ## Restore all *.tsv file
	python ./bin/restore_tsv.py
