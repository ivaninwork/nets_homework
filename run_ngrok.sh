NGROK_JOB_PID_FILE=~/ngrok/ngrok_job_pid.txt 
if [ -f $NGROK_JOB_PID_FILE ]; then
    kill $(cat $NGROK_JOB_PID_FILE )
fi
~/ngrok/ngrok http 8000 --log=stdout > ~/ngrok/ngrok.log &
NGROK_JOB_PID=$!
echo $NGROK_JOB_PID > $NGROK_JOB_PID_FILE
