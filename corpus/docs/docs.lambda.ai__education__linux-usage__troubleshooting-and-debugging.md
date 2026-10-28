# Troubleshooting and debugging - Lambda Docs

Source: https://docs.lambda.ai/education/linux-usage/troubleshooting-and-debugging/

Skip to content

# Troubleshooting and debugging#

## Linux#

### Generate a Lambda bug report#

Lambda bug reports are useful for troubleshooting systems with NVIDIA GPUs, including Cloud instances.

To generate a Lambda bug report, run:

wget -nv -O - https://raw.githubusercontent.com/lambdal-support/lambda-public-tools/main/lambda-bug-report.sh | bash -

Warning

You can run this script only on Lambda workstations and On-Demand Cloud instances. Do not run it on a cluster.

This command creates a file named lambda-bug-report.tar.gz in your current
directory. This file contains the Lambda bug report.

You can view the contents of the Lambda bug report by running tar -zxf
lambda-bug-report.tar.gz. This command creates a directory named
lambda-bug-report containing the contents of the Lambda bug report.

The Lambda bug report includes the NVIDIA bug report log file, which contains a
lot of information about the GPU. For tips on troubleshooting using the NVIDIA
bug report file, see Using the nvidia-bug-report.log file to troubleshoot your
system.

Note

Be sure to generate and provide a Lambda bug report whenever submitting a support ticket to Lambda Support. Providing a Lambda bug report when you first submit a ticket helps Support more quickly troubleshoot any problems you're experiencing with your Lambda system.

### Fix blank black screen with blinking cursor#

If your system boots to a blank black screen with a blinking cursor, rather than
the expected GUI, you might need to reinstall Lambda
Stack. To reinstall
Lambda Stack when the GUI doesn't launch:

Note

If your boot drive is encrypted, first enter your passphrase at the blank screen, then press Enter.

- Press Alt + Ctrl + F3 to switch to a virtual console, then log into Ubuntu using your usual login and password.

- 

Follow the instructions for removing and reinstalling Lambda Stack. Then, run sudo reboot to restart your system.

If after restarting you're still encountering a blank black screen with a
blinking cursor, follow step 1 again, then run sudo apt update && sudo apt
-y full-upgrade to update your system. When the update is finished, restart
your system by running sudo reboot.

Tip

If your system is set up for remote access via SSH, you can instead SSH into your system to run the commands listed in step 2.

## Windows#

### How do I gather system information in Windows using DxDiag?#

You can use the DirectX Diagnostic Tool
(DxDiag)
in Windows to gather system information that might be helpful for
troubleshooting.

To use DxDiag to gather system information:

- 

Press the Windows key + R to open the Run window. Type

dxdiag /dontskip /whql:off /64bit /t %userprofile%/Desktop/DxDiag.txt

then press Enter.
2. After 5-10 seconds, a file named DxDiag.txt will be created on the Desktop. This file contains information about the system.

If you prefer to use the graphical interface of DxDiag to gather system information:

- Press the Windows key + R to open the Run window.

- In the Run window, type dxdiag then press Enter.

- Click Save All Information to save the system information to a text file.

### How do I gather system information in Windows using MSINFO32?#

You can use
MSINFO32,
also known as Microsoft System Information or Msinfo32.exe, to gather useful
information for troubleshooting your computer.

To use MSINFO32:

- Press the Windows key + R to open the Run window. Type cmd then
 press Ctrl + Shift + Enter to open an elevated command prompt.

- 

In the elevated command prompt, run:

MSInfo32 /report %userprofile%/Desktop/sysinfo.txt

This will create a file on your Desktop named sysinfo.txt that contains useful information about your computer.

Note

You can additionally use DxDiag to gather useful information for troubleshooting.

### How do I prevent an incorrect clock in Windows after booting Ubuntu?#

Ubuntu saves the current time to the machine hardware clock in
UTC. Windows saves
the current time to the machine hardware clock in the local time. Because Ubuntu
and Windows save the current time to the machine hardware clock differently, the
current time displays incorrectly in Windows after booting Ubuntu.

To fix this problem:

- 

Press the Windows key + R to open the Run window. Type cmd then press Ctrl + Shift + Enter.

This command opens the Command Prompt window with elevated (admin) privileges.
2. In the Command Prompt window, run the command: reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG_DWORD /f.

If Windows asks to update the clock due to DST (Daylight Savings Time), let Windows update the clock. The current time will be saved to the machine hardware clock in UTC but will display in Windows in the local time.

To learn more about this problem, see the Arch Linux documentation on system time.

### How do I run a filesystem check on Windows and repair system files?#

If Windows is freezing or behaving erratically, there might be a problem with the filesystem or system files. Examples of erratic behavior include:

- blue screens

- crashing applications

- sluggish performance

- failed Windows updates

You can use the built-in Deployment Image Servicing and Management (DISM) and System File Checker (SFC) tools to try to fix the problem.

To use the DISM tool to fix problems with the filesystem or system files:

- Press the Windows key + R to open the Run window.

- 

In the Run window, type cmd then press Ctrl + Shift + Enter.

This command opens the Command Prompt window with elevated (admin) privileges.
3. In the Command Prompt window, run the command:

DISM.exe /Online /Cleanup-Image /RestoreHealth

This command performs cleanup and recovery operations on the system files. For more information, see Microsoft’s documentation on repairing a Windows image.
4. After DISM.exe finishes, run the following command in the Command Prompt window: sfc /scannow. This command scans all protected system files and replaces corrupted files. For more information, see Microsoft’s documentation on using SFC to repair missing or corrupted system files.

Run the sfc /scannow command up to 3 times until you receive the message: Windows Resource Protection did not find any integrity violations.

Note

If after running this command 3 times you do not receive the message Windows Resource Protection did not find any integrity violations, it is unlikely that a problem with the filesystem or system files is the cause of Windows freezing or behaving erratically.

Reboot the machine and test to see if Windows continues to freeze or behave erratically.

### Where can I find my Windows license key?#

If you purchased your system with Windows 11 preinstalled, you can download and reinstall Windows 11 without a license key.

If you purchased your system with Windows 10 preinstalled, your Windows license key is located on a cardboard envelope included with your system.

Cardboard envelope with Windows license key

Warning

Make sure not to lose your license key! We can't replace lost license keys.

Inside of the license key envelope is a sticker with the license key on it. We strongly suggest affixing this sticker to your system's chassis.

 Back to top
