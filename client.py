import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"[КЛИЕНТ] Подключен к {host}:{port}")
            
            while True:
                message = input("Введите сообщение (или 'exit' для выхода): ")
                if message.lower() == 'exit':
                    break
                
                # Отправляем данные
                s.sendall(message.encode('utf-8'))
                
                # Ждем ответ (блокирующий режим)
                data = s.recv(1024)
                print(f"[КЛИЕНТ] Ответ сервера: {data.decode('utf-8')}")
                
        except ConnectionRefusedError:
            print("[КЛИЕНТ] Ошибка: Сервер не запущен.")

if __name__ == "__main__":
    start_client()