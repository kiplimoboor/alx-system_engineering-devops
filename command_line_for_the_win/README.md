![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

## About 
Command line for the win Project

## Concepts Tested
1. Bash command line skills
2. Secure File Transfer Protocol (SFTP)

## Use of SFTP in the Project
The project involved tackling command line challenges at [Command Challenge](https://cmdchallenge.com).
Since the challenge is done in a local machine, yet the project folders are in a sandbox, the screenshot files from the project needed to be uploaded into the sandbox from the local machine. SFTP was thus utilized for the transfer.

The steps for using SFTP included:

1. Establish sftp session in the sandbox. To establish the session, use the command ``sftp username@hostname``. Enter the password when prompted.
2. The hostname, username, and password provided by ALX was used for the project.
2. Navigate to the directory where the file is to be uploaded. In this case. The directory was */command_line_for_the_win*.
3. Navigate to the directory with the screenshots in the local machine. Navigating in the local machine involved prefixing the sftp commands with an l. For example, while ``ls`` lists file in the sandbox, ``lls`` lists file in the local machine.
4. Use the ``put`` command to upload necessary from local machine to the sandbox.
5. Ending the sftp session with the ``exit`` command.
6. The  files are now available for any necessary actions in the sandbox.
