import socket
import tkinter as tk
import threading





def port_scan():

    target_host = host_entry.get() if host_entry.get() else "127.0.0.1"
    start_port = int(start_port_entry.get()) if start_port_entry.get() else 10
    end_port = int(end_port_entry.get()) if end_port_entry.get() else 200
    num_threads = int(threads_entry.get()) if threads_entry.get() else 10

    result_text.delete("1.0", tk.END)  # Clear the result text
    result_text.insert(tk.END, f"Starting Port Scanning...\n\n")

    # Calculate the number of threads based on the port range
    num_threads = min(end_port - start_port + 1, 10)  # Limit to a maximum of 100 threads
    
    # Create a list to hold the threads
    threads = []
    
    # Divide the port range into equal chunks for each thread
    port_chunks = chunk_port_range(start_port, end_port, num_threads)
    
    # Create a separate thread for each port chunk
    for ports in port_chunks:
        thread = threading.Thread(target=perform_port_scan, args=(target_host, ports))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    # for thread in threads:
    #     thread.join()

    
    


def chunk_port_range(start_port, end_port, num_chunks):
    port_range = end_port - start_port + 1
    chunk_size = port_range // num_chunks
    remaining_ports = port_range % num_chunks
    
    ports = []
    current_port = start_port
    
    for _ in range(num_chunks):
        chunk_end_port = current_port + chunk_size - 1
        
        if remaining_ports > 0:
            chunk_end_port += 1
            remaining_ports -= 1
        
        ports.append((current_port, chunk_end_port))
        current_port = chunk_end_port + 1
    
    return ports


def perform_port_scan(target_host, port_range):

    for port in range(port_range[0], port_range[1]):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            result = sock.connect_ex((target_host, port))
            
            if result == 0:
                result_text.insert(tk.END, f"Port {port} is open\n")
            else:
                result_text.insert(tk.END, f"Port {port} is closed\n")

            
            sock.close()
        except socket.error:
            result_text.insert(tk.END, f"Error occurred while scanning port {port}\n")


# Create the GUI
window = tk.Tk()
window.title("Port Scanner")

frame = tk.Frame(window)
frame.pack()

# Host Entry
host_label = tk.Label(frame, text="Host:")
host_label.pack(padx=10, pady=10)
host_entry = tk.Entry(frame)
host_entry.pack()

# Start Port Entry
start_port_label = tk.Label(frame, text="Start Port:")
start_port_label.pack(padx=10, pady=10)
start_port_entry = tk.Entry(frame)
start_port_entry.pack()

# End Port Entry
end_port_label = tk.Label(frame, text="End Port:")
end_port_label.pack(padx=10, pady=10)
end_port_entry = tk.Entry(frame)
end_port_entry.pack()


threads_label = tk.Label(frame, text="Number Threads:")
threads_label.pack(padx=10, pady=10)
threads_entry = tk.Entry(frame)
threads_entry.pack()


# Scan Button
empty_label = tk.Label(frame, text="")
empty_label.pack()

scan_button = tk.Button(frame, text="Start Scanning", command=port_scan,padx=10, pady=10)
scan_button.pack()

empty_label2 = tk.Label(frame, text="")
empty_label2.pack()


# Result Text
result_text = tk.Text(frame, height=20, width=60)
result_text.pack()

window.mainloop()