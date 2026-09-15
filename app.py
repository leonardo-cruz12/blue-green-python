import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


def crear_servidor(version, puerto):
    class Manejador(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/health':
                respuesta = f"OK: {version}"
                codigo = 200
            else:
                respuesta = f"Aplicación ejecutandose - version: {version}"
                codigo = 200
            self.send_response(codigo)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(respuesta.encode('utf-8'))


        def log_message(self, format, *args):
            return  # Desactivar el registro de solicitudes
    return HTTPServer(('127.0.0.1', puerto), Manejador)

#Funcion principal
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', type=str, required=True)
    parser.add_argument('--puerto', type=int, required=True)
    argumentos = parser.parse_args()

    servidor = crear_servidor(argumentos.version, argumentos.puerto)

    print(f"Servidor {argumentos.version} en http://127.0.0.1:{argumentos.puerto}")
    servidor.serve_forever()

if __name__ == '__main__':
    main()