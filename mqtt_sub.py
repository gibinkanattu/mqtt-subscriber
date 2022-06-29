import paho.mqtt.client as mqtt 
import json,sys,time,argparse,logging

def parse_argv(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--conf", required=True)
    args = parser.parse_args(argv)
    args = vars(args)    
    return args
flag=True
def on_message(client, userdata, msg):
    msg_payload = msg.payload.decode("utf-8")
    print(msg_payload)
    if flag:
        logging.info(msg_payload)
        flag=False

def main():
    try:
        client = mqtt.Client()
        args = parse_argv(sys.argv[1:])
        conf_file=args.get("conf")
        with open(conf_file,"r") as fp:
            params   = json.load(fp)
            broker = params.get("broker")
            topic  = params.get("topic")
            port   = params.get("port")
            qos    = params.get("qos")
            log    = params.get("log")
        logging.basicConfig(filename=log, level=logging.ERROR)
        try:
            client.connect(broker,port)
            client.subscribe(topic)
            client.on_message=on_message
            client.loop_forever()
        except Exception as e:
            logging.error(e)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()