from Functions import WaitTimer, GeneratePlanning, driverConfigure ,SendMessage, SendAttachment, SearchGroupOrContact
from datetime import datetime
import os, getpass
from dotenv import load_dotenv
load_dotenv()


#  ///////////////// WhatsApp Message Scheduler v1.0 //////////////////////////
# ///////////////////          For Chrome          ///////////////////////////

# MAIN
if __name__ == '__main__':
#====================================================================================================================================
    #PERSONAL VARIABLES:
    load_dotenv(".env")
    username = getpass.getuser()
    target_file_path = os.getenv("ONEDRIVEPATH").format(username=username)
#====================================================================================================================================
    #PATH VARIABLES:
    load_dotenv(".env.defaults")
    profile_name = os.getenv("PROFILENAME")
    chrome_for_testing_path = os.getenv("CHROMETESTINGPATH")
    chrome_driver_path = os.getenv("CHROMEDRIVERPATH")
    Chrome_user_dir_path = os.getenv("CHROMEUSERDIRPATH").format(username=username, profile_name=profile_name)
#====================================================================================================================================
    #NAMES, DATES & TEXT VARIABLES:
    current_date = datetime.now()
    formatted_date_short = current_date.strftime('%b-%d-%y')
# =========================================================================================================================
    #Group_or_chat_name = 'Tech - Parmon Trade World' # //////////// WARNING TECH SELECTED //////////////////
    Group_or_chat_name = 'AlexoPlayer'
    Message_to_send = "Hello Everyone, good morning, here is my daily planning"

    Testing_Group_or_chat_name = 'El grupo de las ardillas'
    Testing_Message_to_send = "==== Test message: everything works! ===="
#====================================================================================================================================
    #FILES AND DOCS VARIABLES:
    template_name = 'DailyPlanning template.xlsx'
    new_filename = f"DailyPlanning {formatted_date_short}.xlsx"
    template_path = f'{target_file_path}/{template_name}'
    File_path = f'{target_file_path}\\{new_filename}'
#====================================================================================================================================
    #XPATHS VARIABLES:
    Search_box_xpath = os.getenv("SEARCHBOX")
    Message_box_xpath = os.getenv("MESSAGEBOX")
    Attach_button_xpath =os.getenv("ATTACHBUTTON")
    Document_button_xpath = os.getenv("DOCUMENTBUTTON")
    Attached_send_button = os.getenv("SENDATTACHMENT")
#====================================================================================================================================
    
    driver = driverConfigure(Chrome_user_dir_path,chrome_for_testing_path,chrome_driver_path,profile_name)
    
    #Generate planning and wait 3 minutes
    GeneratePlanning(template_path,File_path)
    WaitTimer(180)
    # block execution time =3 minutes, Total time = 3 minutes

    #Send Test Message and wait 3 minutes and 30 seconds
    SearchGroupOrContact(driver, Search_box_xpath,Testing_Group_or_chat_name)
    SendMessage(driver, Message_box_xpath,Testing_Message_to_send)
    SendAttachment(driver, Attach_button_xpath,Document_button_xpath,File_path,Attached_send_button)
    Testing_Message_to_send = "Everything Works Confirmed"
    WaitTimer(30)
    SendMessage(driver, Message_box_xpath,Testing_Message_to_send)
    WaitTimer(180)
    # block execution time = 4 minutes and 35 seconds, Total time = 7 minutes and 35 seconds

    #Send Real Message and wait 2 minutes
    SearchGroupOrContact(driver, Search_box_xpath,Group_or_chat_name)
    SendMessage(driver, Message_box_xpath,Message_to_send)
    SendAttachment(driver, Attach_button_xpath,Document_button_xpath,File_path,Attached_send_button)
    WaitTimer(120)
    # Total time = 2 minutes and 30 seconds

    #Final execution 10 minutes and 5 seconds
    driver.quit()