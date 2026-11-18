import socket

def start_server(host='127.0.0.1', port=65432):
    # Создаем TCP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"[СЕРВЕР] Слушаю {host}:{port}...")

        while True:
            # Блокирующий вызов accept - ждем клиента
            conn, addr = s.accept()
            with conn:
                print(f"[СЕРВЕР] Подключен клиент: {addr}")
                while True:
                    # Блокирующий вызов recv - ждем данные
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    # Декодируем, переводим в верхний регистр
                    text = data.decode('utf-8')
                    response = text.upper()
                    print(f"[СЕРВЕР] Получено: '{text}' -> Отправлено: '{response}'")
                    
                    # Отправляем обратно
                    conn.sendall(response.encode('utf-8'))
                print(f"[СЕРВЕР] Клиент {addr} отключен.")

if __name__ == "__main__":
    start_server()