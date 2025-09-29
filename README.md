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


[//]: # (obligatory branding for EOSC.CZ)
<hr style="margin-top: 100px; margin-bottom: 20px">

<p style="text-align: left"> <img src="https://webcentrum.muni.cz/media/3831863/seda_eosc.png" alt="EOSC CZ Logo" height="90"> </p>
This project output was developed with financial contributions from the EOSC CZ initiative throught the project National Repository Platform for Research Data (CZ.02.01.01/00/23_014/0008787) funded by Programme Johannes Amos Comenius (P JAC) of the Ministry of Education, Youth and Sports of the Czech Republic (MEYS).

<p style="text-align: left"> <img src="https://webcentrum.muni.cz/media/3832168/seda_eu-msmt_eng.png" alt="EU and MŠMT Logos" height="90"> </p>
