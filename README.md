# random-sqs

A simple program to test the Amazon SQS product. Just messing around.

## Installation
To configure, modify `random-sqs.env` with your paramters, and your QUEUE_URL for your Amazon SQS instance.

`sudo make install`
`sudo systemctl start random-sqs`

You will need to add your .aws/config and .aws/configuration files to /root for the system service to run properly. 

## Example Logs

```console

(venv) adam@ubuntu:~/projects/random-sqs$ sudo journalctl -r -u random-sqs
-- Logs begin at Wed 2020-09-02 07:17:26 PDT, end at Tue 2021-03-09 21:51:47 PST. --
Mar 09 21:48:15 ubuntu systemd[1]: Stopped Sample Python System Service.
Mar 09 21:48:15 ubuntu systemd[1]: Stopping Sample Python System Service...
Mar 09 21:48:14 ubuntu python3[31178]: consumer-3 Received and deleted message: This message was produced by publisher-0 AT 2021-03-09 21:48:14.669608
Mar 09 21:48:14 ubuntu python3[31178]: publisher-0 Produced new message at 2021-03-09 21:48:14.731094
Mar 09 21:48:13 ubuntu python3[31178]: consumer-1 Received and deleted message: This message was produced by publisher-0 AT 2021-03-09 21:48:12.100171
Mar 09 21:48:12 ubuntu python3[31178]: consumer-3 Received and deleted message: This message was produced by publisher-0 AT 2021-03-09 21:48:10.337067
Mar 09 21:48:12 ubuntu python3[31178]: publisher-0 Produced new message at 2021-03-09 21:48:12.172656
Mar 09 21:48:11 ubuntu python3[31178]: consumer-4 Received and deleted message: This message was produced by publisher-1 AT 2021-03-09 21:48:11.075066
Mar 09 21:48:11 ubuntu python3[31178]: publisher-1 Produced new message at 2021-03-09 21:48:11.129139
Mar 09 21:48:10 ubuntu python3[31178]: publisher-0 Produced new message at 2021-03-09 21:48:10.392761

```