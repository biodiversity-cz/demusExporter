# demus exporter
convert from old Czech herbaria&museums software [DEMUS](https://www.citem.cz/citem/wpress/projekty/demus/), [link2](https://emuzeum.cz/metodicka-centra/edicni-cinnost/metodicke-a-odborne-texty/software/demus-dokumentace-a-evidence-muzejnich-sbirek) data (mdb export „Běžný“) into the JACQ import table format


## local run
```shell
sudo apt update
sudo apt install mdbtools unixodbc-dev 

poetry env use python3.13
poetry install

poetry run python test.py
```

