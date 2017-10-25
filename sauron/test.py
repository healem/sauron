from common.config import Config
from common import loginit
from messaging.blocking.publisher import AMQPPublisher as Pub

loginit.initTestLogging()

cfg = Config("cfg/home.yaml")
exchange = "Test"
topic = "test.topic"

for broker in cfg.brokers:
    addr = broker['address']
    port = broker['port']
    sslpw = broker['ssl_pass']
    cacert = broker['ca_certs']
    keyFile = broker['key_file']
    certFile = broker['cert_file']
    pub = Pub(addr, port, cacert, keyFile, certFile)
    pub.publishOneShot(exchange, topic, "Test message")
    
    
    

