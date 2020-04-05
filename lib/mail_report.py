import logging 
import os


def mail_report(config):

    logger = logging.getLogger("debug_log") 
    something = "this is inside perform diff  "
    logger.info("I am warning you about %s", something)


    # send mail
    output_directory = config.get('UNIQUE','output_directory')
    cmd_mail_report = "/usr/sbin/sendmail " + config.get('UNIQUE','report_distribution_email_ids') + " < "+  output_directory + "/report.html"
    logger.info ( cmd_mail_report )
    os.system(cmd_mail_report )




