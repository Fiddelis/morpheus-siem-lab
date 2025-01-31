import logging
from morpheus.config import Config
from morpheus.pipeline import LinearPipeline
from morpheus.stages.general.monitor_stage import MonitorStage
from morpheus.utils.http_utils import HTTPMethod
from morpheus.stages.input.http_server_source_stage import HttpServerSourceStage
from morpheus.utils.logger import configure_logging
from morpheus.stages.output.http_client_sink_stage import HttpClientSinkStage

def run_pipeline():
    # Configura o Log do Morpheus
    configure_logging(log_level=logging.DEBUG)

    config = Config()

    # Cria um pipeline linear
    pipeline = LinearPipeline(config)

    # Configura o estágio de entrada como um servidor HTTP
    pipeline.set_source(HttpServerSourceStage(config,
                            bind_address="0.0.0.0",
                            port=80,
                            lines=True,
                            endpoint="/message"))

    # Adiciona um estágio de monitoramento
    pipeline.add_stage(MonitorStage(config))

    # Configura o estágio de escrita para o Elasticsearch
    pipeline.add_stage(HttpClientSinkStage(config,
                            base_url="http://elastic:123456@elasticsearch:9200",
                            endpoint="/suricata-log/_doc",
                            method=HTTPMethod.POST,
                            lines=True,
                            headers={"Content-Type": "application/json"}))
    pipeline.run()

if __name__ == "__main__":
    run_pipeline()
