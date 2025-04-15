import socket


def pod_name(request):
    return {
        'pod_name': socket.gethostname()
    }
