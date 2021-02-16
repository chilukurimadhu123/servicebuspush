from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = "Endpoint=sb://test-service-bus-queue.servicebus.windows.net/;SharedAccessKeyName=my-policy;SharedAccessKey=5QRc6X4wF6ibeUEXvma3WrlUBKGxNBgDFegMVUpKopQ=;EntityPath=test-queue"
QUEUE_NAME = "test-queue"

def send_single_message(sender):
    input_msg=input("enter data to push")
    message = ServiceBusMessage(input_msg)
    sender.send_messages(message)
    print("Sent a single message")

servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        send_single_message(sender)