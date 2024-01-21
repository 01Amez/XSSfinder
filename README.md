# Downloading and Using waybackurls on Windows

## Install Go

1. Download the latest stable version of Go from the official website: [https://golang.org/dl/](https://golang.org/dl/)
2. Run the Go installer and follow the installation instructions.

## Set Up Environment Variables (if not set up automatically)

1. Open the Start menu and search for "Environment Variables."
2. Click on "Edit the system environment variables."
3. In the System Properties window, click the "Environment Variables" button.
4. In the Environment Variables window, locate the "Path" variable in the "System variables" section and click "Edit."
5. Click "New" and add the path to the Go bin directory (e.g., `C:\Go\bin`).

## Open a Command Prompt

1. Open a new Command Prompt window to execute commands.

## Download and Install waybackurls

1. Run the following command to download and install waybackurls using Go:
    ```bash
    go get github.com/tomnomnom/waybackurls
    ```

2. Verify the installation:
    ```bash
    waybackurls -h
    ```
   This command should display the help message for waybackurls, indicating a successful installation.


## Navigate to XSSfinder Directory

1. After downloading or cloning the XSSfinder repository, navigate to the XSSfinder directory using the following command:
    ```bash
    cd XSSfinder
    ```

2. Run the XSSfinder script:
    ```bash
    python xssfinder.py
    ```
   Adjust the command based on your Python environment and script location.

That's it! You have successfully downloaded waybackurls, navigated to the XSSfinder directory, and run the xssfinder.py script on your Windows machine.
