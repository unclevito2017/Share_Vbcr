# Share_Vbcr 
tested on Win 10<br>
Add share functionality to VBCr.exe<br>
Completes all shares requested<br>
first download VBCr.exe from https://github.com/WanderingPhilosopher/VanBitCrackenRandom2 <br>
run python3 share_Vbcr.py<br>
adjust time.sleep(70)  # (default) Wait for 70 seconds. adjust to your gpu speed
command = f'VBCr.exe -t 0 -gpu -gpuId 0 -begr {start_keyspace} -endr {end_keyspace} -o {output_filename} -drk 1 -dis 1 -r 30000 -c 13zb1hQb'<br> 
adjust -t cpu threads -r for number of random and 13zb1hQb for desired prefix length <br>
