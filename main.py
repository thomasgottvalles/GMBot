from bose.launch_tasks import launch_tasks
from bose import LocalStorage
from src import tasks_to_be_run




msg = "Love It? Star It!  https://github.com/thomasgottvalles/GMBot"

def print_pro_bot():
    global msg
    print(msg) 

if __name__ == "__main__":

    launch_tasks(*tasks_to_be_run)
    count = LocalStorage.get_item('count', 0)
    
    if count % 5 == 0:
        print_pro_bot()
