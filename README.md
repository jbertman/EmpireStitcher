Wraps the Emp\*re stagers with Python for conditional execution

##Usage

    usage: stitcher.py [-h] [-w WINDOWS] [-n NIX]

    Stich together Emp*re stagers (python) to conditionally execute based on platform

    optional arguments:
    -h, --help            show this help message and exit
    -w WINDOWS, --windows WINDOWS
                        Path to Windows (Empire) stager
    -n NIX, --nix NIX     Path to *nix (EmPyre) stager  

You need both a Windows (Powershell Empire) and a \*nix (EmPyre) stager.

You can drop them to file using the OutFile parameter in the respective launcher modules.

After your listeners are set up. You can generate stagers for each one:

    usestager launcher
    set Listener test
    set OutFile /root/nix_stager.txt
    generate

Perform the same for Powershell Empire.

When you're ready for stitching:

    python stitcher.py -w windows_stager.txt -n nix_stager.txt

The output can be pasted in either Windows or \*nix terminals for cross-platform execution.
