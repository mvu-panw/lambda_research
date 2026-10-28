# Connecting to an instance - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/on-demand/connecting-instance/

Skip to content

# Connecting to an instance#

You can connect to your On-Demand Cloud (ODC) instances directly through SSH or
by using the preinstalled JupyterLab server.

## Setting up SSH access#

Before you launch an instance into a workspace, you must add an SSH key to that
workspace. When you go through the process of launching an instance, you'll
be prompted to supply this SSH key so you can securely connect to the instance
after launching. You can import an existing key if you have one, or you can
generate a new one in the Lambda Cloud console.

### Adding an existing SSH key#

If you have an existing SSH key, you can add it to a workspace and use it to
connect to your instances. Lambda Cloud accepts SSH keys in the following
formats:

- OpenSSH, the format ssh-keygen uses by default when generating keys.

- RFC4716, the format PuTTYgen uses when you save a public key.

- PKCS8

- PEM

View examples of each key type

OpenSSH keys look like:

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK5HIO+OQSyFjz0clkvg+48YAihYMo5J7AGKiq+9Alg8 foo@bar

RFC4716 keys begin with:

---- BEGIN SSH2 PUBLIC KEY ----

PKCS8 keys begin with:

-----BEGIN PUBLIC KEY-----

PEM keys begin with:

-----BEGIN RSA PUBLIC KEY-----

To add an existing SSH key to a workspace:

- Navigate to the SSH keys page
 in the Lambda Cloud console.

- If needed, click the workspace dropdown at the top of the console and select
 your target workspace.

- Click Add SSH Key. A dialog appears.

- In the dialog, in the text input box, paste your public SSH key.

- Enter a name for your key, then click Add SSH key.

You can also add an SSH key through the Lambda Cloud API. For details, see
Add an SSH key
in the Lambda Cloud API browser.

### Generating a new SSH key#

If you don't have an SSH key, you can generate one in the Lambda Cloud console.
Lambda Cloud generates SSH keys in PEM format.

To generate a new SSH key:

- Navigate to the
 SSH keys page
 in the Lambda Cloud console.

- Click Add SSH Key. A dialog appears.

- Click Generate a new SSH key.

- Enter a name for your key, then click Create.

Depending on your browser settings, your key will automatically download to your
default download folder or you'll be prompted to select a download location.

You can also generate an SSH key through the Lambda Cloud API. For details, see
Add an SSH key
in the Lambda Cloud API browser.

### Deleting an SSH key#

To delete an SSH key from your workspace:

- Navigate to the
 SSH keys page
 in the Lambda Cloud console.

- In your key's row, in the Actions column, click Delete. A dialog
 appears.

- Click Delete SSH key.

You can also delete an SSH key through the Lambda Cloud API. For details, see
the following sections in the
Lambda Cloud API browser:

- List your SSH keys:
 Used to retrieve the SSH key ID.

- Delete an SSH key:
 Used to perform the delete operation.

## Establishing an SSH connection#

After you've added or generated an SSH key, you can establish a connection to
your instance. To establish an SSH connection:

- Navigate to the
 Instances page
 in the Lambda Cloud console.

- In your instance's row, in the IP Address column, click your IP
 address to copy it.

- 

On your local machine, in your terminal, run the following command.
 Substitute <SSH-KEY-FILE-PATH> with the path to your SSH key, and
substitute <INSTANCE-IP> with your instance's IP address:

ssh -i '<SSH-KEY-FILE-PATH>' ubuntu@<INSTANCE-IP>

### Using an SSH tunnel#

To use services on Lambda instances without opening additional ports in your
Lambda Cloud firewall, you can set up an SSH tunnel. An SSH tunnel forwards a
port on your local machine to a port on your ODC instance using an SSH
connection.

To set up an SSH tunnel, run the following command in your local terminal,
replacing the following placeholders:

- Replace <LOCAL-PORT> with the port from which you want to access the
 service locally.

- Replace <REMOTE-PORT> with the port on which the remote service is running.

- Replace <REMOTE-IP> with the public IP of your Lambda instance.

ssh -L <LOCAL-PORT>:127.0.0.1:<REMOTE-PORT> ubuntu@<INSTANCE-IP>

You can now access the remote service from your local machine at
localhost:<LOCAL-PORT> or 127.0.0.1:<LOCAL-PORT>.

### Using multiple SSH keys#

