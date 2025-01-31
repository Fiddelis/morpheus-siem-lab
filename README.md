# Morpheus SIEM Lab

Este projeto configura um laboratório para testes de SIEM.

## Construção das Imagens Docker

Antes de subir o ambiente, é necessário buildar as imagens Docker:

```sh
cd ./morpheus-siem-lab

docker build -t logstash ./logstash/
docker build -t morpheus ./morpheus/
docker build -t suricata ./suricata/
```

## Inicializando o Laboratório

### 1. Elasticsearch e Kibana
```sh
docker compose -f ./elasticsearch_kibana/docker-compose.yml up -d
```

### 4. Morpheus
```sh
# Pré-requisitos: https://docs.nvidia.com/morpheus/getting_started.html#requirements
docker run --rm -ti --runtime=nvidia --gpus=all --net=elastic_siem-net --cap-add=sys_nice \
  --name=morpheus -v /var/run/docker.sock:/var/run/docker.sock morpheus bash
```

### 2. Suricata
```sh
docker run -it --net=elastic_siem-net --name=suricata --rm suricata bash
```

### 3. Logstash
```sh
docker run --rm -it --net=elastic_siem-net --volumes-from=suricata --name=logstash logstash
```
