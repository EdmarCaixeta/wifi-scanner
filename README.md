This application aims to scan all WiFi networks in your PC range, listing: SSID, Signal and MAC Address. Furthermore, the application also appends those informations into an existent .csv file or creates a new one if inexistent, if the flag --store is used.

To run it:
    
    pip3 install -r requirements.txt (If you don't have the required modules installed on your Python Environment)
    
    python3 scanner.py <flags>
    
Flags:

    --store: save the data into a csv file, existent or not.
