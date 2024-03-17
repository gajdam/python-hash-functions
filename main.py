import hashlib
import time
import timeit
import plotly.graph_objects as go


def hash_all_available(data, verbose=False):
    """
    Hashes the given data using all available hash algorithms.

    Parameters:
        data (bytes): The data to be hashed.
        verbose (bool): If True, prints the hash for each algorithm. Default is False.

    Returns:
        dict: A dictionary containing hash values for each algorithm.
    """
    hashes = {}
    for algorithm in hashlib.algorithms_available:
        if algorithm.startswith('shake'):
            # Skip SHAKE algorithms as they require additional parameter
            continue
        hashed_data = hash_data(data, algorithm)
        hashes[algorithm] = hashed_data
        if verbose:
            print(f"{algorithm}: {hashed_data}")
    return hashes


def hash_file(file_path, hash_type='sha256'):
    """
    Calculates the hash of a file using the specified hash algorithm.

    Parameters:
        file_path (str): The path to the file.
        hash_type (str): The type of hash algorithm to use. Default is 'sha256'.

    Returns:
        str: The hexadecimal representation of the file's hash.
    """
    hash_obj = hashlib.new(hash_type)
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


import hashlib
import time
import matplotlib.pyplot as plt


def hash_data(data, hash_type='sha256'):
    """
    Calculates the hash of the given data using the specified hash algorithm.

    Parameters:
        data (bytes): The data to be hashed.
        hash_type (str): The type of hash algorithm to use. Default is 'sha256'.

    Returns:
        str: The hexadecimal representation of the hashed data.
    """
    hash_obj = hashlib.new(hash_type)
    hash_obj.update(data)
    return hash_obj.hexdigest()


def measure_hash_time(data_size, hash_type='sha256'):
    """
    Measures the time taken to hash data of given size using the specified hash algorithm.

    Parameters:
        data_size (int): The size of data in bytes.
        hash_type (str): The type of hash algorithm to use. Default is 'sha256'.

    Returns:
        float: The time taken to hash the data in seconds.
    """
    data = b'0' * data_size
    start_time = time.time()
    hash_data(data, hash_type)
    end_time = time.time()
    return end_time - start_time


def plot_hash_time_for_data_size(hash_type='sha256'):
    """
    Plots the time taken to hash data for different sizes using the specified hash algorithm.

    Parameters:
        hash_type (str): The type of hash algorithm to use. Default is 'sha256'.

    Returns:
        None
    """
    data_sizes = [10**i for i in range(1, 7)]  # List of data sizes from 10^1 to 10^6 bytes
    hash_times = [measure_hash_time(size, hash_type) for size in data_sizes]

    plt.plot(data_sizes, hash_times, marker='o')
    plt.xscale('log')
    plt.xlabel('Data Size (bytes)')
    plt.ylabel('Time (seconds)')
    plt.title(f'Hashing Time for {hash_type.upper()} Algorithm')
    plt.grid(True)
    plt.show()


def hash_control(choice, *args):
    """
    Controls the hashing process based on the user's choice.

    Parameters:
        choice (str): User's choice of action.
        args: Additional arguments based on the choice.

    Returns:
        None
    """
    if choice == '1':
        input_data = input("Enter data to hash: ").encode()
        hash_type = input("Choose hash algorithm from the list of available algorithms: ")
        hashed_data = hash_data(input_data, hash_type)
        print(f"Hashed data: {hashed_data}")


    elif choice == '2':
        file_path = args[0]
        # all_hashes = hash_all_available(open(file_path, 'rb').read())
        all_hashes = hash_all_available(open(file_path, 'rb').read())
        print("Hashes for all available algorithms:")

        for algorithm, hashed_data in all_hashes.items():
            print(f"{algorithm}: {hashed_data}")

    elif choice == '3':
        hash_type = input("Enter the hash algorithm to plot hashing time for (e.g., md5, sha256): ")
        plot_hash_time_for_data_size(hash_type.lower())

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    choice = input("Choose an option:\n1. Enter data to hash\n2. Hash a file with all available algorithms\n3. Plot hashing time for a specific algorithm\nEnter your choice: ")

    if choice in ('1', '2', '3'):
        if choice == '1':
            hash_control(choice)
        elif choice == '2':
            file_path = "C:\\Users\\gajda\\Downloads\\python-3.12.2-amd64.exe"
            # file_path = input("Enter the path to the file: ")
            hash_control(choice, file_path)
        elif choice == '3':
            hash_control(choice)
    else:
        print("Invalid choice.")