When you create a new ODC instance, you add a single SSH key to the instance. If
needed, you can add more SSH keys by adding the relevant public keys to
~/.ssh/authorized_keys on your instance:

- Establish an SSH connection to your instance.

- 

Use echo to append your public key to ~/.ssh/authorized_keys.
 Substitute <PUBLIC-KEY> with your public key, and make sure not to remove
the quotes around <PUBLIC-KEY>.

echo '<PUBLIC-KEY>' >> ~/.ssh/authorized_keys

- 

Verify that the key has been added:

cat ~/.ssh/authorized_keys

You should now be able to log into your instance using the SSH key you just
added.

### Importing an SSH key from GitHub#

To import an SSH key from a GitHub account and add it to your ODC instance:

- 

Using your existing SSH key, establish an SSH connection to your instance.

Note

Alternatively, you can open a terminal inside your instance's
JupyterLab. For details on accessing JupyterLab, see Accessing
JupyterLab and Jupyter notebooks below.

- 

Import the SSH key from the GitHub account. Replace <USERNAME> with
 the GitHub account's username:

ssh-import-id gh:<USERNAME>

If the import is successful, you should see output similar to the following:

2023-08-04 15:03:52,622 INFO Authorized key ['256', 'SHA256:C6pl0q4evVYZWcyByVF69D6fdbdKa7F8ei8V2F/bTW0', 'cbrownstein-lambda@github/67649580', '(ED25519)']
2023-08-04 15:03:52,623 INFO [1] SSH keys [Authorized]

## Accessing JupyterLab and Jupyter notebooks#

Lambda's default machine image preinstalls JupyterLab on your instance. To open
JupyterLab on your instance:

- Navigate to the
 Instances page
 in the Lambda Cloud console.

- In your instance's row, in the Cloud IDE column, click Launch.
 JupyterLab opens.

Note

If you launched your instance using a different machine image, your instance
might not have JupyterLab installed. If JupyterLab hasn't been installed,
you won't see a Launch link for that instance.

## Connecting to your instance's desktop environment#

If you prefer working in a graphical desktop environment, you can set one up
on your ODC instance and then connect to it remotely. First, install and
configure your desktop environment and VNC server:

- 

Establish an SSH connection to your instance, as described in the
 Establishing an SSH connection section
 above.

Note

Alternatively, you can open a terminal inside your instance's
JupyterLab. For details on accessing JupyterLab, see Accessing
JupyterLab and Jupyter notebooks above.

- 

Install the TightVNC server and the desktop environment you want to use.
 These steps use GNOME for the desktop environment:

sudo apt update &&
sudo apt install -y tightvncserver gnome

- 

Start the VNC server to create a VNC session. You're prompted to set a
 password.

vncserver

- 

After you set your password, open ~/.vnc/xstartup for editing:

nano ~/.vnc/xstartup

- 

Replace the contents of the file with the following lines and then save.
 If you installed a different desktop environment, substitute startgnome
 with the appropriate command for that environment:

#!/bin/sh
export XKL_XMODMAP_DISABLE=1
export XDG_CURRENT_DESKTOP=GNOME
/etc/X11/Xsession
xrdb $HOME/.Xresources
startgnome &

- 

Make the file executable:

chmod +x ~/.vnc/xstartup

- 

Restart your server:

vncserver -kill :1 &&
vncserver :1

Now that your VNC server is running, you can set up a secure connection to
your desktop environment:

- On your local machine, navigate to the
 Instances page
 in the Lambda Cloud console and copy your instance's IP address.

- 

Open a terminal and create an SSH tunnel to your instance. Replace
 <API-KEY-PATH> with the local path to the SSH key you associated
 with your instance when you created the instance, <USERNAME> with your
 username, and <INSTANCE-IP> with your instance's IP address:

ssh -i '<API-KEY-PATH>' -L 5901:localhost:5901 <USERNAME>@<INSTANCE-IP>

Note

Most VNC servers choose the port on which to serve a display by adding
the display number to 5900. Because you're connecting to display 1,
this example connects on port 5901.

- 

Install your preferred VNC client solution.

- In your client, connect to localhost:5091 and then enter your VNC
 server password. Your desktop environment should appear in a new window.

## Next steps#

- New to ODC? Check out the ODC Overview.

- For guidance on managing your ODC environment, see
 Managing your system environment.

 Back to top
