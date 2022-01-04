echo "0 */2 * * *  $(pwd)/run_ngrok.sh" | tee -a /var/spool/cron/crontabs/$USER
