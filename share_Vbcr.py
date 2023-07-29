import subprocess
import time
import os
import signal

Tips = 'bc1qus09g0n5jwg79gje76zxqmzt3gpw80dcqspsmm'

def run_vbcr(start_keyspace, end_keyspace, share_number):
    output_filename = f'share{share_number}.txt'  
    command = f'VBCr.exe -t 0 -gpu -gpuId 0 -begr {start_keyspace} -endr {end_keyspace} -o {output_filename} -drk 1 -dis 1 -r 30000 -c 13zb1hQb'

    process = subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    time.sleep(70)  # Wait for 70 seconds
    process.send_signal(signal.CTRL_BREAK_EVENT)  
    process.wait()  # Wait for the process to exit


# Main loop
start_keyspace = input("Enter the starting keyspace value (hex): ")
end_keyspace = input("Enter the ending keyspace value (hex): ")
num_shares = int(input("Enter the number of shares: "))
increment = hex(int((int(end_keyspace, 16) - int(start_keyspace, 16) + 1) / num_shares))[2:]  

current_keyspace = start_keyspace
for share_number in range(1, num_shares + 1):
    next_keyspace = hex(int(current_keyspace, 16) + int(increment, 16) - 1)[2:]  
    print(f"Share {share_number}/{num_shares}")
    print(f"Keyspace Range: {current_keyspace} - {next_keyspace}")
    run_vbcr(current_keyspace, next_keyspace, share_number)
    time.sleep(5)  # Wait for 5 seconds before starting the next subrange
    current_keyspace = hex(int(next_keyspace, 16) + 1)[2:]  

print("All shares processed.")
