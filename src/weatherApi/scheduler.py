from apscheduler.schedulers.background import BackgroundScheduler
from jobs import scheduled_update
def start_jobs():
    scheduler = BackgroundScheduler()
    #run the scheduled job every two hours.
    
    cron_job = {'month': '*', 'day': '*', 'hour': '*2', 'minute':'*'}
    
    scheduler.add_job(scheduled_update, 'cron', **cron_job)
 
    scheduler.start()