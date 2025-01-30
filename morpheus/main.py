import logging
from morpheus.config import Config
from morpheus.pipeline import LinearPipeline
from morpheus.stages.general.monitor_stage import MonitorStage
from morpheus.stages.input.http_server_source_stage import HttpServerSourceStage
from morpheus.stages.output.write_to_elasticsearch_stage import WriteToElasticsearchStage
from morpheus.utils.logger import configure_logging

def run_pipeline():
    # Configura o Log do Morpheus
    configure_logging(log_level=logging.DEBUG)

    config = Config()

    # Cria um pipeline linear
    pipeline = LinearPipeline(config)

    # Configura o estágio de entrada como um servidor HTTP
    pipeline.set_source(HttpServerSourceStage(config))

    # Adiciona um estágio de monitoramento
    pipeline.add_stage(MonitorStage(config))

    # Configura o estágio de escrita para o Elasticsearch
    elasticsearch_stage = WriteToElasticsearchStage(
        config=config,
        index="morpheus-logs",
        host="http://localhost:9200",
        auth=("elastic", "teste@123")
    )

    # Adiciona o estágio ao pipeline
    pipeline.add_stage(elasticsearch_stage)

    # Executa o pipeline
    pipeline.run()

if __name__ == "__main__":
    run_pipeline()
