from bose.launch_tasks import launch_tasks
from bose import LocalStorage
from src import tasks_to_be_run

# TG - Code added to fork
from vendor.EmailScraper.start import main
import os



msg = "Love It? Star It!  https://github.com/thomasgottvalles/GMBot"

def print_pro_bot():
    global msg
    print(msg) 

if __name__ == "__main__":
    launch_tasks(*tasks_to_be_run)
    count = LocalStorage.get_item('count', 0)
    
    # TG - Code added to fork
    os.chdir('vendor/EmailScraper')
    main()
    
    if count % 5 == 0:
        print_pro_bot()
